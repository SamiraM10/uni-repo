#!/usr/bin/env python
# coding: utf-8

# In[9]:


from collections import Counter
import sys
def anagram(first,second):
    return Counter(first) == Counter(second)

anagram("abah5","hbaa5");
print(sys.getsizeof("abah5"))


# In[ ]:




