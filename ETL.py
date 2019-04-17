#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine


# ### Store CSV into DataFrame

# In[2]:


data = "csiro_recons_gmsl_yr_2015_csv.csv"
rate_df = pd.read_csv(data)
rate_df.head()


# In[3]:


data2 = "epa-sea-level_csv.csv"
rate2_df = pd.read_csv(data2)
rate2_new_df = rate2_df.drop(columns=['NOAA Adjusted Sea Level'])
rate2_new_df.head()


# In[5]:


rds_connection_string = "root:3SARAnora@127.0.0.1/sea_level_change"
engine = create_engine(f'mysql+pymysql://{rds_connection_string}')


# In[6]:


rate_df.to_sql(name='csiro_recons_gmsl_yr_2015', con=engine, if_exists='append', index=False)


# In[7]:


rate2_new_df.to_sql(name='epa_sea_level', con=engine, if_exists='append', index=False)


# In[8]:


engine.table_names()


# In[9]:


pd.read_sql_query('select * from csiro_recons_gmsl_yr_2015', con=engine).head()


# In[10]:


pd.read_sql_query('select * from epa_sea_level', con=engine).head()


# In[ ]:




