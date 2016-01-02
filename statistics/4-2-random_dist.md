[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> First, the code that will visualize this for me. 
```
t = [random.random() for _ in range(1000)]
cdf =  thinkstats2.Cdf(t)
thinkplot.Cdf(cdf)
thinkplot.Show()
```

>>Which gives me this:

<a href="http://imgur.com/1xYarpg"><img src="http://i.imgur.com/1xYarpg.png" style="width: 100px;" target="_blank"></a>

So I discovered in the exercises that you can't use a PMF for these random numbers. All the numbers are really long and have the exact same probability, so it doesn't work for the kind of graph we want to chart. 
Luckily for us, a CDF should show us the answer. Before I plotted it, I thought the program would give us a perfect slope, because it's supposed to be perfectly random, right? 
As it turns out, the numbers aren't. The slope stays pretty close to one, but there's lots of dips and humps. I looked further into the issue and discovered things like [The Birthday Problem](https://en.wikipedia.org/wiki/Birthday_problem) and the [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister). Python uses Mersenne as the built-in Pseudo Random Number Generator or PRNG. I think ThinkStats2 uses the same.
As I discovered, you really can't make a perfectly random number generator using algorithms. People have gotten close - Mersenne Twister is the current favorite - but it's not wise to count on these things as perfect. Digital artifacts come out that show these aren't perfectly random, which we can see in the chart above. I can't understand the math, but I can understand what mathematician and physicist [John von Neumann said about PRNGs](https://en.wikipedia.org/wiki/John_von_Neumann): "Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin."

