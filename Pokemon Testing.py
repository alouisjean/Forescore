#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import os
import datetime
import re
from itertools import islice
os.getcwd()
os.chdir('C:\\Users\\aaron//Downloads')


# In[2]:


df = pd.read_csv('pokemon.csv')
df= df.drop(columns = ['id','Form'])
df.head()


# In[3]:


# df = df.drop(columns = ['Total']) to remove columns ; have to equal it back to df

df['Total'] = df.iloc[:, 4:10].sum(axis=1) #sum accross row
df.head(6)


# In[5]:


copy = df.copy()
copy.head()


# In[17]:


copy = copy[['Name','Type1','Type2','Total','Attack','Defense']]
copy.head()


# In[19]:


#copy.to_csv('modified_poke.csv',index=False)


# In[31]:


# Filter for certain values 
newdf = df.loc[(df['Type1'] == 'Grass') & (df['Total'] > 350)]

newdf.reset_index(drop=True, inplace=True)

newdf2 = df.loc[2]
print(newdf2)
newdf.head()


# In[46]:


df.loc[df['Name'].str.contains('saur')] # ~ means not 

df.loc[df['Type1'].str.contains('Fire|Water')]  #fire or water 


# In[56]:


df.loc[df['Type1'] == 'Fire', 'Type1'] = 'Flames'  #use first condition to change value
df.head()


# In[ ]:




