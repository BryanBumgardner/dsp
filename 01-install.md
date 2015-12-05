# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

---

Did you install Python 2 or 3? Why? How can you check the version of Python installed if you happen to be on an unfamiliar computer?

>> I installed 3, after doing some research. 3 is easier to learn, but as I've discovered, there's a handful of backwards compatibility issues that may require me to use 2. Still, it seems like the Python communities are trying to move up to 3 so I'll deal with compatability problems when I get to them. If I have problems with libraries, I'll learn to port them to 3 myself. Learning experience! There's a variety of different commands I can run to check the version. One option: "--version"

---


### Homebrew

If you use a Mac, install [Homebrew](http://brew.sh/) if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.
