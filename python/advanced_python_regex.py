import pandas as pd
import re
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
#Now that you've set these up, it's time to work on them. Test them first with these:
#print (email)
#print (title)
#print (email)
#print (degrees)

#This will assign a dictionary to title so you can search it. It also counts the specific types and prevents redundancy.
def title_count(title):
	title_dict = dict()
	for x in title:
			if x not in title_dict:
				title_dict[x] = 1
			else:
				title_dict[x] += 1
	return title_dict
#this puts the parts together. There's one for each function.
final_titles = title_count(title)

#this one organizes and counts the degrees. 
def degree_count(degrees):
	new = []
	d = dict()
	for x in degrees:
		#this part allows for people with multiple degrees.
		if len(x) >1:
			new.append(x[0])
			del(x[0])
		new.append(x[0])
		#the smoothest way to do this, I think
	for x in new:
		if x not in d:
				d[x] = 1
		else:
				d[x] += 1
	return d

The_list = degree_count(degrees)

def count_domains(email):
	all_domains =[]
	atsign = "@"
	#rename it for clarity
	for x in email:
			all_domains.append(x[(x.index(atsign)):])
	domain_dict = dict()
	for x in all_domains:
		if x not in domain_dict:
			domain_dict[x] = 1
		else:
			domain_dict[x] += 1
	return domain_dict

final_domains = count_domains(email)


print("Total number of degrees:", The_list)
print("Total number of titles:", final_titles)
print("List of domains:", final_domains)
print("Faculty emails:", email)



