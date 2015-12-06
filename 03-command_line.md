# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > I have a little experience with command line stuff. New things:

1. pushd: saves your spot in a directory temporarily and snaps you to a new directory. 

2. popd: returns you to the saved spot from pushd. These are fast ways to move between directories for quick actions, when used together. 
3. touch: creates new empty files. Does this work with more than just .txt files? More research is needed. 
4. mv: rename files. Didn't know you could do this.
5. | (pipes): Takes the output from the command on the left of the pipe and "pipes" it to the command on the right. 
6. cat: shows you the contents of the file without opening a second window. Could prove problematic if you try this on a .jpg. 
7. rm: removes (deletes) a file. Beware your spelling - no undo if you mess up, I think. 
8 * (wildcard): applies your command to files that match whatever isn't covered by the asterisk. Good for operating on large amounts of similar files. 
9. find: helps you find specific files. You can pair this with wildcards to find a whole bunch of stuff. 
10. grep: wow. This you can use to replace entire words and sentences in files. 

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > ls lists all contents of your working directory. 

Adding "-a" won't hide directories and files that start with "." (Usually these are hidden as admin files, I think.) 'ls -l' returns the contents in a long form, which shows you names, dates, locations and some other information rather than just the name of each piece of content. Adding the 'h' (human) makes things print in a human readable format. For example, the 'ls -l' command returns a handful of directories for me, full of random numbers. If I use 'ls -lh' instead the numbers come back with descriptions so I can understand what the heck they are. 

---


---

What does `xargs` do? Give an example of how to use it.

> > xargs helps you build and execute commands from standard input, usually a combination the terminal can't handle. 

This is exceptionally useful for finding certain types of files and applying actions to them, usually delete or maybe rename. One example:

find /stuff -name picture -type f -print | xargs /bin/rm -f

This will find any files in /stuff or below with the name 'picture' and deletes them. If I wanted to delete multiple things, I'd have to use wildcards to make sure I capture them all. I couldn't do this without xargs, as I'm using the pipe to pass the output of the find command as the input to the xargs command. At least I think that's how this works.

---

