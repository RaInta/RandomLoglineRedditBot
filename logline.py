#!/usr/bin/python

# Logline
# This takes a general syntactic form for a movie logline and random entries from lists of (hopefully) appropriate adjectives, adverbs etc.
# to generate an almost unique logline.
#
# Created: 12 Dec. 2014, Ra Inta
# Last modified: 20141212, R.I.

import random

# Syntax: A(n) {PROTAG_DESCRIPTOR} {PROTAG} must {GOAL} or {STAKE}. (S)He does this by {VISUAL_MEANS} and {DISCOVERY_PREFIX, DISCOVERY}.


discoveryPrefixList = open('DISCOVERY_PREFIX.txt').read().splitlines()
discoveryList = open('DISCOVERY.txt').read().splitlines()
goalList = open('GOAL.txt').read().splitlines()
protagDescriptorList = open('PROTAG_DESCRIPTOR.txt').read().splitlines()
protagList = open('PROTAG.txt').read().splitlines()
stakeList = open('STAKE.txt').read().splitlines()
visualMeansList = open('VISUAL_MEANS.txt').read().splitlines()


def getRNDList(inputList):
   return random.choice(inputList)

def generate_logline():
    """docstring for generate_logline"""
    protagDescriptor = getRNDList(protagDescriptorList)
    protagField = getRNDList(protagList)
    beginning = 'A'
    for vowel in 'aeiou':
       if vowel == protagDescriptor[0].lower():
          beginning += 'n'
    [protag, sex] = protagField.split(',')
    sex = sex.split()
    if sex == ['e']:
       sex = random.choice(['f', 'm'])
    if sex == ['f']:
       pronounCap = 'She'
       pronoun = 'she'
       possessive = 'her'
       objective = 'her'
    else:
       pronounCap = 'He'
       pronoun = 'he'
       possessive = 'his'
       objective = 'him'
    discovery = getRNDList(discoveryList)
    goal = getRNDList(goalList)
    stake = getRNDList(stakeList)
    visualMeans = getRNDList(visualMeansList)
    goal = goal.replace(' their ', ' ' + possessive + ' ')
    stake = stake.replace('their ', possessive + ' ')
    discovery = discovery.replace(' their ', ' ' + possessive + ' ')
    visualMeans = visualMeans.replace(' their ', ' ' + possessive + ' ')
    goal = goal.replace(' them', ' ' + objective + ' ')
    stake = stake.replace(' them', ' ' + objective + ' ')
    discovery = discovery.replace(' them', ' ' + objective + ' ')
    visualMeans = visualMeans.replace(' them', ' ' + objective + ' ')
    stake = stake.replace('they ',  pronoun + ' ')
    return beginning + " " + protagDescriptor + " " +  protag +  " must " +  goal +  ", or " +  stake + ". " + pronounCap + " does this by " + visualMeans + " and " +  discovery + "."
