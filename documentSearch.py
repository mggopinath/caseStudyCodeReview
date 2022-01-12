'''
CASE Study Document Search CORE Program
@author: gopinath m g
'''

import os
import re
import timeit

data_existing="sampleText//"

def sort_dict_by_value(d, reverse=False):
	return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

#Simple String Match
def search_match(fsearch):
	list1=[]
	search_desc={}
	#Appending the Files Names into List
	with os.scandir(data_existing) as entries:
		for entry in entries:
			list1.append(entry.name)
	#Fetch the file names one by one
	for word in list1:
		hit_count=0
		#Open the txt files in read only mode
		with open(data_existing+word, 'r') as f:
			for line in f:
				hit_count = hit_count+line.count(fsearch)
			search_desc[word]=hit_count
		desc_result=sort_dict_by_value(search_desc,True)
	#Print the Search count Results in Descending order
	for k,v in desc_result.items():
		print(k,'----->',v,' matches')



#Regular Expression CaseIgnore Search

def search_regx(regxSearch):
	list1=[]
	search_desc={}
	#Appending the Files Names into List
	with os.scandir(data_existing) as entries:
		for entry in entries:
			list1.append(entry.name)
	#Fetch the file names one by one
	for word in list1:
		matched = 0
		with open(data_existing+word, 'r') as f:
			for line in f:
				#Regular Expression FindAll methold
				result=re.findall(regxSearch, line, re.IGNORECASE)
				matched = matched + len(result)
			search_desc[word]=matched
		desc_result=sort_dict_by_value(search_desc,True)
	#Print the Search count Results in Descending order
	for k,v in desc_result.items():
		print(k,'----->',v,' matches')


#String Index Search

def search_str_index(indexInput):
	list1=[]
	search_desc={}
	#Appending the Files Names into List
	with os.scandir(data_existing) as entries:
		for entry in entries:
			list1.append(entry.name)
	#Fetch the file names one by one
	for word in list1:
		indexcount = 0
		with open(data_existing+word, 'r') as f:
			for line in f:
				index=0
				while index < len(line):
					index=line.find(indexInput, index)
					if index == -1:
						break
					index += len(indexInput)
					if index > -1:
						indexcount = indexcount + 1
			search_desc[word] = indexcount
		desc_result=sort_dict_by_value(search_desc,True)
	#Print the Search count Results in Descending order
	for k,v in desc_result.items():
		print(k,'----->',v,' matches')


#End of Search Document program		
				
