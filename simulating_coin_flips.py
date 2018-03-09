
# coding: utf-8

# # Simulating Coin Flips

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# outcome of one coin flip
np.random.randint(2)


# In[3]:


# outcomes of ten thousand coin flips
np.random.randint(2, size=10000)


# In[4]:


# mean outcome of ten thousand coin flips
np.random.randint(2, size=10000).mean()


# In[5]:


# outcome of one coin flip
np.random.choice([0, 1])


# In[6]:


# outcome of ten thousand coin flips
np.random.choice([0, 1], size=10000)


# In[7]:


# mean outcome of ten thousand coin flips
np.random.choice([0, 1], size=10000).mean()


# In[8]:


# outcomes of ten thousand biased coin flips
np.random.choice([0, 1], size=10000, p=[0.8, 0.2])


# In[9]:


# mean outcome of ten thousand biased coin flips
np.random.choice([0, 1], size=10000, p=[0.8, 0.2]).mean()

