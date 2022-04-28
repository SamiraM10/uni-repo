#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import Counter
def anagram(first,second): 
    import sys
    print(sys.getsizeof(first,second)) # 24
    return Counter(first) == Counter(second)

anagram("abcde", "badec") #True


# In[ ]:




