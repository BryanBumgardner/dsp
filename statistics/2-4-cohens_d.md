[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>First of all, the code:

```
live, firsts, others = first.MakeFrames()
  # the solution code is broken. If you don't define this outside of 
  # the testing variable, it won't print for you. 
hist = thinkstats2.Hist(live.prglngth)

  # to explore the ages we must make a function
def babyCohenD(live, firsts, others):
	# these names are the dataframes
	# live = df of all live births
	# firsts = df of first borns
	# others = df of all other babies beside firsts

	meanlive = live.totalwgt_lb.mean()
	meanfirsts = firsts.totalwgt_lb.mean()
	meanothers = others.totalwgt_lb.mean()
	# these built in functions will calculate the means
	# for these values, which is our first step. 

	var1 = firsts.totalwgt_lb.var()
	var2 = others.totalwgt_lb.var()
	# these will calculate variance for our values

	# I liked his very clear print options so I'm using them.
	print('Mean')
	print('First babies', meanlive)
	print('Others', meanothers)
	# These display the basic means. It's always good to show your work,
	# even when it's done by Python 

	print('Variance')
	print('First babies', var1)
	print('Others', var2)
	# This prints the calculated variance from above. 

	print('Difference in pounds:', meanfirsts - meanothers)
	print('Difference in ounces:', (meanfirsts - meanothers) * 16)
	# because there's 16 ounces in a pound

	# here's where his solution strays from the explanation put in the book. 
	print('Difference relative to mean (age points)',
			(meanfirsts - meanothers) / meanlive * 100)
	# This will show the relative difference between the two. 

	d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
	print('Cohen D:', d)
	# calculate!!
```
>>Okay, here is the output:

```
chap02ex4ans.py: All tests passed.
Mean
First babies 7.265628457623368
Others 7.325855614973262
Variance
First babies 2.0180273009157768
Others 1.9437810258964572
Difference in pounds: -0.12476118453549034
Difference in ounces: -1.9961789525678455
Difference relative to mean (age points) -1.7171423678372415
Cohen D: -0.088672927072602
```

>> So looking at this, we got a pretty tiny Cohen's D. (resisting inappropriate joke...)
>> Okay seriously: The Cohen's D is .089 standard deviations, which isn't even a whole one. This means it's statistically insignificant. Yes, it's true there's a difference of almost two ounces between the Firsts and Others, but if you look at the Variance, that difference isn't a big deal inside the groups themselves. 
>>In this case, our hypothesis (and widespread urban myth) is wrong. This mirrors our findings about pregnancy length we figured out earlier in the exercise. So much for Grandma's wisdom.
