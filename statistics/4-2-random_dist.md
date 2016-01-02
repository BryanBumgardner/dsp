[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> First, the code that will visualize this for me. 
```
t = [random.random() for _ in range(1000)]
cdf =  thinkstats2.Cdf(t)
thinkplot.Cdf(cdf)
thinkplot.Show()

```

>> Which gives me this:

<br>
![cdf](http://i.imgur.com/1xYarpg.png)<br>

>> So I discovered in the exercises that you can't use a PMF for these random numbers. All the numbers are really long and have the exact same probability, so it doesn't work for the kind of graph we want to chart. 
Luckily for us, a CDF should show us the answer. Before I plotted it, I thought the program would give us a perfect slope, because it's supposed to be perfectly random, right? 

