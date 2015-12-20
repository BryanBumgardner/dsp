import pandas as pd
from pandas import DataFrame, read_csv
from collections import OrderedDict
#where is your file? here!
path = '/Users/bryanbumgardner/anaconda/faculty.csv'
#convert into pandas dataframe, and be picky about your column names.
df = pd.read_csv(path, header=0)
df.columns = ['Name', 'Degree', 'Title', 'Email']

#make a dictionary that combines people by last names, for Q6
#def First_name_dict(df):
#	names = [x for x in df['Name']]
#	last = [x.split(" ")[-1] for x in names]
#	df['LastName'] = pd.Series((x for x in last), index=df.index)
#	df = df.set_index(df['LastName'])
#	df = df.drop(['LastName', 'Name'], axis=1) #drop the extra stuff off the dict
#	d = dict()
#	for x in df.index:
#		d[x] = df.loc[[x]].values.tolist()
#	return d
#make sure you only show those first three rows. Lets make vs

#Qsix = First_name_dict(df[:3])


#That's not efficient, lets do full names for Q7
#def full_name_d(df):
#	fullnames = dict()
#	df['Name'] = [tuple(x.split(" ")) for x in df['Name']]
#	df = df.set_index(df['Name'])
#	df = df.drop('Name', axis=1) # we get an extra name when we do this
#	for x in df.index:
#		fullnames[x] = df.loc[[x]].values.tolist()
#	return fullnames

#Qseven = full_name_d(df[:3])

#newdict = df.set_index(df['Name']).to_dict #saving this for later!

#Now do last name first. 

def last_name(df):
	names = [x for x in df['Name']]
	last = [x.split(" ")[-1] for x in names]
	df['LastName'] = pd.Series((x for x in last), index=df.index)
	df = df.set_index(df['LastName'])
	df = df.drop(['LastName', 'Name'], axis=1)
	lastnamed = dict()
	for x in df.index:
		lastnamed[x] = df.loc[[x]].values.tolist() #because you'll get middle initials if you don't
	ordered = OrderedDict(sorted(lastnamed.items(), key=lambda t: t[0][-1]))
	return ordered

Qeight = last_name(df[:3])

#print(Qsix)
#print(Qseven)
print(Qeight)

#uncomment the one you want at any specific time
