#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, k = input().split()

K = int(k)

N = int(n)

count=0

for i in range(N):
    elements = int(input())
    if(elements%K==0):
        count+=1

print(count)

