# -*- coding: utf-8 -*-



result = 5*100 / 5 + 1**1 - 0.75
print(result)

result = 4 * (6 + 5)
print(result)

result =  4 * 6 + 5 
print(result)

result = 4 + 6 * 5 
print(result)

s = 'hello'
print(s[1])

print(s[::-1])

print(s[4])
print(s[-1])

l = {0 , 0, 0}
print(l)
l = [0]*3
print(l)

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'

print(list3)

list4 = [5,3,4,6,1]
list5 = sorted(list4)
print(list5)


d = {'simple_key':'hello'}
# Grab 'hello'
s = d['simple_key']
print(s)


d = {'k1':{'k2':'hello'}}
# Grab 'hello'
s = d['k1']['k2']
print(s)

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
s = d['k1'][0]['nest_key'][1][0]
print(s)

#Grab hello
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
s = d['k1'][2]['k2'][1]['tough'][2][0]
print(s)

list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]

# Convert the list to a set to remove duplicates
unique_values_set = set(list5)

# Convert the set back to a list if needed
unique_values_list = list(unique_values_set)

print(unique_values_list)  # Output: [1, 2, 33, 4, 11, 22, 3]

result_1 = 2 > 3
result_2 = 3 <= 2
result_3 = 3 == 2.0
result_4 = 3.0 == 3
result_5 = 4**0.5 != 2

# Printing results
print(result_1)  # Output: False
print(result_2)  # Output: False
print(result_3)  # Output: False
print(result_4)  # Output: True
print(result_5)  # Output: False


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
result = l_one[2][0] >= l_two[2]['k1']
print(result) #false

for num in l_one:
       print(num)
       print(5)

x = 5
while x < 10:
    print(x)
    x += 1
    
    
    