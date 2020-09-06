#!/usr/bin/env python
# coding: utf-8

# # First Armstrong

# In[31]:


#num = 1634
# Changed num variable to string,
# and calculated the length (number of digits)
l=1042000
u=702648265
for num in range(l,u):
    order = len(str(num))
    # initialize sum
    sum = 0
    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    # display the result
    if num == sum:
        print(num,"is an Armstrong number")
        break
    


# In[ ]:




