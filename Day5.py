#!/usr/bin/env python
# coding: utf-8

# # Write a program to identify sub list [1,1,5] is there in the given list in the same order, if yes print
# “it’s a Match” if no then print “it’s Gone” in function.
# Example -
#  Listy =[1,5,6,4,1,2,3,5] - it’s a Match
# Listy = [1,5,6,5,1,2,3.6] - it’s Gone

# In[7]:


list1 = [1,5,6,5,1,2,3.6]
sub_list = [1,1,5]

def check(x,y):
    for i in x:
        for j in y:
            if len(y)>=0 and i==j:
                y.pop(0)
            else :
                break
    return y
if len(check(list1,sub_list))==0:
    print('Its a Match ')
else:
    print('its Gone')
    


# # Make a Function for prime numbers and use Filter to filter out all the prime numbers from 1-2500

# In[84]:


def isprime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
        else:
            return True
    else:
        return False
    
                    
                


# In[86]:


list1 = list(range(2500))
prime_nos = list(filter(isprime,u))
print(prime_nos)


# # Make a Lambda function for capitalizing the whole sentence passed using arguments.
# And map all the sentences in the List, with the lambda functions
# [“hey this is sai”,I am in mumbai”,....]
# o/p- [“Hey This Is Sai”, I Am In Mumbai”,....]

# In[20]:


list2 = ['hey this is sai','I am in mumbai']
Capital = list(map(lambda str1:str1.title(),list2))
print(Capital)


# In[ ]:




