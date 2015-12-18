# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples and lists are both sequences, but they differ in a few ways. You can't modify tuples, which means they are 'immutable,' to use Python terminology. The information inside them can't be changed or updated, so you have to write around them to get what you want. They also use parentheses where lists use brackets. Lists on the other hand are easily changed and broken down collections of objects in a specified order. 

>> You can't use lists as dictionary keys. In short, to keep Python dictionaries efficient, certain hash functions are used to explore objects. Lists, by their nature, clash against the specific algorithms used by dictionaries to assign values to keys. They are containers and don't hash appropriately, which means you could have tons of problems. You might search two copies of the same list and get returns that shows two completely different answers are equivalent. Even if you hash lists by their ids, you'll always get errors like that or a direct KeyError if you used a list literal.

>> Tuples work as keys in dictionaries because their contents are immutable and can be hashed without concerns of modification. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists keep things in order, where sets do not. Sets forbid duplicates, where lists do not. If you try to check for a value in a huge list data set, it would be majorly problematic. Sets are much easier to check membership, if you have hashable items in it. Because sets are immutable, they save memory by not allowing changes, which makes searching them faster to process. Granted, you might have to make decisions based on the limitations of the first sentence. 

>> Lists are the simplest sequences, I think. They can be combinations of whatever. 
>> An example: 
'''
list1 = ['apple', 'orange', 'pear', 'banana'];
'''

>>Sets, on the other hand, break whatever you put into them into specific objects. See how this example breaks up the letters and doesn't recognize them together. I assign set to x

>>x = 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

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





