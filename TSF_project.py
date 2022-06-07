#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis - Retail
# # The spark foundation 
# I used Python to perform EDA on this Retail Dataset.
# 
# dataset link: https://bit.ly/3i4rbWl
#                                                                                       
#                                                                                       -- Shubham Gupta --

# Import most important Liabraries

# In[1]:


import numpy as np
import pandas as p
import seaborn as s
import matplotlib.pyplot as m


# In[3]:


data= p.read_csv("C:/Users/Shubham/Downloads/SampleSuperstore.csv")


# In[25]:


data


# # Basic idea of data Inside

# In[ ]:


data.sample() # gives rows randomly an certain numbers you specify


# In[ ]:


data.describe() #discription of data like mean,max,std,quartile etc at glance


# In[ ]:


data.info() #basic information of data


# In[ ]:


data.isnull().sum() #to get total null values in each column


# In[ ]:


data.columns #to display columns name


# In[ ]:


data['City'].unique() # to get unique vales in perticular column


# In[ ]:


data['column name'].value_counts() #returns a series containing counts of unique values in specific column


# In[ ]:


data.head() #to get first 5 rows 


# # get total counts of unique values in each column

# In[ ]:


for i in data.columns:
    print(i,len(data[i].unique()))


# # Data Visualization using various plots:

# In[25]:


segment_totalprofit_category_wise= s.catplot(y='Profit',x='Category',estimator= sum,kind="bar",data=data,height=5,aspect=2,row='Segment')

m.show()


# In[35]:


all=s.pairplot(data)


# In[18]:


s.catplot(x='Quantity',col='Region' ,kind='count',data=data)
m.show()


# In[28]:


s.relplot(y='State',x='Sales',kind='scatter',data=data,height=8,aspect=2,color='green')
m.show()


# In[39]:


lines=s.relplot(x='Sales',y='Profit',kind="line",data=data,row='Ship Mode',height=4,aspect=2)
s.set(font_scale=1)


# In[54]:


s.catplot(x="Region",y='Discount',kind='box',data=data,aspect=2,estimator=sum,margin_titles=True,row='Segment')
m.show()


# In[ ]:


df=s.relplot(x='Ship Mode',y='Sales',data=data,kind="line")


# # Thank you
# 
