#!/usr/bin/env python
# coding: utf-8

# # start Pandas for Data Analysis 

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[13]:


labels = ['a','b','c','d']
mdata = [10,20,30]


# In[14]:


arr = np.array(mdata)
d = {'a':10,'b':20,'c':30}


# In[15]:


mdata


# In[16]:


d


# In[17]:


arr


# In[21]:


pd.Series(data=mdata)


# In[30]:


labels


# In[32]:


pd.Series(labels)


# In[35]:


ser1 = pd.Series([1,2,3,4],['USA','GERMANY','INDIA','BANGLADESH'])


# In[36]:


ser1


# In[37]:


ser2 = pd.Series([1,2,3,4],['USA','GERMANY','Italy','BANGLADESH'])


# In[38]:


ser2['GERMANY']


# In[41]:


ser1+ser2    # can't find the match. answer is 'no'
             # integer converted into float


# # DataFrames

# In[42]:


from numpy.random import randn


# In[43]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[44]:


df


# In[50]:


df[['W','Z']]


# In[46]:


type(df)


# In[51]:


df['New'] = df ['W']+df['Z']


# In[52]:


df


# In[53]:


del df['New'] # df.drop('New',axis =1)


# In[54]:


df


# In[55]:


df.shape


# In[60]:


df.loc['A']


# In[63]:


df.loc[['A','B'],['W' ,'Y']]


# In[64]:


df>0


# In[65]:


df['W']>0


# In[67]:


df[df['Z']<0]


# In[68]:


Newind = 'av vd eb re ae'.split()


# In[69]:


Newind


# In[70]:


df['States'] = Newind


# In[71]:


df


# In[ ]:




