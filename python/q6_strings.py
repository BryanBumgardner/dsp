# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    """
 
    # start!
def donuts(count):
... 	if count < 10:
... 		numberofdonuts = count
... 	else:
... 		numberofdonuts = 'many'
... 	return 'Number of donuts: ' + str(numberofdonuts)
... 
>>> donuts(4)
'Number of donuts: 4'


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
#start!
def both_ends(s):
... 	if len(s) < 2:
... 		return ''
... 	return s[0:2] + s[-2:]
... 
>>> both_ends('spring')
'spng'


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
#start!
def fix_start(s):
... 	char = s[0]
... 	length = len(s)
... 	s = s.replace(char, '*')
... 	s = char + s[1:]
... 	return s
... 
>>> fix_start('aardvark')
'a*rdv*rk'

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
#start!
>>> def mix_up(a, b):
...     swap_a = b[:2] + a[2:]
...     swap_b = a[:2] + b[2:]
...     return swap_a + ' ' + swap_b
... 
>>> mix_up('mix', 'pod')
'pox mid'


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
#start!!!
>>> def verbing(s):
...     length = len(s)
...     if length > 2:
...             if s[-3:] == 'ing':
...                     s += 'ly'
...             else:
...                     s += 'ing'
...     return s
... 
>>> verbing('hail')
'hailing'


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
 #start!
 >>> def not_bad(s):
...     ynot = s.find('not')
...     ybad = s.find('bad')
...     if ybad > ynot:
...             s = s.replace(s[ynot:(ybad+3)], 'good')
...     return s
... 
>>> not_bad('This dinner is not that bad!')
'This dinner is good!'
#whatever you say, computer

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
#start!
>>> def front_back(a, b):
...     alength = len(a)
...     blength = len(b)
...     if alength % 2 == 0:
...             aindex = alength //2
...     else:
...             aindex = (alength //2) + 1
...     if blength % 2 == 0:
...             bindex = blength //2
...     else:
...             bindex = (blength //2) + 1
...     afront = a[0:aindex]
...     aback = a[aindex:]
...     bfront = b[0:bindex]
...     bback = b[bindex:]
...     return afront + bfront + aback + bback
... 
>>> front_back('abcd', 'xy')
'abxcdy'
#woohoo!
