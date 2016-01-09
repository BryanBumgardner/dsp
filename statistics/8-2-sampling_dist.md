[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> The code:

```
from __future__ import print_function

import thinkstats2
import thinkplot
import math
import random
import numpy as np
from scipy import stats
from estimation import RMSE, MeanError


def Estimate(lam=2, n=10, m=1000):
	#sets distribution, sample size and iterations
	def TheLine(x, y=1):
		thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)
	estimates = []
	for j in range(m):
		xs = np.random.exponential(1.0/lam, n)
		lamhat = 1.0 / np.mean(xs)
		estimates.append(lamhat)
	stderr = RMSE(estimates, lam)
	print('standard error:', stderr)
	#make a cdf and a confidence interval
	cdf = thinkstats2.Cdf(estimates)
	ci = cdf.Percentile(5), cdf.Percentile(95)
	print('Confidence interval:', ci)
	TheLine(ci[0])
	TheLine(ci[1])

	#cdf plotting
	thinkplot.Cdf(cdf)
	thinkplot.Show(xlabel='estimate',
					ylabel='CDF',
					title='Sampling distribution')
	return stderr

Estimate(lam=2, n=10, m=1000)
```

The result for sample sizes:
- n=10: Standard Error: 0.79 CI: 1.3, 3.6
- n=100: Standard Error: .2 CI: 1.7, 2.4
- n=1000: Standard Error: .05 CI: 1.9, 2.1

As you can see, as the samples increase the Standard Error and the width of the confidence intervals get smaller. This is statistics, people! 
