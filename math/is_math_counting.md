# Is Math Counting?

One of the very first mathematical concepts that people learn is how to count. Being able to count to ten, on your fingers for example, is so easy a child can do it.

I have a confession: Once, in undergrad, I had to take a test on counting. And I failed.

Before I go into this story, let's step back for a moment, and talk about counting overall.

## What is Counting

Let's start simple. Suppose you take a walk and find a bunch of stones on the ground that are white, black and grey that look like this:

<!-- image of stones -->

How could we count the stones?

## Ordinal vs Cardinal

One way we can think of counting these stones is by comparing different stones. We notice that there is only a single black stone (near the centre) and there are multiple white stones and multiple grey stones. We also see that there are more grey stones than white stones or, put another way, there are the most grey stones. Effectively, this kind of counting ranks or orders the amount of each stone, so we can write a statement such as

```
black stones < white stones < grey stones
```
 where `<` is the usual less-than comparison symbol. This is an _ordinal_ numbering of stones. I'll note that this approach doesn't tell us the total number of stones.

 Another way we can think of counting these stones is to assign a value to each amount of each kind of stone. Let's start with the grey stones. We can count |||| stones, with each | representing a single stone and we can call this amount "four". We repeat the process for white stones and find ||| white stones and we can call this amount "three". Finally, there is | stone, and we can call this value "one". Assigning a specific value to each amount is called a _cardinal_ numbering of the stones. 

 Assigning values and names to the amount of each stones does allow us to count the total, which is |||| ||| | or "eight" stones. We can figure this out without doing any calculation or arithmetic, which is notable. This cardinal approach we can count both the total number of stones and subsets of stones by colour. 

## Using Number Systems

Using | or some other symbol to denote a single item in a group and then repeating that symbol for multiple items is helpful if you want to count distinct groupings or get a total. It can become inconvenient writing out the same symbol many many times. In fact, many societies have come up with all kinds of symbolic systems for counting. The ancient Babylonians used a number [system based on groups of sixty](https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_numerals/), which is practical for accounting and commerce since sixty can be neatly divided in half, in thirds, and so on. The Mayans had a [system based on groups of twenty](https://en.wikipedia.org/wiki/Maya_numerals), which is practical because most humans that many fingers and toes. In these and other cases, the core concept of choosing a number system is to have a ways to group or write down certain quantities in a systemic fashion. The main goal of counting is to align ways of writing down and communicating quantities in ways everyone in a society can understand. 

## Counting Without Numbers
You may have noticed that I took some pains to avoid using commons numbers, putting numbers into quotes and using symbols instead of digits. This is because there is a distinction to be made between counting and numbers. Having a system for counting does not necessarily need numbers, and numbers do not need to be used to "count" things. A clear example of counting without numbers is from the civilization of the Inca who had devices for counting even though they did not have a number system or even a written form of communication. These devices were known as [quipus](https://www.peruforless.com/blog/quipu/), which were groups of strings with knots added to keep track of quantities in agriculture, population censuses, and so on. An individual skilled with the quipu could quickly count a number given an inquiry. This was possible even without a number system.


## Counting Without Counting
We could also make the decision of whether there is one stone, or more than one stone. On the left side, there is a single white stone that is apparently separated from the others. On the right side, there is more than a single stone. So we could count them as "one" or "single" stone. Some cultures count this way, including [indigenous cultures in places such as Australia](https://www.sydney.edu.au/news-opinion/news/2017/02/01/explainer--how-does-the-aboriginal-numeric-system-work-.html). These cultures have expressions for "one", "two" or "many" along with number systems that are not written down nor expressed using objects such as quipus. Instead of writing systems or devices, such cultures have expressions for amounts that are communicated by body language and may be highly contextual. Again, counting and number systems are not the same thing.

## Getting Past Small Numbers

In the scenarios above, the amount of stones we find is a small number; we could hold them in our hands if we wanted to. This makes counting (and related reasoning) about these stones fairly easy. 

What about when the number of stones gets large? Suppose we look at a rocky beach, with potentially thousands, millions or more stones. Can we count items of this size? What if we only wanted to count dark-coloured stones in this case?

The answer is: yes.

In mathematics, the term _enumeration_ is used to mean counting, often a higher level. We might want to enumerate the number of items in a set, for example, or number of points that satisfy some relationship. There is a whole branch of mathematics called [_combinatorics_](https://en.wikipedia.org/wiki/Combinatorics) that explores enumeration and counting in general.

Some problems in combinatorics are relatively easy to understand. For example, _permutations_ and _combinations_ are concepts that are often taught at the high school level. A permutation is an _ordered_ counting of items in a set, while combinations are countings of an _unordered_ set. For example, suppose I wanted to arrange three of the stones above in a particular order, such as black, grey and white. I may be interested to know how many ways I can do this (the answer is six) or I may be interested in how many ways I can pick two stones that are different colours if I choose some at random (I leave this as an exercise to the reader). 

In the first case, I look at permutations of stones; if I have three stones, each of a different colour, I can ennumerate the possible orderings directly:

```
black, white, grey
black, grey, white
white, grey, black
white, black, grey
grey, white, black
grey, black, white
```
showing there are six distinct possibilities. 

In the second case, I look at the combinations or unordered selections; as a hint for determining the number, list all the ordered pairs and then remove duplicates that are the same total number of stones. For example,

```
white, grey
```

and 

```
grey, white
```

are the same _set_ because the contain the same elements, even if the are different _ordered pairs_.

Based on permutations and combinations, counting items seems straightforward. List out the possibilities, then count them using normal counting numbers. So why is combinatorics a whole branch of mathematics (and in turn, why are there entire [university departments](https://uwaterloo.ca/combinatorics-and-optimization/) and [professors](https://www3.nd.edu/~dgalvin1/) dedicated to studying it?)

## Thinking Big

Listing out the possibilities of a counting problem, like some illustrated above is straightforward mostly because the numbers are not large. When you can keep track of the total number of elements or stones using fingers on one hand, or two hands, or even a few more, it is easy to count. What happens when the numbers or elements of a set are large, or even really, really large?

To think of this, suppose I have stones in several colours. As we've seen if I have stones in three colours (black, white, grey) I get six possibilities of orderings. If I add blue stones, I will now have 24 possibilities. If I add green, I have 120 possibilities, and in general if I have _n_ colours of stones, I will have _n!_ orderings (read as "n factorial"), where 

```
n! = n * (n-1) * (n-2) * ... * 2 * 1
```

meaning I multiply the number each integer from 1 to _n_ to get _n!_. In terms of the coloured stones, _3! = 3*2*1 = 6_, _4! = 4*3*2*1 = 24_, and so on. 

While this all appears neat and tidy, in practice factorials grow _very_ quickly. Most pocket calculators that can calculate factorials, but usually error with factorials larger than _12!_, with more powerful graphing calculators getting up to _20!_. Eventually, the number of digits in a factorial calculation becomes large, and in turn even _managing_ how to calculate and store such numbers becomes tricky, let alone actually computing the number itself. This phenomenon is known as [combinatorial explosion](https://en.wikipedia.org/wiki/Combinatorial_explosion) is a known problem in both mathematics and computer science. Certain problems are incredibly difficult to solve in combinatorics simply because the numbers are _so large_. For example, writing down a number with a [100 digits](https://en.wikipedia.org/wiki/Googol) is one thing, but perfuming calculations with it is a totally different thing. In fact, standard programming language representations of 64-bit integers reach a maximum at around 9 quintillion, which is a 9 followed by 18 zeros. A google is over five times larger than this.

In short, there are a lot of really, really big numbers. 

In terms of applications, large numbers appear often in counting problems. One famous example from mathematics is [Ramsey Theory](https://en.wikipedia.org/wiki/Ramsey's_theorem) which counts the number of possible [subgraphs of a graph](https://www.sfu.ca/~vjungic/RamseyNotes/Friends.html). There are other applications and problems, including representing large numbers in a way that is practical, which arises in computational problems from encryption to scientific simulation. 

## Counting is Hard

And this brings us to my experience with counting in undergrad. The quiz I took was on permutations, combinations and related topics. 

In conclusion, I failed counting (but it was the hard kind of counting)



