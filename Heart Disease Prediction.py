#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


dt = pd.read_csv("C:/Users/Prajwal Kulkarni/heart.csv")


# In[13]:


dt.head()


# In[20]:


dt.tail()


# In[14]:


#To get column names
dt.columns.values


# In[15]:


dt.isna().sum()


# In[16]:


dt.info()


# In[18]:


dt.hist(bins = 50, grid = False, figsize = (20,15));


# In[19]:


dt.describe()


# In[41]:


questions = ["1. How many people have heart disease and how many people doesn't have heart disease?",
             "2. Which sex people have most heart disease?",
             "3. People of which sex type have which type of chest pain the most?",
             "4. People with which chest pain are most likely prone to have heart disease?",
             "5. People of which sex has most exercise induced angina?",
             "6. People of which sex type have more fasting blood sugar which is > 120 mg/dl? "]


# In[42]:


questions


# #ANSWERS TO ABOVE QUESTIONS

# In[23]:


dt.target.value_counts()


# In[27]:


dt.target.value_counts().plot(kind = 'bar', color = ['blue', 'red'])
plt.title("Heart disease values")
plt.xlabel("1 = Disease, 0 = No disease")
plt.ylabel("Total number of people");


# In[30]:


dt.target.value_counts().plot(kind = 'pie', figsize = (8,6))
plt.legend(["Disease", "No disease"])
plt.title("Pie chart");


# In[31]:


dt.sex.value_counts()


# In[32]:


dt.sex.value_counts().plot(kind = 'pie', figsize = (8,6))
plt.legend(["Male", "Female"])
plt.title("Pie chart");


# In[33]:


pd.crosstab(dt.sex, dt.target)


# In[34]:


sns.countplot(x = 'target', data = dt, hue = 'sex');


# In[35]:


dt.cp.value_counts()


# In[38]:


dt.cp.value_counts().plot(kind = 'bar', color =["blue", "green", "red", "yellow"])
plt.title("Graph showing chest pain Vs Total amount of people")
plt.xlabel("chest pain")
plt.ylabel("Total amount of people");


# In[37]:


pd.crosstab(dt.sex, dt.cp)


# In[40]:


pd.crosstab(dt.sex, dt.cp).plot(kind = 'bar', color =["blue", "green", "red", "yellow"])
plt.title("Type of chest pain Vs Amount of people")
plt.xlabel("0 = Female,, 1 = Male")
plt.ylabel("amount of people");


# In[43]:


pd.crosstab(dt.cp, dt.target)


# In[44]:


sns.countplot(x = 'cp', data = dt, hue = 'target');


# In[46]:


df.head(10)


# In[ ]:


sns.countplot(x = 'exang', data = dt, hue = 'sex')
plt.title("Exercise induced angina Vs sex");


# In[ ]:




