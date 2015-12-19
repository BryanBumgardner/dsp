# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?


>> I was a writer first and a programmer second, so through the rest of these answers I'm going to try and explain things simply and without too much technical jargon unless necessary - that's how I can understand it myself. If I need to be more technical let me know, I'm still a beginner with Python. 

>> Tuples and lists are both sequences, but they differ in a few ways. You can't modify tuples, which means they are 'immutable.' The information inside them can't be changed or updated. They also use parentheses where lists use brackets. Lists on the other hand are easily changed and broken down collections of objects in a specified order. 

>> You can't use lists as dictionary keys. In short, to keep Python dictionaries efficient, certain hash functions are used to explore objects. Lists, by their nature, clash against the specific algorithms used by dictionaries to assign values to keys. They are containers and don't hash appropriately, which means you could have tons of problems. You might search two copies of the same list and get returns that shows two completely different answers are equivalent. Even if you hash lists by their ids, you'll always get errors like that or a direct KeyError if you used a list literal.

>> Tuples work as keys in dictionaries because their contents are immutable and can be hashed without concerns of modification. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists keep things in order, where sets do not. Sets forbid duplicates, where lists do not. If you try to check for a value in a huge list data set, it would be majorly problematic. Sets are much easier to check membership, if you have hashable items in it. Because sets are immutable, they save memory by not allowing changes, which makes searching them faster to process. Granted, you might have to make decisions based on the limitations of the first sentence. 

>> Lists are the simplest sequences, I think. They can be combinations of whatever. Sets can only contain immutable elements.
>> An example: 
```
list1 = ['apple', 'orange', 'pear', 'banana'];
```

>>Sets, on the other hand, break whatever you put into them into specific objects. See how this example breaks up the characters and doesn't recognize them together. I assign `(Hello, World)` to set `x`. Then when I call `x`, what I get is a list of the characters unconnected, illustrating what sets do. Notice how there aren't any duplicates of L or O?

```
x = set(Hello, World)
x 
{',', 'W', 'o', 'd', 'l', 'H', 'e', ' ', 'r'}
```

>>>Hello, World!  

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `Lambda` is a cheap and easy way to make one-off functions. Functions exist to remove redundancy in code, which partially is an effort to keep code simple. `Lambda` works off the same principle, allowing us to create a one-line function that we'll only use once. They are anonymous, and the body itself is limited. `Lambda` can only take one expression. 

>> Technically we could live without it, but `lambda` helps us keep things simple in specific situations. Here's a basic example of two functions that do the same thing, but are simplified with `lambda`. 
```
>>> def f(x):
...     return x*2
... 
>>> f(2)
4
```
>> So many lines for such a simple thing. How about this:
```
>>> r = lambda x: x*2
>>> r(3)
6
```
>> No variable? No problem! `lambda` doesn't technically require one. Thusly, the beauty of a one-line function. Still, some people don't like `lambda` because it's too simple and too limiting. 
```
>>> (lambda x: x*2)(5)
10
```
>> Now, to use in the `key` for a `sorted` argument, complex record keeping in the Mystery Machine:
```
>>> mystery_tuples = [
...     ('a', '2', 'Velma'),
...     ('b', '1', 'Shaggy'),
...     ('c', '3', 'Scooby'),
...     ('d', '4', 'Daphne'),
...     ('e', '5', 'Fred')
... ]
>>> sorted(mystery_tuples, key= lambda mystery: mystery[2])
[('d', '4', 'Daphne'), ('e', '5', 'Fred'), ('c', '3', 'Scooby'), ('b', '1', 'Shaggy'), ('a', '2', 'Velma')]
```
>>In this case I sorted them by the first letter of the final part of the tuple, where their names are entered. 



---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are short ways of making lists. This is useful when you're making a list that's a result of some operation applied to another sequence, for example. List comprehensions can basically substitute for `lambda`, `map`, `filter` and `reduce` in a way that's easier for mathematicians to read, if you're into that sort of thing. Some of these rules and syntax changed in Python 3.
```
# a quick list of squares, as a list comprehension
>>> squaredn = [x ** 2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
>>That same list, using `map`. 
```
>> squaredn = list(map(lambda x: x**2, range(10)))
>> squaredn
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
``` 
>> Or maybe you prefer `filter`? I can't even figure out how to get those numbers using just `filter` without writing something totally unreadable. This filter shows us all the answers when `x` is less than 5, from our original range of 10.
```
list(map(lambda x: x ** 2, filter(lambda x: x < 5, range(10))))
[0, 1, 4, 9, 16]
```
>> We can do set comprehensions too. This `set` will show me all the characters in `'scooby'` if they aren't duplicated in the string `'doo'`. Much science, very Python. 
```
>>> set = {x for x in 'scooby' if x not in 'doo'}
>>> set
{'b', 's', 'c', 'y'}
```
>> Dictionary comprehensions are easy to do as well. Overall, comprehensions are much easier to read, even if they are limited in complexity. 
```
>>> {x: x+' doo' for x in ('doobie', 'Scooby')}
{'doobie': 'doobie doo', 'Scooby': 'Scooby doo'}
# by the end of this class we'll be singing the entire theme song with Python
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





