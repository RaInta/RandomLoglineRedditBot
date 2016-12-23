# Random Logline Reddit Bot
Generates a randomly generated movie logline in response to a post containing the text "random logline" on Reddit 

---

> An incompetent forensic entomologist must travel to a remote village of cannibals, or his best friends will divorce. He does this by genetically modifying the common cold and discovers that a straw will show which way the wind blows.

No doubt you've seen plenty of movie loglines. You know, the short (TV-guide) description of what the movie is about. These few sentences can make the difference between a box-office success or a complete bomb. Also, a good logline can be a valuable tool for a screenwriter to convince a prospective producer to invest a large amount of money in their movie concept.

Yet, surprisingly often, coming up with a short two or three sentence description can be deceptively difficult. Enter the random logline bot! The logline at the beginning is an example picked from running the [code in this repository](logline.py). OK, it's probably not something you'd run out and watch or enter in your annual Oscar betting pool. But you can hopefully _see_ it resembles what a movie ought to be. 

### How does it work?


~~The main engine is a thinly sliced NLP based on a Markov Chain Monte Carlo sampling scheme that parses the Twitter API~~
The structure is actually quite simple. A good (traditional, Hollywood) logline has a number of constraints. Of course, a logline has to be brief (we're all busy and have ever-atrophying attention spans). But it also has to be _about_ some character: the _protagonist_. But you're not just going to watch some dude driving around aimlessly in a car for ninety minutes (OK, [maybe Tom Hardy could carry it off](http://www.imdb.com/title/tt2692904/) ). Your protagonist needs some sort of _goal_. And, to be interesting--to have a point--there needs to be some sort of _stake_ involved, if the protagonist fails to achieve that goal -- implying there's an obstacle to that goal.

We could stop there and that would suffice for many loglines. Some so-called logline experts opine that the perfect loglines are exactly 27 words long.

However, we want what is sometimes referred to as a 'working logline'. Something that additionally shows off the cool 'fun and games' in the second act, the _visual means_. This can then be topped off with the cream of what we all learned, i.e. the _theme_.

Finally, to add some extra spice, we can add a totally awesome _adjective_ to describe our protagonist, just to make the whole thing pop. Because, frankly, we rely heavily on stereotypes for characters. Anything that delineates our particular cop procedural drama from the countless others is beneficial. 

So the structure looks like:

> An _adjective_ _protagonist_ must _goal_ or _stakes_. She does this by _visual means_ and learns _theme_.

### Final note

Hopefully you can see that, with the appropriate constraints, our mind can create fairly vivid interpolations of otherwise random drivel. The logline is a useful structure to convey the essence of a movie.

One vital ingredient, amongst many, that is missing in this scheme is the element of irony. The best loglines are deliciously ironic. For example, [_Liar, Liar_ (1997) ](http://www.imdb.com/title/tt0119528/?ref_=fn_al_tt_1): "A lawyer must win the biggest hearing of his career -- but is magically prevented from lying".

Below are another nine I selected from a sample of fifty random loglines. Obviously they aren't all winners. But you get the idea...

---

> A terminally ill air traffic controller must attain single-digit body fat percentage, or he will be evicted. He does this by falling into a trance and discovers that beauty, unaccompanied by virtue, is as a flower without perfume.

> A self-assured disc jockey must raise and train a reluctant service dog, or William Shatner will go to prison for a crime he didn't commit. He does this by forming a band of shady, but liberty-obsessed outlaws and learns that failure teaches you more than success.

> A decrepit meter maid must break out of a mental asylum, or she will lose all memory of faces. She does this by souping up a bitchin' Camaro and learns that a fool says what he knows, and a wise man knows what he says.

> A vegan waterslide tester must solve a horrific murder, or his school will burn down, killing all of his friends. He does this by assembling a bad-ass team of motherfuckers and discovers that if wishes were horses, beggars would ride.

> A smart pan-handler must battle the Dalai Lama, or he will lose his freaking mind. Literally. He does this by creating an army and learns to not make a mountain out of a mole-hill.

> A visionary taxi driver must win at FaceBook, or his mother will die from cancer. He does this by enlisting the help a group of girls from a halfway house and learns that excuses are only for those people who are unwilling to find the solution.

> A decrepit watch maker must fight a horde of ninjas, or Flipper will come back as a zombie. He does this by creating a psychopathic, but omniscient, android and learns that he who digs a hole for someone, will fall in it himself.

> A smart car saleswoman must retrace her steps from a three day party at a famous designer-drug manufacturer's, or she will become an experiment for torture devices. She does this by cornering the market on Nerf guns and discovers that no man is an island.

> A passionate embalmer must eradicate a vicious gang of horse thieves, or all bird-life will become extinct. He does this by summoning ethereal beings possessing psychokinetic powers and discovers that the smoothest way is full of stones.
