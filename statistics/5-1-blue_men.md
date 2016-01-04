[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> Code:
```
import scipy.stats
# here's the mean and standard deviation of heights for men in cm
mu = 178 # thank you documentation for making life easy 
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
# grabs us some CDF and basic math shows the percentage
low = dist.cdf(177.8) #that's our target height in cm
high = dist.cdf(185.4)
print(low)
print(high)
print(high-low)
```
Output:
```
Bryans-MacBook-Pro:Code bryanbumgardner$ python Chap5.py
0.489639027865
0.831733710811
0.342094682946
```
So, knowing that these numbers should be percentages, 34.2 percent of the male U.S. population is lucky enough to try out for Blue Man Group. Basically, what we did here was build a distribution of heights. We made the "chart" using the known mu and sigma, then we ran some heights through it to determine percentages of the whole. While I can figure out how many of the people will qualify, I can't figure out just yet how to do the optional answers for this section. Maybe more forthcoming before the camp starts. 
