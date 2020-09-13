#!/usr/bin/env python
# coding: utf-8

# # List1 = [1,2,3,4,5,7,8]
# List2 = [“a”, “b”, “c”, “d”, “e”]
# Convert to a dictionary in one line code using list comprehension (without using zip method)

# In[25]:


#version 1 (using zip)
list1 = [1,2,3,4,5,7,8]
list2 = ['a','b','c','d','e']

dict(zip(list1,list2))


# In[23]:


#version 2 (using naive method)
list1 = [1,2,3,4,5,7,8]
list2 = ['a','b','c','d','e']

dict1 = {}
for i in list1:
    for j in list2:
        dict1[i]=j
        list2.remove(j)
        break
                
print(dict1)


# In[30]:


#version 3 (using list comprehension)
list1 = [1,2,3,4,5,7,8]
list2 = ['a','b','c','d','e']

dict1 = dict([(list1[i],list2[i]) for i in range(len(list2))])
print(dict1)


# In[33]:


#version 3 (using dict comprehension)
list1 = [1,2,3,4,5,7,8]
list2 = ['a','b','c','d','e']
dict1 = {list1[i]:list2[i] for i in range(len(list2))}
print(dict1)


# In[ ]:




