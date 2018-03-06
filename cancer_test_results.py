
# coding: utf-8

# # Cancer Test Results

# In[1]:


import pandas as pd
# load dataset
df = pd.read_csv('cancer_test_data.csv')
df.head()


# In[4]:


# number of patients
df.shape


# In[2]:


# number of patients with cancer
df.has_cancer.sum()


# In[5]:


# number of patients without cancer
(df.has_cancer == False).sum()


# In[6]:


# proportion of patients with cancer
df.has_cancer.mean()


# In[7]:


# proportion of patients without cancer
1 - df.has_cancer.mean()


# In[8]:


# proportion of patients with cancer who test positive
(df.query('has_cancer')['test_result'] == 'Positive').mean()


# In[9]:


# proportion of patients with cancer who test negative
(df.query('has_cancer')['test_result'] == 'Negative').mean()


# In[10]:


# proportion of patients without cancer who test positive
(df.query('has_cancer == False')['test_result'] == 'Positive').mean()


# In[11]:


# proportion of patients without cancer who test negative
(df.query('has_cancer == False')['test_result'] == 'Negative').mean()

