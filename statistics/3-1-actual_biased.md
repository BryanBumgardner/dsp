[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> The code, which is explained in the markdown. I just wrote a program to do this. I followed his example but explained each and every line when it wasn't redundant. 

```
from __future__ import print_function

import math
import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot
import chap01soln
resp = chap01soln.ReadFemResp()
 
pmf = thinkstats2.Pmf(resp.numkdhh)
# thinks makes a PMF of numkdhh, which is the children over 18. resp is needed
# because we aren't manually entering numbers, we're calling them

thinkplot.Pmf(pmf, label='numkdhh')
thinkplot.Show()
#this shows the plot of our PMF for the first time. Test as you go, 

def BiasPMF(pmf, label=''):
	# if we're gonna get the bias we have to oversample.
	new_pmf = pmf.Copy(label=label)
	# this line copies our old Pmf we already had. 
	for x, p in pmf.Items():
		new_pmf.Mult(x, x)
		# this for statement and handy Mult function multiplies the number
		# of children in each household by how many children in each household 
		# can actually observe that number, which is the equivalent of only surveying them. Science! 
	new_pmf.Normalize()
	# honestly, I don't know what this does. I looked it up and I'm still confused.
	# ¯\_(ツ)_/¯
	return new_pmf
	# spits out the new pmf. 

biased = BiasPMF(pmf, label='biased')
# make the biased pmf from the BiasPMF function

thinkplot.PrePlot(2)
# I don't really understand this part here. Is this telling it I'm about to
# plot two things? 'PrePlot' suggests as much.
thinkplot.Pmfs([pmf, biased])
# this makes sense - plot both pmf and my new one, biased
thinkplot.Show()

pmf.Mean()
biased.Mean()
# get the means of both the pmfs with a function. 
```

