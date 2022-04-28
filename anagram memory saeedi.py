#!/usr/bin/env python
# coding: utf-8

# In[26]:


from collections import Counter 
import sys
def anagram(first, second):
    print(sys.getsizeof('first'))
    return Counter(first) == Counter(second)
anagram("abcd3", "3acdb") #True


# In[ ]:




