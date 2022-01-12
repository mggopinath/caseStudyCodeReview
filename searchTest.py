''' 

Case Study Document Search Test Case

@author: gopinath m g
'''

from documentSearch import *

print("****************************** Target Document Search Case Study *************************************************")
print("1. Simple String Search")
print("2. Regular Expression Search")
print("3. Index Search")
option = input("Enter your option:")

if option == '1':
	sval=input("Enter your String Value: ")
	sstart = timeit.default_timer()
	print("Search Results:")
	search_match(sval)
	send = timeit.default_timer()
	print("Simple String Match Elaspse Time ---->",send-sstart,"ms")
elif option =='2':
	rgval=input("Enter your String Value: ")
	rgstart = timeit.default_timer()
	print("Search Results:")
	search_regx(rgval)
	rgend = timeit.default_timer()
	print("Simple String Match Elaspse Time ---->",rgend-rgstart,"ms")
elif option =='3':
	ival=input("Enter your String Value: ")
	istart = timeit.default_timer()
	print("Search Results:")
	search_str_index(ival)
	iend = timeit.default_timer()
	print("Simple String Match Elaspse Time ---->",iend-istart,"ms")
else:
	print("Please Select the Valid Option --> Program exit")
	