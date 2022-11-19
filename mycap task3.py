#!/usr/bin/env python
# coding: utf-8

# In[7]:


def recursive_fibnocci(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibnocci(n-1) + recursive_fibnocci(n-2))

nterms = 15

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recursive_fibnocci(i))


# In[ ]:




