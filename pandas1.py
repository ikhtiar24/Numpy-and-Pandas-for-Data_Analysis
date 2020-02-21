#!/usr/bin/env python
# coding: utf-8

# # Start Python with Ikhtiar Ahmed
# 
# ##### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# In[1]:


import pandas as pd
df = pd.read_csv("result_sheet.csv")


# In[2]:


df


# In[3]:


df.head(10)


# In[4]:


df.tail(10)


# In[5]:


df.columns


# In[6]:


df["Roll"]


# In[7]:


df.Gender 


# In[9]:


df[["Roll","Gender","Name"]]


# In[11]:


df[df['Gender']=='Male'] #filtering


# In[12]:


df[df['Gender']=='Female']


# In[13]:


df.iloc[0:5]  #first 5 row show


# In[15]:


for index, row in df.iterrows(): # list of data 
      print(index,row["Name"])


# In[18]:


df["Total"] = df["Bangla"]+ df["Math"]+ df["English"]


# In[20]:


df 


# In[23]:


ndf= df.sort_values("Total", ascending = False) # descending order --> ascending = True
    


# In[24]:


ndf["New Roll"] = ndf.index


# In[25]:


ndf


# In[26]:


del ndf["New Roll"]


# In[27]:


del ndf["total"]


# In[28]:


ndf


# In[29]:


ndf["New Roll"] = range(1,21)


# In[30]:


ndf


# In[31]:


ndf.to_csv("new_result_2020.csv")


# In[ ]:




