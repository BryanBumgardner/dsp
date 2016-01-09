[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> The code:
```

from __future__ import print_function
import sys
import numpy as np
import math
import first
import thinkplot
import thinkstats2
import nsfg



def ReadFemPreg(dct_file='2002FemPreg.dct',
		dat_file='2002FemPreg.dat.gz'):
	dct = thinkstats2.ReadStataDct(dct_file)
	df = dct.ReadFixedWidth(dat_file, compression='gzip')
	CleanFemPreg(df)
	return df
df = nsfg.ReadFemPreg()

#first, make a scatterplot. Set the limits for the axes, data sources, and labels. 
def Splot(heights, weights, alpha=1.0):
	thinkplot.Scatter(heights, weights, alpha=alpha)
	thinkplot.Config(xlabel='Height (cm)',
					ylabel='Weight (kg)',
					xlim=[10, 45],
					ylim=[0,15],
					legend=False)
# the author advises a hexbin as well, which makes sense after the first run. 
def HexBin(ages, weights, bins=None):
	thinkplot.HexBin(ages, weights, bins=bins)
	thinkplot.Config(xlabel='Age (years)',
					ylabel='Weight (lbs)',
					legend=False)
#because this is a big data set we need a better visualization to provide better insight.
def BinsPercents(df):
	bins = np.arange(10, 48, 3)
	# why is arrange spelled wrong? No idea but it is.
	indices = np.digitize(df.agepreg, bins)
	# computes the index of the bin that contains each value in df.agepreg
	groups = df.groupby(indices)
	# prepares us some GroupBy objects for iteration
	ages = [group.agepreg.mean() for i, group in groups][1:-1]
	# computes mean age 
	cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]
	# computes the CDF of total weight

	for percent in [75, 50, 25]:
		weights = [cdf.Percentile(percent) for cdf in cdfs]
		label = '%dth' % percent
		# cool labels
		thinkplot.Plot(ages, weights, label=label)
		# Now finally we plot percentiles of age versus weight
	thinkplot.Show(xlabel="mother's age (years)",
		ylabel='birthweight (lbs)')
	
#now, the actual script:
def Plot(script):
	thinkstats2.RandomSeed(17)
	live, firsts, others = first.MakeFrames()
	live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
	BinsPercents(live)
	#this removes the miscarriages. Sad but necessary. Also brings in our Bins from earlier.
	ages = live.agepreg
	weights = live.totalwgt_lb
	#grabs the data
	scatterplot(ages, weights, alpha=0.1)
	thinkplot.Show(legend=False,
					formats=['jpg'])

live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
BinsPercents(live)
	#this removes the miscarriages. Sad but necessary. Also brings in our Bins from earlier.
ages = live.agepreg
weights = live.totalwgt_lb

print('thinkstats2 Corr', thinkstats2.Corr(ages, weights))
print('thinkstats2 Spearman', thinkstats2.SpearmanCorr(ages, weights))
	# put the function right inside the print for brevity. 
#Somehow I can't figure out how to print the damn thing from inside the function so here it's outside. 

Plot(df)
```
Which gives me this output:
<a href="http://i.imgur.com/mwglE9x.jpg"><img src="http://i.imgur.com/mwglE9x.jpg" style="width: 100px;" target="_blank"></a>
And also this:
```
Bryans-MacBook-Pro:Code bryanbumgardner$ python c7.py
thinkstats2 Corr 0.0688339703541
thinkstats2 Spearman 0.0946100410966
```
The results are as thus:
- Glancing at the charts show a small but existing relationship between all three percentiles between the ages of 15 and 20. The small humps that follow are staggered, so there may be further things to explore here, at least from just looking at the plots. The relationship is weak but it's there, because the 3 lines look similar. It appears to be non-linear after the age of 20.
- Pearson's Correlation rounds up to .07, Spearman's rounds to .09. Because they aren't the same, it suggests there's a small relationship. 
