#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())

for j in range(n):
    N = int(input())
    int_string = str(N)
    mapping = map(int, int_string)
    mapped = list(mapping)
    
    rev_map = mapped[::-1]
    strings = [str(i) for i in rev_map]
    
    joined_string = "".join(strings)
    
    string_int = int(joined_string)
    
    print(string_int)

