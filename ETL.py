#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine


# ### Store CSV into DataFrame

# In[7]:


suicide_rates_overview_1985_to_2016 = "master.csv"
rate_df = pd.read_csv(csv_file)
rate_df.head()


# In[11]:


new_rate_df = rate_df[['country', 'year', 'age','suicides_no','population','suicides/100k pop']].copy()
new_rate_df.head()


# In[18]:


rds_connection_string = "<inser user name>:<insert password>@127.0.0.1/rate_db"
engine = create_engine(f'mysql://{rds_connection_string}')


# In[21]:


new_rate_df.to_sql(name='new_rate_df', con=engine, if_exists='append', index=False)


# In[22]:


pd.read_sql_query('select * from new_Rate_df', con=engine).head()


# In[ ]:




