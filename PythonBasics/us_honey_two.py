#!/usr/bin/env python
# coding: utf-8

# In[1]:


#step 1- import the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# step2 - read the csv file
df = pd.read_csv("US_honey_dataset.csv")


# In[3]:


df


# In[ ]:


# step 3  data cleaning (EDA) -> Exploratory data analysis


# In[4]:


# remove / drop the unnamed columns 

# axis - 0 (row) , axis - 1 (columns)

df = df.drop(["Unnamed: 0"],axis = 1)


# In[5]:


df


# In[6]:


# check the information about the columns 

df.info()


# In[7]:


df.shape


# In[8]:


# check how many unique states are there

df["state"].unique()


# In[9]:


df["state"].nunique()


# In[10]:


# check how many differene years data I am having

df["year"].nunique()

# 2021 - 1995 = 27


# In[11]:


df["year"].unique()


# In[12]:


df["year"].max()


# In[13]:


df["year"].min()


# In[14]:


# check for null values

df.isnull().sum()


# In[15]:


#checking the duplicate values

df.duplicated()


# In[16]:


df.duplicated().sum()


# In[18]:


df["state"].isnull().sum()


# # 1) Which states are rarely contributing to honey production for the last 27 years?
# 

# In[19]:


data = df["state"].value_counts()


# In[24]:


data


# In[30]:


plt.figure(figsize = (12,12))

plt.pie(data.values,labels = data.index,autopct = "%0.2f%%")

plt.show()


# In[31]:


# least honey producing are 
#Maryland - 9
#oklahoma- 9


# # 2) Which are the top 5 Honey producing states in the US ?
# 

# In[32]:


plt.figure(figsize = (15,10))
sns.barplot(x = df["state"],y = df["production"])
plt.xticks(rotation = 90)
plt.title("State vs Production")
plt.show()


# In[33]:


# compare states by value of honey production

new_value = df.groupby("state").sum().reset_index()


# In[34]:


new_value


# In[35]:


new_df = new_value.sort_values("production",ascending = False)


# In[36]:


new_df


# In[37]:


new_df.head(5)


# In[38]:


plt.figure(figsize = (15,10))
sns.barplot(x = new_df["state"],y = new_df["production"])
plt.xticks(rotation = 90)
plt.show()


# # 3) What is the Change in mean Average price of Honey from 1995 to 2021?

# In[51]:


# to find the average price  for all theyears from 1995 - 2021

df2 = df.groupby("year")["average_price"].mean().reset_index()


# In[52]:


df2


# In[53]:


plt.figure(figsize = (15,10))
sns.barplot(x = df2["year"],y = df2["average_price"])
plt.show()


# In[ ]:


# average price was highest in the year 2017 (302) and lowest is 2019


# # 4) Which was the year when production of Honey in wholeUS was the highest?

# In[62]:


df3 = df.groupby("year")["production"].sum().reset_index()


# In[63]:


df3


# In[64]:


df_new = df3.sort_values("production",ascending = False)


# In[65]:


df_new


# In[69]:


plt.figure(figsize = (15,10))
sns.barplot(x = df_new["year"],y = df_new["production"])
plt.show()


# # 5) From the above inference we get the production was highest in the year 2000, now let
# # infer which state was having highest contribution in that year

# In[ ]:


# which state was having he highest production in the year 2000

# step1 - find all the staes for the year 2000


# In[70]:


data = df[df["year"] == 2000]


# In[71]:


data


# In[72]:


data_df = data.sort_values(by = "production",ascending = False)


# In[73]:


data_df


# In[74]:


plt.figure(figsize = (15,10))
sns.barplot(x = data_df["state"],y = data_df["production"])
plt.xticks(rotation = 90)
plt.show()


# # 6) Which states have the highest no. of colonies in the year 2000?

# In[75]:


df


# In[76]:


data = df[df["year"] == 2000]


# In[77]:


data


# In[78]:


df8 = data.sort_values(by = "colonies_number",ascending = False )


# In[79]:


df8


# In[80]:


plt.figure(figsize = (15,10))
sns.barplot(x = df8["state"], y = df8["colonies_number"])
plt.xticks(rotation = 90)
plt.show()


# In[ ]:




