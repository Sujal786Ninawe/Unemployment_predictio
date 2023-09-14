#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


df= pd.read_csv('Unemployment in India.csv')


# In[3]:


df


# In[4]:


df.isnull().values.any()
   


# In[5]:


df.isnull().sum().sum()


# In[6]:


sujal=df.dropna()


# In[7]:


sujal


# In[8]:


sujal.head(10)


# In[9]:


sujal.drop(sujal.iloc[:,2:3], inplace=True, axis=1)


# In[10]:


sujal


# In[11]:


print(sujal.isnull().sum())


# In[12]:


sujal["Region"].unique()


# In[13]:


sujal2=pd.read_csv("Unemployment in India.csv")
(sujal)


# In[14]:


sujal2 = sujal2.rename(columns={sujal2.columns[0]:'Region',sujal2.columns[3]:'Unemployment_rate',sujal2.columns[4]:'Employed', sujal2.columns[5]:'labour_participation_rate', sujal2.columns[6]:'area'})
sujal2.head()


# In[15]:


region = sujal2.groupby(["Region"])[['Unemployment_rate', "Employed", "labour_participation_rate"]].mean()
region = pd.DataFrame(region).reset_index()

fig = px.bar(region, x="Region", y="Unemployment_rate", color="Region", title="Average Unemployed Rate by Region")
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[16]:


region = sujal2.groupby(["Region"])[['Unemployment_rate', "Employed", "labour_participation_rate"]].mean()
region = pd.DataFrame(region).reset_index()

fig = px.bar(region, x="Region", y="Employed", color="Region", title="Average Employed Rate by Region")
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[17]:


plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(8,6))
sns.heatmap(sujal.corr())
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




