#!/usr/bin/env python
# coding: utf-8

# # Pilot Problem 
# 

# In[5]:


height =int(input('Enter the height : '))
print(f'{height} ft')
if height <= 1000:
    print("Safe to land")
elif height>1000 and height<=5000:
    print('Bring down to 1000ft')
else:
    print('Go around and try later ')


# # Prime number

# In[27]:



for num in range(2,200):
    for i in range(2,num):
        if(num%i)== 0:
            break
    else:
        print(num)
        


# In[ ]:




