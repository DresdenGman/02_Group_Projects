#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Project Introduction" data-toc-modified-id="Project Introduction-1">Project Introduction</a></span></li><li><span><a href="#1.data" data-toc-modified-id="1.data-2">1.data</a></span><ul class="toc-item"><li><span><a href="#1.1.-has missing values" data-toc-modified-id="1.1.-has missing values-2.1">1.1. has missing values</a></span></li><li><span><a href="#1.2.- and feature" data-toc-modified-id="1.2.- and feature-2.2">1.2.  and feature</a></span></li><li><span><a href="#1.3.-viewdatainfo" data-toc-modified-id="1.3.-viewdatainfo-2.3">1.3. viewdatainfo</a></span></li><li><span><a href="#1.4.-featureinfo" data-toc-modified-id="1.4.-featureinfo-2.4">1.4. featureinfo</a></span></li><li><span><a href="#1.5.-" data-toc-modified-id="1.5.--2.5">1.5. </a></span></li><li><span><a href="#1.6.-columns" data-toc-modified-id="1.6.-columns-2.6">1.6. columns</a></span></li></ul></li><li><span><a href="#2.Data Explorationanalysis" data-toc-modified-id="2.Data Explorationanalysis-3">2.Data Explorationanalysis</a></span><ul class="toc-item"><li><span><a href="#2.1.-analysis" data-toc-modified-id="2.1.-analysis-3.1">2.1. analysis</a></span></li><li><span><a href="#2.2.-Correlationanalysis" data-toc-modified-id="2.2.-Correlationanalysis-3.2">2.2. Correlationanalysis</a></span></li><li><span><a href="#2.3.variableanalysis" data-toc-modified-id="2.3.variableanalysis-3.3">2.3.variableanalysis</a></span><ul class="toc-item"><li><span><a href="#2.3.1.-EmployeeTurnover" data-toc-modified-id="2.3.1.-EmployeeTurnover-3.3.1">2.3.1. EmployeeTurnover</a></span></li><li><span><a href="#2.3.2.-EmployeeYear" data-toc-modified-id="2.3.2.-EmployeeYear-3.3.2">2.3.2. EmployeeYear</a></span></li><li><span><a href="#2.3.3.-EmployeeTurnover" data-toc-modified-id="2.3.3.-EmployeeTurnover-3.3.3">2.3.3. EmployeeTurnover</a></span></li><li><span><a href="#2.3.4.-Employee" data-toc-modified-id="2.3.4.-Employee-3.3.4">2.3.4. Employee</a></span></li><li><span><a href="#2.3.5-EmployeeSalaryTurnover" data-toc-modified-id="2.3.5-EmployeeSalaryTurnover-3.3.5">2.3.5 EmployeeSalaryTurnover</a></span></li><li><span><a href="#2.3.6.-Employee5yearTurnover" data-toc-modified-id="2.3.6.-Employee5yearTurnover-3.3.6">2.3.6. Employee5yearTurnover</a></span></li><li><span><a href="#2.3.7.-EmployeeTurnover" data-toc-modified-id="2.3.7.-EmployeeTurnover-3.3.7">2.3.7. EmployeeTurnover</a></span></li></ul></li></ul></li><li><span><a href="#3." data-toc-modified-id="3.-4">3.</a></span><ul class="toc-item"><li><span><a href="#3.1.-Turnoveranalysis" data-toc-modified-id="3.1.-Turnoveranalysis-4.1">3.1. Turnoveranalysis</a></span></li><li><span><a href="#3.2.-need to 🤔" data-toc-modified-id="3.2.-need to 🤔-4.2">3.2. need to 🤔</a></span></li></ul></li><li><span><a href="#" data-toc-modified-id="-5"></a></span></li></ul></div>

# ## Project Introduction
# 
# - description  
# 
# analysisdatasetEmployeeinfodata，including （）、Employeerelated （、monthhour、Salary）、and related （evaluation、）
# 
# - datadescription
# 
# fileHR_comma_sep.csvcontains10，specific infoas follows：
# 
# |No|	attribute|	data|	|
# |--|--|--|--|
# |1|	satisfaction_level|	Float	|Employee：0-，1-|
# |2|	last_evaluation|	Float|	|
# |3| number_project|	Integer|	Count|
# |4	|average_montly_hours|	Integer|	monthhour（hr）|
# |5	|time_spend_company|	Integer	（year）|
# |6|	work_accident|	Integer|	：0-，1-|
# |7|	left|	Integer|	Turnover：0-，1-Turnover|
# |8|	promotion_last_5years|	Integer|	5year：0-，1-|
# |9|	sales|	String|	|
# |10|	salary|	String|	|
# 
# - data
# 
# https://www.kaggle.com/mizanhadi/hr-employee-data-visualisation/data?select=HR_comma_sep.csv
# 
# notebookthrough analysis、Correlationanalysis、variableanalysisEmployeeTurnover。and  and 。

# 

# In[29]:


get_ipython().system('pip install plotly  -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn')


# In[3]:


get_ipython().system('pip install colorlover -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn')


# importneed to 

# In[1]:


import pandas as pd
import numpy as np

from plotly import __version__
print (__version__)

from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
from plotly.graph_objs import *
import colorlover as cl

import matplotlib.pyplot as plt
import seaborn as sns


# ## 1.data

# In[2]:


colors = ['#e43620', '#f16d30','#d99a6c','#fed976', '#b3cb95', '#41bfb3','#229bac', '#256894']
data = pd.read_csv('./HR_comma_sep.csv')

data.head()


# In[3]:


print("",data.shape[0],"Employeerecord，",data.shape[1],"Employeefeature。")


# ### 1.1. has missing values

# In[4]:


data.isnull().sum()


# ### 1.2.  and feature

# In[5]:


df = data.rename(columns = {"sales":"department","promotion_last_5years":"promotion","Work_accident":"work_accident"})
df.columns


# ### 1.3. viewdatainfo

# In[6]:


df.info()


# ### 1.4. featureinfo

# In[7]:


df.describe(include=['O'])


# ### 1.5. 
# 1. `salary``department`**Category**data
# 2. save
# 3. targeting `salary` and `department``Object`****feature，。

# In[8]:


# 1. `salary``department`**Category**data
df['department'] = df['department'].astype('category')#, categories=cat.categories)
df['salary'] = df['salary'].astype('category')#, categories=cat.categories)


# In[9]:


df.info()


# In[10]:


# save
# department_categories = pd.Categorical(df['department']).categories
# salary_categories = pd.Categorical(df['salary']).categories


# In[11]:


# 2. save
salary_dict = dict(enumerate(df['salary'].cat.categories))
department_dict = dict(enumerate(df['department'].cat.categories))
salary_dict,department_dict


# In[12]:


# 3. targeting `salary` and `department``Object`feature，。
for feature in df.columns:
    if str(df[feature].dtype) == 'category':
        df[feature] = df[feature].cat.codes
        # df[feature] = pd.Categorical(df[feature]).codes
        df[feature] = df[feature].astype("int64") # dataint64


# In[13]:


df.head()


# ### 1.6. columns
# 1.columns
# 	- `left`view
# 2.based on dataframe

# In[14]:


cols = df.columns
cols = list(cols[:6]) + list(cols[7:]) + [cols[6]]
print('Reordered Columns:',cols)


# In[15]:


# based on dataframe
df = df[cols]
df.head()


# In[16]:


print(df.shape)
df.info()


# ## 2.Data Explorationanalysis
# 

# ### 2.1. analysis
# **`left`**Group，analysis[[1]](https://zhuanlan.zhihu.com/p/30282012)
# viewTurnover，feature

# In[17]:


left_summary = df.groupby(by=['left'])
left_summary.mean()


# In[18]:


df.describe()


# ### 2.2. Correlationanalysis
# based on ，：
# 
# - `(satisfaction_level）`
# 	- Employee****（satisfaction_level）Turnover（left）**related **（-），****（number_project）、**Year**（time_spend_company）Correlation。
# - `evaluation(last_evaluation)`
# 	- **evaluation**(last_evaluation)****（number_project） and **monthtime**（average_montly_hours）feature**related **（+）,，，monthhour，EmployeeAssessment。
# 	- evaluation，Correlation， so EmployeeAssessment。
# - `Turnover（left）`
# 	- TurnoverEmployee****（satisfaction_level）、5year****（promotion_last_5years）、****（work_accident）、****（salary）**related **（-）。 if Employee，implement ，Turnover。
# 	- TurnoverEmployee**Year**（time_spend_company）**related **（+）。**monthtime**（average_montly_hours），****（department）Correlation。

# In[19]:


corr = df.corr()                 # pearsonrelated 
mask = np.zeros_like(corr)
mask[np.tril_indices_from(mask)]=True


# In[20]:


with sns.axes_style("white"):
    sns.set(rc={'figure.figsize':(11,7)})
    ax = sns.heatmap(corr, 
                xticklabels=True, yticklabels=True, 
                cmap='RdBu', # cmap='YlGnBu',  # Color
                mask=mask,   # using minute
                fmt='.3f',     # 
                annot=True,    # data
                linewidths=.5, # 
                vmax=.4,       # max
                square = True
                # center = 0
                )

plt.title("Correlation")
label_x = ax.get_xticklabels()
plt.setp(label_x,rotation=45, horizontalalignment='right')
plt.show()


# ### 2.3.variableanalysis
# #### 2.3.1. EmployeeTurnover

# In[21]:


left_count = df['left'].value_counts().reset_index(name = "left_count")


# In[25]:


df = df.fillna('')


# In[27]:


trace = Pie(labels = ['','Turnover'], values = left_count.left_count,
            hoverinfo = "label + percent + name",
            marker = dict(colors = colors[3:]), hole = .6, pull = .1)
layout = Layout(title = "EmployeeTurnover", width = 380, height = 380)
iplot(Figure(data = [trace], layout = layout))


# #### 2.3.2. EmployeeYear

# In[28]:


time_mean_satifaction = df.groupby(by = ['time_spend_company'])['satisfaction_level'].mean().reset_index(name = "average_satisfaction") # 


# In[29]:


trace = Bar(x=time_mean_satifaction.time_spend_company, y=time_mean_satifaction.average_satisfaction, marker=dict(color = colors),)
layout = Layout(title= "Employeetime？",
                width = 700, height = 400,
                xaxis = dict(title="time（year）"),
                yaxis = dict(title = ""),
                )
iplot(Figure(data=[trace],layout= layout))


# #### 2.3.3. EmployeeTurnover
# We can see ，salesTurnover，1014，technicalTurnover697。

# In[30]:


depart_left_table = pd.crosstab(index=df['department'],columns=df['left'])


# In[31]:


data = []
left_eles = df.left.unique()
for l in left_eles:
    trace = Bar(x = depart_left_table[l], y = depart_left_table.index, name=('Turnover' if l == 1 else ''),orientation='h',marker=dict(color=colors[l+4]))
    data.append(trace)
layout = Layout(title="TurnoverEmployeeEmployee", barmode="stack",width=800,height=500,yaxis=dict(title="",tickmode="array",tickvals=list(department_dict.keys()),ticktext=list(department_dict.values())))
iplot(Figure(data= data, layout=layout))


# #### 2.3.4. Employee
# Sales（sales）（low salary），2099,(technical)(support),respectively13721146。
# 

# In[32]:


depart_salary_table = pd.crosstab(index=df['department'], columns=df['salary'])
# depart_salary_table


# In[33]:


data = []
for i in range(3):
    trace = Bar(x=depart_salary_table.index, y=depart_salary_table[i],name=salary_dict[i],marker=dict(color=colors[i+2]))
    data.append(trace)
layout = Layout(title="Employee",width=800,height=450,xaxis = dict(tickmode="array",tickvals=list(department_dict.keys()),ticktext=list(department_dict.values())))
iplot(Figure(data = data,layout = layout))


# #### 2.3.5 EmployeeSalaryTurnover
# SalaryEmployeeTurnoverrespectively42%，26%，Employee7%Turnover。

# In[34]:


salary_left_table=pd.crosstab(index=df['salary'],columns=df['left'])


# In[35]:


data = []
for i in range(2):
    trace = Bar(x=salary_left_table.index, y=salary_left_table[i],name=("" if i ==0 else "Turnover"),marker=dict(color=colors[i+4]))
    data.append(trace)
layout = Layout(title="EmployeeSalaryTurnover",width=580,height=350,xaxis = dict(tickmode="array",tickvals=list(salary_dict.keys()),ticktext=list(salary_dict.values())))
iplot(Figure(data = data,layout = layout))


# #### 2.3.6. Employee5yearTurnover
# 5yearEmployeeTurnover。Employee94%。

# In[36]:


promotion_left_table=pd.crosstab(index=df['promotion'],columns=df['left'])


# In[37]:


promotion_dict = {0:"",1:""}
data = []
for i in range(2):
    trace = Bar(x=promotion_left_table.index, y=promotion_left_table[i],name=("" if i ==0 else "Turnover"),marker=dict(color=colors[i+4]))
    data.append(trace)
layout = Layout(title="Employee5yearTurnover",width=400,height=350,xaxis = dict(tickmode="array",tickvals=list(promotion_dict.keys()),ticktext=list(promotion_dict.values())))
iplot(Figure(data = data,layout = layout))


# #### 2.3.7. EmployeeTurnover
# TurnoverEmployeeAssessment

# In[38]:


eva_left_table = pd.crosstab(index=df['last_evaluation'], columns=df['left'])


# In[39]:


data = []
for i in range(2):
    trace = Bar(x=eva_left_table.index, y=eva_left_table[i],name=("" if i ==0 else "Turnover"),marker=dict(color=colors[i+4]))
    data.append(trace)
layout = Layout(title="EmployeeevaluationTurnover",width=1000,height=400,)#xaxis = dict(tickmode="array",tickvals=list(promotion_dict.keys()),ticktext=list(promotion_dict.values())))
iplot(Figure(data = data,layout = layout))


# ## 3.
# 
# ### 3.1. Turnoveranalysis
# 
# based on 👆analysis，，**TurnoverEmployeefeature**：
# 
# - ****；
# - **dayshour**10.4hour（month5dayscalculate），；
# - **Salary**；
# - 5yearbasic ****；
# - TurnoverEmployeeminute**Sales**、********，Salesmain ；
# - EmployeeTurnover** because **，，TurnoverEmployeeAssessment，0.8-1has 。Correlationanalysis， and ，descriptionAssessmentEmployeeTurnover。
# 
# ** so ，minuteEmployeeTurnover because 、、implement 。**
# 
# ### 3.2. need to 🤔
# - AssessmentEmployeeTurnover？AssessmentTurnoverEmployee170？minuteEmployee？
# - SalesTurnoverEmployee？
# - Employee？
# 
# Employee，，Employeeimplement ，Employee。

# ## 
# 
# [[1]https://www.kaggle.com/mizanhadi/hr-employee-data-visualisation](https://www.kaggle.com/mizanhadi/hr-employee-data-visualisation)

# In[ ]:




