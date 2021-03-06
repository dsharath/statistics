
# coding: utf-8

# # Conditional Probability & Bayes Rule Quiz

# In[1]:


# load dataset
import pandas as pd
df = pd.read_csv('cancer_test_data.csv')
df.head()


# In[ ]:


# What proportion of patients who tested positive has cancer?
df.query('test_result == \"Positive\"')['has_cancer'].mean()


# In[2]:


# What proportion of patients who tested positive doesn't have cancer?
1 - df.query('test_result == \"Positive\"')['has_cancer'].mean()


# In[3]:


# What proportion of patients who tested negative has cancer?
df.query('test_result == \"Negative\"')['has_cancer'].mean()


# In[4]:


# What proportion of patients who tested negative doesn't have cancer?
1 - df.query('test_result == \"Negative\"')['has_cancer'].mean()

