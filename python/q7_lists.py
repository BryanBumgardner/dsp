# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
#start!!
>>> def match_ends(words):
...     amt = 0
...     for word in words:
...             if len(word) > 1 and word[0] == word[-1]:
...                     amt += 1
...     return amt
... 
>>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
3


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
#start! This one was kind of hard.
>>> def front_x(words):
...     xlist = []
...     alist = []
...     for word in words:
...             if word.startswith('x'):
...                     xlist.append(word)
...             else:
...                     alist.append(word)
...     return sorted(xlist) + sorted(alist)
... 
>>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
['xaa', 'xzz', 'axx', 'bbb', 'ccc']


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
#start!
>>> def last(t):
...     return t[-1]
... 
>>> def sort_last(tuples):
...     return sorted(tuples, key=last)
... 
>>> sort_last([(1, 3), (3, 2), (2, 1)])
[(2, 1), (3, 2), (1, 3)]


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
#start! ooh la la
>>> def remove_adjacent(nums):
...     i = 1
...     while i < len(nums):
...             if nums[i] == nums[i-1]:
...                     nums.pop(i)
...                     i -= 1
...             i += 1
...     return nums
... 
>>> remove_adjacent([1, 2, 2, 3])
[1, 2, 3]

def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
#Start! standard merge algorithm, right?
def linear_merge(list1, list2):
...     result = []
...     i = j = 0
...     total = len(list1) + len(list2)
...     while len(result) != total:
...             if len(list1) == i:
...                     result += list2[j:]
...                     break
...             elif len(list2) == j:
...                     result += list1[i:]
...                     break
...             elif list1[i] < list2[j]:
...                     result.append(list1[i])
...                     i += 1
...             else:
...                     result.append(list2[j])
...                     j += 1
...     return result
... 
>>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
['aa', 'bb', 'cc', 'xx', 'zz']
