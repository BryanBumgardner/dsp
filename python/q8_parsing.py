#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

# it's PANDAS TIME!
# http://imgur.com/gallery/CVJw1

import pandas as pd

def smallest_gap(fname, col1, col2, result_col):
    data = pd.read_csv(fname)
    diff = abs(data[col1] - data[col2]) #you gotta put abs in here to get the number closest to zero
    smallest = data[diff == diff.min()]
    return smallest[result_col].values[0]

team = smallest_gap('football.csv', 'Goals', 'Goals Allowed', 'Team')
print (team)

Bryan:anaconda bryanbumgardner$ python parse_csv.py 
Aston_Villa
