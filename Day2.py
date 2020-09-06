#!/usr/bin/env python
# coding: utf-8

# # List

# In[56]:


list1= [2,3,4,5,67,9]


# In[13]:


list1.append(1)
print(list1)


# In[14]:


list1.insert(1,0)
print(list1)


# In[57]:


list1.pop()
print(list1)


# In[16]:


list1.remove(1)
print(list1)


# In[21]:


list2 = [9,3,5,6]
list1.extend(list2)
print(list1)


# # Dictionary

# In[22]:


dict1 ={'Rohit':78,'Biki':76,'Rahul':56,'Samuel':67}


# In[23]:


dict1.keys()


# In[24]:


dict1.values()


# In[26]:


dict1.items()


# In[27]:


dict1.get('Rahul')


# In[32]:


list1= ['X','Y','Z']
list2= [1,2,3]
dict1 = dict.fromkeys(list1,list2)
print(dict1)


# # Sets

# In[40]:


set1 = {12,34,54}


# In[37]:


set1.add(13)
print(set1)


# In[42]:


set1.clear()
print(set1)


# In[50]:


set2 ={12,24,45}
set1 = set2.copy()
print(set1)


# In[51]:


set1.pop()


# In[54]:


set1 ={1,2,3}
set2= {4,5,6}
set1.union(set2)


# # Tuple

# In[63]:


tuple1 =(3,4,56,6)


# In[64]:


tuple1.count(4)


# In[66]:


tuple1.index(56)


# # Strings

# In[69]:


str1 = 'Hello World'
print(str1)


# In[70]:


str1.lower()


# In[71]:


str1.upper()


# In[72]:


str1.replace('H','L')


# In[73]:


str1.split()


# In[77]:


str1.find('e')


# In[ ]:




