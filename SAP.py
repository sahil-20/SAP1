#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install numpy


# In[3]:


pip install pandas


# In[4]:


pip install seaborn


# In[7]:


import numpy


# In[5]:


import pandas as pd


# In[6]:


import seaborn as sns


# In[8]:


import sklearn


# In[11]:


from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[150,0]]))


# In[ ]:




