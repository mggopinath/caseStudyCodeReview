'''

Performance Test script for documentSearch
@author: gopinath m g
'''

from documentSearch import *
from tabulate import tabulate


sample=["The","more","the","more","is","Is","THE","welcome","IS","done"]

#Repeat function
def repeat_fun(times, f):
    for i in range(times): f()


#Simple String Match		
print("******************Simple String Match***********************")

def performance_search_match():	
	for list in sample:
		search_match(list)
	
sstart = timeit.default_timer()
repeat_fun(10000, performance_search_match)
send=timeit.default_timer()
performance_search_match_eTIME = send-sstart
print("Simple String match Elaspse Time --->", performance_search_match_eTIME, "ms")
print()

#Regular Expression Search
print("******************Regular Expression Search***********************")
def performance_search_regx():	
	for list1 in sample:
		search_regx(list1)
	
rstart = timeit.default_timer()
repeat_fun(10000, performance_search_regx)
rend=timeit.default_timer()
performance_search_regx_eTIME = rend-rstart
print("Regular Expression String Match Elaspse Time ---->", performance_search_regx_eTIME, "ms")
print()

#String Index Search

print("******************String Index Search***********************")
def performance_search_regx():	
	for list2 in sample:
		search_str_index(list2)
	
rstart = timeit.default_timer()
repeat_fun(10000, performance_search_regx)
rend=timeit.default_timer()
performance_search_str_index_eTIME = rend-rstart
print("String Index Search Match Elaspse Time ---->", performance_search_str_index_eTIME, "ms")
print()


#print("Simple String match Elaspse Time --->", performance_search_match_eTIME, "ms")
#print("Regular Expression String Match Elaspse Time ---->", performance_search_regx_eTIME, "ms")
#print("String Index Search Match Elaspse Time ---->", performance_search_str_index_eTIME, "ms")

#Table for Performance Test Results
print("***********************************PERFORMANCE TEST RESULTS***************************************************")

performance_result_table = [['Search Method', 'Simple String Match', 'Regular Expression Search','String Index Search Match'], ['Elaspse Time(ms)', performance_search_match_eTIME, performance_search_regx_eTIME, performance_search_str_index_eTIME ]]
print(tabulate(performance_result_table, headers='firstrow', tablefmt='grid'))