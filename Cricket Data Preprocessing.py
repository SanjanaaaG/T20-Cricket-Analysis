#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import json


# In[3]:


with open('t20_wc_match_results.json') as f:
    data = json.load(f)


# In[4]:


df_match = pd.DataFrame(data[0]['matchSummary'])
df_match.head()


# In[5]:


df_match.shape


# In[6]:


df_match.rename({'scorecard' : 'match_id'} , axis = 1 , inplace = True)
df_match.head()


# In[7]:


match_ids_dict = {}

for index , row in df_match.iterrows():
    key1 = row['team1'] + ' Vs ' + row['team2']
    key2 = row['team2'] + ' Vs ' + row['team1']
    
    match_ids_dict[key1] = row['match_id']
    match_ids_dict[key2] = row['match_id']
    


# In[8]:


match_ids_dict


# In[ ]:


df_batting.to_csv('t20_wc_match_summary' , index = False)


# In[ ]:





# In[10]:


with open('t20_wc_batting_summary.json') as f:
    data = json.load(f)
    
    all_records = []
    
    for rec in data:
        all_records.extend(rec['battingSummary'])
        
all_records


# In[11]:


df_batting = pd.DataFrame(all_records)
df_batting.head(10)


# In[12]:


df_batting['out/not_out'] = df_batting.dismissal.apply(lambda x : 'out' if len(x)>0 else 'not_out')
df_batting.head()


# In[13]:


df_batting.drop(columns=['dismissal'] , inplace = True)
df_batting.head(11)


# In[14]:


df_batting.head(31)


# In[15]:


df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda x : x.replace('â€' , ' '))
df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda x : x.replace('\xa0' , ' '))
df_batting.head(10)


# In[16]:


match_ids_dict['Namibia Vs Sri Lanka']


# In[17]:


df_batting['match_id'] = df_batting['match'].map(match_ids_dict)


# In[18]:


df_batting.head()


# In[19]:


df_batting.to_csv('t20_wc_batting_summary' , index = False)


# In[ ]:





# In[20]:


with open('t20_wc_bowling_summary.json') as f:
    data = json.load(f)
    
    all_rec = []
    
    for rec in data:
        all_rec.extend(rec['bowlingSummary'])
        
all_rec


# In[21]:


df_bowling = pd.DataFrame(all_rec)
df_bowling.head(10)


# In[22]:


df_bowling.head(20)


# In[24]:


df_bowling['match_id'] = df_bowling['match'].map(match_ids_dict)


# In[25]:


df_bowling.head(10)


# In[26]:


df_bowling.to_csv('t20_wc_bowling_summary.csv', index = False)


# In[ ]:





# In[28]:


with open('t20_wc_player_info.json') as f:
    data = json.load(f)


# In[29]:


df_players = pd.DataFrame(data)

print(df_players.shape)
df_players.head(10)


# In[30]:


df_players['name'] = df_players['name'].apply(lambda x: x.replace('â€', ''))
df_players['name'] = df_players['name'].apply(lambda x: x.replace('†', ''))
df_players['name'] = df_players['name'].apply(lambda x: x.replace('\xa0', ''))
df_players.head(10)


# In[31]:


df_players[df_players['team'] == 'India']


# In[32]:


df_players.to_csv('t20_wc_players.csv', index = False)

