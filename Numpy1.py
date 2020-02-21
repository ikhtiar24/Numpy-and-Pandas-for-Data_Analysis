#!/usr/bin/env python
# coding: utf-8

# # Data Analysis with Numpy - - - - 

# In[1]:


lis =[1,2,3,4]


# In[2]:


import numpy as np


# In[3]:


lis 


# In[4]:


arr = np.array(lis)


# In[5]:


arr


# In[6]:


mat = [[1,2,3], [4,5,6],[7,8,9]]


# In[7]:


np.array(mat)


# In[10]:


np.arange(0,11)


# In[11]:


np.arange(0,11,2) # show all even number between range-


# In[12]:


np.zeros(3) # to generate all zeros


# In[13]:


np.zeros((5,5)) # number of rows = number of column


# In[14]:


np.zeros((2,5)) # 2-rows and 5 columns 


# In[15]:


np.ones(4)


# In[16]:


np.ones((3,4))


# In[17]:


np.linspace(0,5,10) # Gotland space


# In[18]:


np.eye(4) # generate square matrix


# In[19]:


np.random.rand(5)


# In[20]:


np.random.rand(5,5)


# In[21]:


np.random.randn(2) # random numbers


# In[22]:


np.random.rand(4,4) # 4-4 matrix


# In[23]:


np.random.randint(1,100,10 ) # low- inclusive, high- exclusive


# In[24]:


arr= np.arange(25)


# In[25]:


arr


# In[26]:


ranarr = np.random.randint(0,50,10) # could be 10 integers there


# In[27]:


ranarr


# In[28]:


arr.reshape(5,5)


# In[29]:


ranarr.max() #find max value


# In[30]:


ranarr.min() #find min value


# In[31]:


ranarr


# In[32]:


ranarr.argmax() # find the location of the max value


# In[33]:


ranarr.argmin() # find the location of the min value


# In[34]:


arr.shape


# In[35]:


arr.dtype #data type


# In[36]:


from numpy.random import randint


# In[37]:


randint(2,10)


# # NumPy Indexing and Selection

# In[38]:


arr = np.arange(1,11)


# In[39]:


arr


# In[40]:


arr[8]


# In[41]:


arr[1:6]


# In[42]:


arr[:6]


# In[43]:


arr[5:]


# In[44]:


arr[0:5]= 100 #braodcast first 5 digit


# In[45]:


arr


# In[46]:


arr = np.arange(1,11)


# In[47]:


slice_arr = arr[0:6]


# In[48]:


slice_arr


# In[54]:


import numpy as np

ar_2d = np.array([[5,10,15],[20,30,40],[25,35,45]])


# In[55]:


ar_2d


# In[56]:


ar_2d[0][0] # row... then column


# In[57]:


ar_2d[1][1]


# In[58]:


ar_2d[:2,1:] #grab data top of the right corner 


# In[59]:


# conditonal array

arr = np.arange(1,11)


# In[60]:


arr


# In[66]:


bool_arr = arr>5


# In[67]:


bool_arr


# In[68]:


arr[bool_arr]


# In[70]:


arr[arr<3]


# In[71]:


arr_2d = np.arange(50).reshape(5,10)


# In[72]:


arr_2d 


# In[74]:


arr_2d[1:3,3:5]


# ### Array with array
# ### Array with scalars
# ### Universal array functions

# In[76]:


arr = np.arange(0,11)


# In[77]:


arr


# In[78]:


arr+arr


# In[79]:


arr-arr


# In[80]:


arr*arr


# In[81]:


arr+100 # scalar


# In[82]:


arr/arr


# In[83]:


arr **2  # square


# In[84]:


np.sqrt(arr)


# In[85]:


np.max(arr)


# In[86]:


np.sin(arr) # numpy functions 


# In[87]:


np.log(arr) # numpy functions 


# In[88]:


np.exp(arr)


# # NumPy Exercises - 

# In[89]:


import numpy as np


# In[90]:


np.zeros(10)


# In[91]:


np.ones(10)


# In[92]:


np.ones(10)*5


# In[93]:


np.zeros(10)+5


# In[94]:


np.arange(10,51)


# In[97]:


np.arange(10,51,2)


# In[99]:


np.arange(9).reshape(3,3)


# In[102]:


a = np.arange(9)
a.reshape(3,3)


# In[103]:


np.eye(3) # idendtity matrix


# In[104]:


np.random.rand(1) #create random numbers


# In[105]:


np.random.randn(25)


# In[108]:


np.arange(1,101).reshape(10,10)/100


# In[109]:


np.linspace(0.01,1,100).reshape(10,10)


# In[110]:


np.linspace(0,1,20) #create space


# In[112]:


mat = np.arange(1,26).reshape(5,5)


# In[114]:


mat


# In[115]:


mat[2:,1:]


# In[116]:


mat[3,4]


# In[117]:


mat[:3,1]


# In[119]:


mat[-1:]


# In[120]:


np.sum(mat) # mat.sum()- get same answer


# In[121]:


mat.std() # standard deviation


# In[122]:


mat.sum(axis=0)


# # NumPy - Matplotlib 

# In[128]:


import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11)
y = 2 * x + 5
plt.title("Matplot Graph")
plt.xlabel(" x - axis direction")
plt.ylabel(" y - axis direction")
plt.plot(x,y)
plt.show()


# In[129]:


import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11)
y = 2 * x + 5
plt.title("Matplot Graph")
plt.xlabel(" x - axis direction")
plt.ylabel(" y - axis direction")
plt.plot(x,y,"ob")  # 'ob' --- format string in plot function
plt.show()


# In[132]:


import numpy as np 
import matplotlib.pyplot as plt  

# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 4 * np.pi, 1) 
y = np.sin(x) 
plt.title("sine wave form") 

# Plot the points using matplotlib 
plt.plot(x, y) 
plt.show() 


# In[135]:


from matplotlib import pyplot as plt 
x = [5,8,10] 
y = [12,20,8]  

x2 = [6,9,11] 
y2 = [6,15,7] 
plt.bar(x, y, color = 'r', align = 'center') 
plt.bar(x2, y2, color = 'g', align = 'center') 
plt.title('Bar Graph') 
plt.ylabel('Y axis direction') 
plt.xlabel('X axis direction')  

plt.show()


# In[ ]:




