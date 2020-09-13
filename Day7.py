#!/usr/bin/env python
# coding: utf-8

# # Use the dictionary,
# port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"},
# and make a new dictionary in which keys become values and values become keys,
# as shown: Port2 = {“FTP":21, "SSH":22, “telnet":23,"http": 80}# 

# In[1]:


port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}

dict1 = {v:k for k,v in port1.items()}
print(dict1)


# # Take a list of tuple as shown below.
# [(1,2), (3,4), (5,6),(4,5)]
# Make a new list which contains the sum of the number of tuples.
# For example
# Input
# [(1,2), (3,4), (5,6)]
# Output
# [3, 7, 11]

# In[2]:


#version 1
list1 = [(1,2), (3,4), (5,6),(4,5)]
list2 = []
for i in list1:
    list2.append(sum(i))
print(list2)


# In[3]:


#version 2
[sum(i) for i in list1]


# # Take a list as shown below
# [(1,2,3), [1,2], ['a','hit','less']]
# The List contains tuple and lists. Make the elements of inner lists and tuples to outer list
# 

# In[6]:


list1 = [(1,2,3), [1,2], ['a','hit','less']]
list2 = []
for i in list1:
    list2.append(list(i))
tuple1 = tuple(list2)
print(tuple1)


# In[ ]:




