
# coding: utf-8

# In[1]:


#essential packages for dataimport/visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from scipy import stats

#More advanced visualizing
import seaborn as sns
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
sns.set(style='ticks', palette='Set2')
# shows graphs in notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#this is how i renamed the data
fifa_data = pd.read_csv("/Users/tclawson/Desktop/fifa_ranking.csv")


# In[3]:


#I want to see what is included in the data, this helps me see the first 20 rows of data.
fifa_data.head(20)


# In[4]:


#how to get summary stats
fifa_data.describe()


# In[5]:


#now that I have the basic information understood in the data set, 
#I want to visualize the data so I can see trends as well as outliers


# In[6]:


#I am defining a function that visualizes, allowing me to see rank and how it relates to points
def plotrankpoints(file):
    fig, ax = plt.subplots()
    ax.scatter(x = file['rank'],y = file['total_points'])
    plt.ylabel('Total Points', fontsize=13)
    plt.xlabel('Ranking', fontsize=13)
    plt.show()


# In[7]:


#here I'm using the newly defined function and having it read in the fifa data set
plotrankpoints(fifa_data)


# In[8]:


#I want to remove all of those teams with zero points that we saw in the graph above
fifa_data = fifa_data.drop(fifa_data[(fifa_data['total_points']<1)].index)


# In[9]:


plotrankpoints(fifa_data)

#we've removed the zeros


# In[10]:


fifa_data.describe()
#now that we've removed zeroes this gives us an idea of how much data we are working with


# In[11]:


#I'm curious what countries are in the data set. 
fifa_data['country_full'].unique()


# In[12]:


#I'm curious how often each country is in the set 
fifa_data['country_full'].value_counts()


# In[13]:


#this gives us a good idea of how many data points and what is in the set
fifa_data.info()


# In[14]:


#can I map a country on a plot over time? How did a specific country do overtime?
#Lets try denmark

fig, ax = plt.subplots()
ax.scatter(x = fifa_data['rank_date'],y = fifa_data['rank'])
#naming axis
plt.ylabel('Rank', fontsize=13)
plt.xlabel('Year', fontsize=13)
plt.show()


# In[15]:


#ok, that clearly included every country, how can I specify one country?
#lets make a new data set that includes only one country


# In[16]:


#lets make a dataset that only includes denmarks information overtime
denmark = fifa_data.loc[fifa_data['country_full'] == 'Denmark']


# In[17]:


#what is in the denmark data?
denmark


# In[18]:


#Great, we have unique data refelcting Denmark and thier results by month since Aug 2011, Lets visualize thier
#ranking overtime to understand which way they have been trending


# In[19]:


#Lets create a function that plots rank over time
def plotranktime(file):
    fig, ax = plt.subplots()
    ax.scatter(x = file['rank_date'],y = file['rank'])
    #naming axis
    plt.ylabel('Rank', fontsize=13)
    plt.xlabel('Date', fontsize=13)
    plt.xticks(rotation=90)
    plt.show()


# In[20]:


#using the new function lets look at Denmarks international rank over time
plotranktime(denmark)


# In[21]:


#BOOM, team ranking overtime
#lets compare it to points over time
fig, ax = plt.subplots()
ax.scatter(x = denmark['rank_date'],y = denmark['total_points'])
#naming axis
plt.ylabel('Points', fontsize=13)
plt.xlabel('Year', fontsize=13)
#this is a nice feature to add a title
plt.title('DENMARK: Points over time')
#pl.show removes extra text above
plt.show()


# In[22]:


#inversely coorelated (eye test), this makes perfect sense. more points = a better (lower) ranking


# In[23]:


#lets look at correlations in the denmark dataset
denmark.corr()


# In[24]:


#is the denamrk data above similar to FIFA as a whole?
fifa_data.corr()

#after running the correlation is very similar with denmark having greater inverse corelation thatn FIFA overall


# In[25]:


#lets try another country, italy
#this will create a unique dataframe with only italy data since rankings began in 2011
italy = fifa_data.loc[fifa_data['country_full'] == 'Italy']


# In[26]:


#I want to see the italy data
italy


# In[27]:


#lets look at rank over time for italy using our plotranktime function
plotranktime(italy)


# # Data set number 2:  .XLS

# In[28]:


#this is data on the LA bike sharking program


# In[29]:


excel_file = '/Users/tclawson/Desktop/labike.xls'
labike = pd.read_excel(excel_file)


# In[30]:


#Here we can see the basic information regarding the dataset
labike.head()


# In[31]:


labike.describe()
#this will provide us with basic summary statistics


# In[32]:


#This helps us understand the dimensions of our table, with the first number representing rows
labike.shape


# In[33]:


#I want to know what the most popular type of passholder is
labike["Passholder Type"].value_counts()


# In[34]:


#lets make a function for what we just accomplished
def new_df_valuecount(variable):
    return labike[variable].value_counts()
    


# In[38]:


#lets try running the new function
new_df_valuecount("Passholder Type")


# In[40]:


#now lets use the new function to create a new dataframe for the passholder counts
passholdertype_df=new_df_valuecount("Passholder Type")
passholdertype_df


# In[41]:


#lets visualize the types of passholders in a histogram
passholdertype_df.plot(kind="bar")
plt.title("Passholder Breakdown")
plt.show()


# In[42]:


#lets make a function that creates a histogram
def histvis(file):
    file.plot(kind="bar")
    plt.show()


# In[43]:


#running the new visulaization function we created
histvis(passholdertype_df)


# In[44]:


#I'm interested in which starting station is the most popular, lets create a unique dataframe with the counts 

location_df=new_df_valuecount("Starting Station ID")
location_df


# In[45]:


#lets visualize the locations, 
#while we can't read the x axis we understand that certain stations are much mre popular than others. 
histvis(location_df)


# In[47]:


#I want to know if short or long rides are more poular
duration_df=new_df_valuecount("Duration")
duration_df

#by running this we clealry see that short bike rides are the most popular,(between 120 and 1200 seconds, (2 and 20 minutes)


# In[48]:


histvis(duration_df)


# In[49]:


#lets clean out the outliers and understand themost common times people ride
duration_df = duration_df.drop(duration_df[(duration_df['Duration']<1201)].index)

# This will not run because the duration_df is not a dataframe with headers, I need to leanr how to create that and/or give this headers to better interpret


# In[54]:


labike = labike.drop(labike[(labike['Duration']<1201)].index)


# In[55]:


duration1_df=new_df_valuecount("Duration")
duration1_df


# In[52]:


histvis(duration1_df)


# # Data Set 3 (SQLite)
# 

# In[56]:


#LEts start by importing a SQL PAckage
import sqlite3


# In[57]:


#I need to connect this package to the database
conn=sqlite3.connect("/Users/tclawson/Desktop/database.sqlite")


# In[58]:


#the salries command pulls a table from the SQL database
salary_df = pd.read_sql("select * from Salaries;", con=conn)

salary_df


# In[59]:


#lets dive deeper into the data with summary statistics
salary_df.describe()


# In[60]:


#it looks like there is negative and zero pay. lets learn more about that
#how many people are recieving negative or zero salary

salary_df["TotalPay"].value_counts()

#we see there are 368 people not being paid!


# In[61]:


#knowing this I want to remove all data thta resuts in zero pay, and anything less than a living wage of $30,000

salary_df = salary_df.drop(salary_df[(salary_df['TotalPay']<30000)].index)


# In[62]:


#what does the data look like now that we've removed lower wages?
#lets take a look again with summary stats
salary_df.describe()


# In[63]:


#mean total pay has increased from 74k toalmost 94k, interesting, lets visualize, maybe there are high outliers as well


# In[64]:


sns.distplot(salary_df.TotalPay, kde=False, bins=100)


# In[65]:


# i want to see a visualization of where most of the data is, I'll use the box plot function
sns.boxplot(salary_df.TotalPay)


# In[66]:


#seeing this graph, I am thinking maybe the cuttoff at 30 thousand was too much, 
#and everything above 275K is too big to include
#lets reimport the data and reclean, removing all data with less than 0 and over 275k

salary_df = pd.read_sql("select * from Salaries;", con=conn)

salary_df


# In[67]:


salary_df = salary_df.drop(salary_df[(salary_df['TotalPay']<0)].index)
salary_df = salary_df.drop(salary_df[(salary_df['TotalPay']>275000)].index)


# In[68]:


sns.distplot(salary_df.TotalPay, kde=False, bins=100)


# In[69]:


# i want to see a visualization of where most of the data is, I'll use the box plot function
sns.boxplot(salary_df.TotalPay)
#Between roughly30 and 110K


# In[70]:


#Now that we can more accurately see the data, lets remove the data before the first dip at
#25k and remove after the visual fall at 250k
#we'll start by reimporting then removing
salary_df = pd.read_sql("select * from Salaries;", con=conn)

salary_df = salary_df.drop(salary_df[(salary_df['TotalPay']<25000)].index)
salary_df = salary_df.drop(salary_df[(salary_df['TotalPay']>250000)].index)


# In[71]:


sns.distplot(salary_df.TotalPay, kde=False, bins=100)


# In[72]:


#setting KDE to true draws a line of best fit with the data
sns.distplot(salary_df.TotalPay, kde=True, bins=100)


# In[73]:


#this final box plot shows where most of the data fits
sns.boxplot(salary_df.TotalPay)


# In[74]:


#My question is, have wages gone up over time?
#Lets look for a simple correlation
salary_df.corr()


# In[380]:


#Benefits correlate drastically to total pay, and year correlates to total pay and totalpaybenefits
#Lets see if we can see any slope on a line using the salary data with respect to time
sns.lmplot(x="Year", y="TotalPay", data=salary_df)


# In[ ]:


#while this is not super helpful, we see an overall up trend in total pay year over year. 
#I would like to run a regression but do not know how to yet

