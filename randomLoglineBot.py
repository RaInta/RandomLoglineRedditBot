#!/usr/bin/python

##################################################
##   randomLoglineBot.py      ####################
##################################################
#
# This takes a random logline generator (logline.py)
# and turns it into a Reddit bot (www.reddit.com).
# The behaviour of # the bot is such that it will
# post a single reply to a post that includes the
# string "random logline".
#
# The reply post is a movie logline in the form of
# "A [PROTAGONIST] must [ACHIEVE GOAL] or [STAKES].
# They do this via [COOL STUFF IN MOVIE] and learns
# [THEME]."
#
# There are lists of each of the variables in
# the square brackets which are randomly selected
# for each reply.
#
# Currently, the plan is for this reply to only
# occur in response to comments made in the
# /r/test and /r/Screenwriting subreddits.
#
# The idea behind this is that _no-one_ really
# likes to have to write a logline. When learning
# how, it can appear daunting. Unfortunately, in
# certain domains, a lot can ride on these one
# or two sentence descriptions.
# However, the actual format is fairly simple.
# It's surprising how much our mind can interpolate
# random features and see how a movie could come
# about.
#
# Another possibility is a 'logline-to-synopsis'
# competition, where Reddit users can be publicly
# allocated a random logline and have to create a
# brief synopsis, based on their logline, within
# a given time-frame.
#
#
##################################################
# Created: 10 November 2016, Ra Inta
# Last modified: 20161120, R.I.
##################################################



import praw
import bot_cred
#import requests.packages.urllib3
#requests.packages.urllib3.disable_warnings()
import os
import re
import time
import logline

r = praw.Reddit(bot_cred.app_ua)
r.set_oauth_app_info(bot_cred.app_id, bot_cred.app_secret, bot_cred.app_uri)
#r.get_authorize_url("...","submit read identity", True)

############################################################
# Some really ugly copypasta for the moment ################
# Paste in auth code returned from parsing URL returned from above:
#authCode = "36KhaYQb5VdFWXHwoQiBL06Je8A"
#access_information = r.get_access_information(authCode)
## Refresh access_token (token lasts one hour)
#r.refresh_access_information(access_information['refresh_token'])
############################################################

## Refresh access_token (token lasts one hour)
r.refresh_access_information(bot_cred.refresh_token)

## Double-check we are us
#authenticated_user = r.get_me()
#print(authenticated_user.name, authenticated_user.link_karma)


# Check to see if text file has been created to
# keep track of people we've posted to
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

def replybot():
    """docstring for replybot"""
    subreddit = r.get_subreddit(bot_cred.app_subreddit)
    comments = subreddit.get_hot(limit=10)
    pass



subreddit = r.get_subreddit(bot_cred.app_subreddit)
submissions = subreddit.get_new(limit=20)

for submission in submissions:
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    for comment in flat_comments:
        if comment.id not in posts_replied_to and re.search("random logline", comment.body, re.IGNORECASE):
            # This should go before the comment; if something
            # fails here, then at least it won't spam the commenter
            posts_replied_to.append(comment.id)
            print "Submission: ", submission.title
            #print "Text: ", submission.selftext
            #print "ID: ", comment.link_id
            print "---------------------------------\n"
            print "Comment: ", comment.body
            print "---------------------------------\n"
            print "ID: ", comment.id
            print "---------------------------------\n"
            with open("posts_replied_to.txt", "w") as f:
                for post_id in posts_replied_to:
                    f.write(post_id + "\n")
            # Reply to the comment
            reply_body = logline.generate_logline()
            reply_boilerplate = "\n\n***\n"
            reply_boilerplate += """[](#footer)*^(I'm a bot, with very limited feelings.
                                Please downvote me if this was not the logline you were looking for.)
                                ^\([Info](/u/random_logline) ^/ ^[Feedback](/message/compose?to=/u/random_logline))*"""
            comment.reply( reply_body + reply_boilerplate )
            print "Random logline bot replying to : ", submission.title
            print "with : ", reply_body
            time.sleep(45)

## Here's something to try if we're getting rate limited:
## From https://www.reddit.com/r/redditdev/comments/1i7fma/been_messing_around_with_praw_but_ive_been/cb1s0g1/
#import praw, urllib2, time
#try:
#    praw.stuff()
#
#except praw.errors.RateLimitExceeded as RateLimit:
#     print("Ratelimit Exceeded.")
#     time.sleep(RateLimit.sleep_time)
#     stuff_again()
#
#except urllib2.HTTPError as error:
#    if error.getcode() == "403" :
#        print( "Banned from subreddit.")
#    else:
#        print(error.getcode())

### For making the bot resilient to Reddit dropping out
## Thanks to /u/peoplma
#
#import traceback
#import praw
#import time
#
#def main():
## your while True code goes here
#
#def secondary():
#    try:
#        while True:
#            main()
#    except:
#        traceback.print_exc()
#        print('Resuming in 30sec...')
#        time.sleep(30)
#while True:
#    secondary()
