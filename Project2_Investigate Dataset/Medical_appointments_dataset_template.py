#!/usr/bin/env python
# coding: utf-8

# # Medical appointments dataset
# 
# ## Table of Contents
# 
# - [Introduction](#Introduction)
# - [Data Wrangling](#Wrangling)
# - [Exploratory & Visualisation](#Exploratory)
# - [COMMENTS/Limitations](#COMMENTS)
# - [Conclusions](#Conclusions)

# <a id='Introduction'></a>
# # Introduction :
# 
# > I will analysis  the data set of medical appointments to find out what category is taking appointments frequently, is it the category of men or women, and what are the ages, etc. At the beginning, I will download the data after that I will work to clean the data set(Data Wrangling) after that visualization and conclusion.
# 
#  **There are many questions that we will discuss, solved, and touch in our analysis:**
# *  Q1:What is the most gender(M / F) in taking appointments?
# *  Q2: How many people have received a text message and who have not received a text message?
# *  Q3: How many have a scholarship?
# *  Q4: How many have alcohol addiction?
# *  Q5: How many have diabetes?
# *  Q6: What are the most ages that take an appointment?
# *  Q7: What is the more gender who received a message and did not received a message?
# *  Q8: What is the more gender who has a scholarship?
# *  Q9: What are the ages and gender that are taking more than in appointments?
# *  Q10: Who is the gender M / F who shows up for his appointment who doesn't show up for his appointment?
# *  Q11: What is the gender most Injured by diabetes?

# <a id='Wrangling'></a>
# # Data Wrangling

# ## Gathering 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Read dataset of medical appointments
df_appointments=pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
df_appointments.head()


# In[3]:


df_appointments.sample(50)


# ## Assessing

# In[4]:


#display the dataset of medical appointments 
df_appointments.sample(100)


# In[5]:


#display information of dataset  medical appointments 
df_appointments.info()


# In[6]:


#display describe of dataset  medical appointments 
df_appointments.describe()


# In[7]:


#display the data type  of column in dataset  medical appointments 
df_appointments.dtypes


# In[8]:


#display if there null value  in column of dataset  medical appointments 
df_appointments.isnull().sum()


# In[33]:


#display if there is duplicate  value  in column of dataset  medical appointments 
sum(df_appointments.duplicated())
df_appointments['Alcoholism'].value_counts()


# 
# ## Cleaning 

# In[10]:


# Chaning the data type of some column of dataset  medical appointments 

# Chaning the data type of PatientId column to integer 
df_appointments['PatientId']=df_appointments['PatientId'].astype(int)
# Chaning the data type of ScheduledDay column to datetime
df_appointments['ScheduledDay']=pd.to_datetime(df_appointments['ScheduledDay'])
# Chaning the data type of AppointmentDay column to datetime 
df_appointments['AppointmentDay']=pd.to_datetime(df_appointments['AppointmentDay'])


# In[11]:


#Create Chaning_datatype function to convert any data type to category type
def Chaning_datatype(new_name):
 df_appointments[new_name]=df_appointments[new_name].astype('category')

# Chaning the data type of Gander column to category beacuse there is to value just M oR F
Chaning_datatype('Gender')
#Chaning the data type of Scholarship column to category beacuse there is to value just 0==No oR 1==yes
Chaning_datatype('Scholarship')

#Chaning the data type of Hipertension column to category beacuse there is to value just 0==No oR 1==yes
Chaning_datatype('Hipertension')

# Chaning the data type of SMS_received column to category beacuse there is to value just 0==No oR 1==yes
Chaning_datatype('SMS_received')

# Chaning the data type of Alcoholism column to category beacuse there is to value just 0==No oR 1==yes
Chaning_datatype('Alcoholism')

# Chaning the data type of Diabetes column to category beacuse there is to value just 0==No oR 1==yes
Chaning_datatype('Diabetes')


# In[12]:


#Test
#display the data type  of column in dataset  medical appointments 
df_appointments.dtypes


# In[13]:


# Rename (Replace)value name in column 
# Create Replace_Name function to Rename (Replace)value name in column
def Replace_Name(col_name,old_name,new_name,old_name2,new_name2):
  
  df_appointments[col_name] = df_appointments[col_name].replace([old_name],new_name)
  df_appointments[col_name] = df_appointments[col_name].replace([old_name2],new_name2)

#Rename a value in SMS_received column to 0=No_received, 1=Yes_received
Replace_Name('SMS_received',0,'No_received',1,'Yes_received') 

#Rename a value in Scholarship  column to 0=Don’t_have_Scholarship , 1=Have_Scholarship
Replace_Name('Scholarship',0,'Don’t_have_Scholarship',1,'Have_Scholarship') 

#Rename a value in Hipertension   column to 0=Normal, 1=High
Replace_Name('Hipertension',0,'Normal',1,'High') 

#Rename a value in Diabetes column to 0=UnInjured, 1=Injured
Replace_Name('Diabetes',0,'UnInjured',1,'Injured') 

#Rename a value in Alcoholism column to 0=Unaddicted, 1=Addicted
Replace_Name('Alcoholism',0,'Unaddicted',1,'Addicted') 


# In[14]:


#Test
df_appointments.head(50)


# In[15]:


#Dropping Columns
# Drop columns I won't use  
df_appointments.drop(columns=["AppointmentID","ScheduledDay","AppointmentDay","Neighbourhood","Hipertension","Handcap"],axis=1,inplace=True)


# In[16]:


#Test 
df_appointments.columns


# 
# **Create a copy from  data set cleand**

# In[17]:


#We finish from clean data stage, now the data set (df_appointments)has a ready for go to next stage 
# But we should take a clean  copy from data set(df_appointments)
df_appointments_clean=df_appointments.copy()


# <a id='Exploratory'></a>
# # Exploratory & Visualisation 

# **Q1:What is the most gender(M / F) in taking appointments?**

# In[18]:


# We will discover who is taking the most appointments by bar chart 
plt.figure(figsize = [9, 6])
sn.countplot(data= df_appointments_clean, x='Gender',alpha=1,linewidth=5,palette="Blues");
plt.grid(axis='y', alpha=0.10)
plt.yticks(rotation = 45)
plt.title(" The most taking appointments M/F ", fontsize=20)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('Gender',fontsize=18);


# The difference is quite clear; females(7000 Patient) take more appointments than men(4000 Patient) 

# **Q2: How many people have received a text message and who have not received a text message?**

# In[19]:


# We will discover who is received a text message and who have not received a text message by bar chart
plt.figure(figsize = [9, 6])
sn.countplot(data= df_appointments_clean, x='SMS_received', alpha=1,palette="BuGn");
plt.grid(axis='y', alpha=0.10)
plt.title(" The number of SMS received and Not received", fontsize=20)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('SMS received',fontsize=18);


# the number of who is not received(7000 Patient) a text message is more than received (3500 Patient) 

# **Q3: How many have a scholarship?**

# In[20]:


#We will discover How many have a scholarship by bar chart 
plt.figure(figsize = [9, 6])
sn.countplot(data= df_appointments_clean, x='Scholarship', alpha=1,palette="winter_r");
plt.grid(axis='y', alpha=0.10)
plt.title(" The number of have scholarship and Not have", fontsize=20)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('Scholarship',fontsize=18);


# The graphic shows that the number of have a scholarship recipients is small(1500 Patient)  compared to the number Don’t have  a scholarship(9000 Patient) 

# **Q4: How many have alcohol addiction?**

# In[21]:


#We will discover How many have alcohol addiction  by bar chart
plt.figure(figsize = [9, 6])
sn.countplot(data= df_appointments_clean, x='Alcoholism', alpha=1,palette="Blues");
plt.grid(axis='y', alpha=0.10)
plt.title(" The number of have alcohol and Not have ", fontsize=20)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('Alcoholism',fontsize=18);


# It is clear from the drawing that the number of alcoholics is very small(1000 Patient)  compared to the number of non-alcoholics(100000 Patient) 

# **Q5: How many have diabetes?**

# In[22]:


#We will discover How many have diabetes  by bar chart 
plt.figure(figsize = [9, 6])
sn.countplot(data= df_appointments_clean, x='Diabetes', alpha=1,palette="winter_r");
plt.grid(axis='y', alpha=0.10)
plt.title(" The number of have diabetes and Not have ", fontsize=20)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('diabetes',fontsize=18);


# The drawing shows that the number of diabetics is very small (1000 Patient)  compared to the number of non-diabetics(100000 Patient) 

# **Q6: What are the most ages that take an appointment?**

# In[23]:


#We will discover What are the most ages that take an appointment by histogram ?
plt.figure(figsize = [11, 8])
plt.hist(data= df_appointments_clean, x='Age', rwidth=1);
plt.title(" The most ages that take an appointment ", fontsize=20)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('Ages',fontsize=18);


# We notice through the drawing that the number of people of all ages is similar in taking appointments, but ages from one year to 10 years old (18000 Patient)  were the most in taking appointments

# **Q7: What is the more gender who received  a message and  did not  received a message?**

# In[24]:


# We will discover What is the more gender who received  a message and  did not  received a message
plt.figure(figsize = [9, 6])
sn.countplot(data=df_appointments_clean, x='Gender', hue='SMS_received',alpha=1);
plt.grid(axis='y', alpha=0.10)
plt.title(" SMS received Vs Gender ", fontsize=20)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('Gender',fontsize=18);


# Through the drawing, we notice that the number of females exceeds the number of men in taking appointments
# But we care about who receives the message and who does not receive the message, and the result is that the number of those who receive the message and those who do not receive the message are  very close  and the same in both genders.

# **Q8: What is the more gender who has a scholarship?**

# In[25]:


# We will discover What is the more gender who has a scholarship
plt.figure(figsize = [9, 6])
sn.countplot(data=df_appointments_clean, x='Gender', hue='Scholarship',alpha=1,palette="winter_r");
plt.grid(axis='y', alpha=0.10)
plt.title(" The more gender who has a scholarship", fontsize=25)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('Gender',fontsize=18);


# The result was that females (10000 Patient)  have more scholarships than men (5000 Patient) 

# **Q9: What are the ages and gender that are taking more than in appointments?**

# In[26]:


# We will discover What are the ages and gender that are taking more than in appointments
plt.figure(figsize = [14, 8])
some_Ages=df_appointments_clean.query('Age<=25')
sn.countplot(data=some_Ages, x=some_Ages.Age, hue='Gender',alpha=1);
plt.grid(axis='y', alpha=0.10)
plt.title(" Age Vs Gender taking appointments ", fontsize=25)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('Age',fontsize=18);


# At the beginning of ages, the number of taking appointments in both genders was very close, but with Progress in age ,  the number of females taking appointments was higher than men.

# **Q10: Who is the gender M / F who shows up for his appointment who doesn't show up for his appointment?**

# In[27]:


df_appointments_clean['No-show'].unique()


# In[28]:


# We will discover What is the more gender who received  a message and  did not  received a message
plt.figure(figsize = [9, 6])
sn.countplot(data=df_appointments_clean, x='Gender' , hue='No-show',alpha=1);
plt.grid(axis='y', alpha=0.10)
plt.title(" No-show Vs Gender ", fontsize=20)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('Gender',fontsize=18);


# We notice from the drawing that most of the females do not attend their appointments, as their number reaches 55 thousand, and few of them are the ones who bring us to their appointments as their number reaches 15,000, and the number of men who do not attend their appointments is 30,000 and those who attend to their appointments 10,000.

# **Q11: What is the gender most Injured by diabetes?**

# In[29]:


# We will discover What is the gender most Injured by diabetes
plt.figure(figsize = [9, 6])
sn.countplot(data=df_appointments_clean, x='Gender' , hue='Diabetes',alpha=1,palette="winter_r");
plt.grid(axis='y', alpha=0.10)
plt.title("Diabetes Vs gender", fontsize=25)
plt.ylabel('Number of Patient',fontsize=18);
plt.xlabel('Gender',fontsize=18);


# Through the drawing, we can see that females are more Injured by diabetes than men

# In[30]:


# Create correlation matrix for df_appointments_clean
correlation_matrix= df_appointments_clean.corr() 
correlation_matrix 


# In[31]:


# Create correlation matrix for df_appointments_clean
sn.heatmap(correlation_matrix, annot=True)
plt.show()


# <a id='COMMENTS'></a>
# # COMMENTS/Limitations :
# 
# >The data was free of repeated values ​​and missing values, and this is a distinctive and comfortable thing, and the number of females in taking appointments was much more than men in taking appointments, but the data was not complete to me. There is no column showing the most visited sections or taking appointments from them, is it the esoteric section Or the otolaryngology department,or ect..., and also There is no column showing  indicating at what time those appointments are processed in any morning or evening period also in any month, also how to take the appointment is it from the site or the call center or by attending the center, as well The names of the values ​​were not valid for use because the meaning of the value name was unclear.
# 
# 
# 
# 
# 
# 

# <a id='conclusions'></a>
# # Conclusions :
# 
# > Finally, I analysis  the data set for taking appointments and the dataset contained several useful information such as patientID, patients ages, and patients gender. I asked several questions, and I answered those questions.
# * What is the most gender(M / F) in taking appointments?
#   * Females (7000 Patient) take more appointments than men (4000 Patient) , and the number of females more than men.
# *  How many people have received a text message and who have not received a text message?
#  * The number of who is not received(7000 Patient) a text message is more than received (3500 Patient)
# *  How many have a scholarship?
#  * The graphic shows that the number of have a scholarship recipients is small(1500 Patient) compared to the number Don’t have a scholarship(9000 Patient)
# *  How many have alcohol addiction?
#   * It is clear from the drawing that the number of alcoholics is very small(1000 Patient) compared to the number of non-alcoholics(100000 Patient)
# *  How many have diabetes?
#   * The drawing shows that the number of diabetics is very small (1000 Patient) compared to the number of non-diabetics(100000 Patient)
# *  What are the most ages that take an appointment?
#   * We notice through the drawing that the number of people of all ages is similar in taking appointments, but ages from one year to 10 years old (18000 Patient) were the most in taking appointments
# *  What is the more gender who received a message and did not received a message?
#   * Through the drawing, we notice that the number of females exceeds the number of men in taking appointments But we care about who receives the message and who does not receive the message, and the result is that the number of those who receive the message and those who do not receive the message are very close and the same in both genders.
# *  What is the more gender who has a scholarship?
#   * The result was that females (10000 Patient) have more scholarships than men (5000 Patient)
# *  What are the ages and gender that are taking more than in appointments?
#   * At the beginning of ages, the number of taking appointments in both genders was very close, but with Progress in age , the number of females taking appointments was higher than men.
# *  Who is the gender M / F who shows up for his appointment who doesn't show up for his appointment?
#   * We notice from the drawing that most of the females do not attend their appointments, as their number reaches 55 thousand, and few of them are the ones who bring us to their appointments as their number reaches 15,000, and the number of men who do not attend their appointments is 30,000 and those who attend to their appointments 10,000.
# * What is the gender most Injured by diabetes?
#   * Through the drawing, we can see that females are more Injured by diabetes than men.
