import pandas as pd

from pandas import DataFrame, read_csv
#where is your file? here!
path = '/Users/bryanbumgardner/anaconda/faculty.csv'
#convert into pandas dataframe, and be picky about your column names.
df = pd.read_csv(path, header=0)
df.columns = ['Name', 'Degree', 'Title', 'Email']
#you must create variables, right?
title = [x for x in df['Title']]
#because some people have multiple degrees you have to break this one up. It splits with spaces between the degrees.
degrees =[x.split(" ") for x in df['Degree']]

email = [x for x in df['Email']]

new_df = pd.DataFrame(email, columns=['Email'])
new_df.to_csv("profemails.csv")
#thanks pandas, ily

