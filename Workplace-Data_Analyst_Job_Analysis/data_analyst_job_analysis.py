#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Project Introduction" data-toc-modified-id="Project Introduction-1">Project Introduction</a></span><ul class="toc-item"><li><span><a href="#Keywords" data-toc-modified-id="Keywords-1.1">Keywords</a></span></li></ul></li><li><span><a href="#1.-" data-toc-modified-id="1.--2">1. </a></span></li><li><span><a href="#2.-viewdata" data-toc-modified-id="2.-viewdata-3">2. viewdata</a></span></li><li><span><a href="#3.-Data Explorationanalysis" data-toc-modified-id="3.-Data Explorationanalysis-4">3. Data Explorationanalysis</a></span><ul class="toc-item"><li><span><a href="#3.1.-different Data Analysis" data-toc-modified-id="3.1.-different Data Analysis-4.1">3.1. different Data Analysis</a></span></li><li><span><a href="#3.2.-different Data AnalysisPosition" data-toc-modified-id="3.2.-different Data AnalysisPosition-4.2">3.2. different Data AnalysisPosition</a></span></li><li><span><a href="#3.3.-Data Analysisyear" data-toc-modified-id="3.3.-Data Analysisyear-4.3">3.3. Data Analysisyear</a></span></li><li><span><a href="#3.4.-Data Analysis" data-toc-modified-id="3.4.-Data Analysis-4.4">3.4. Data Analysis</a></span></li><li><span><a href="#3.5.-Data AnalysisDistribution" data-toc-modified-id="3.5.-Data AnalysisDistribution-4.5">3.5. Data AnalysisDistribution</a></span></li><li><span><a href="#3.6.-" data-toc-modified-id="3.6.--4.6">3.6. </a></span></li><li><span><a href="#3.7.-" data-toc-modified-id="3.7.--4.7">3.7. </a></span></li><li><span><a href="#3.8.-" data-toc-modified-id="3.8.--4.8">3.8. </a></span></li><li><span><a href="#3.9.-Keywords" data-toc-modified-id="3.9.-Keywords-4.9">3.9. Keywords</a></span></li></ul></li><li><span><a href="#4.analysis" data-toc-modified-id="4.analysis-5">4.analysis</a></span></li></ul></div>

# ###  Project Introduction
# using 437Recruitmentinfo，analysisData AnalysisPosition，Data Analysis。
# 
# #### Keywords
# - Data Explorationanalysis、matplotlibvisualization、minute、

# ### 1. 

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import jieba
import jieba.analyse
import re
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
# from matplotlib.font_manager import FontProperties
import pprint
# jupyter
get_ipython().run_line_magic('matplotlib', 'inline')
# 
plt.rcParams["font.sans-serif"] = 'SimHei'
# 
plt.rcParams['axes.unicode_minus'] = False
# import matplotlib as mpl
# info
import warnings
warnings.filterwarnings('ignore')


# ### 2. viewdata

# In[3]:


data = pd.read_csv('./lagou.csv')


# In[4]:


data.head()


# In[5]:


data.info()


# In[6]:


data.describe()


# ### 3. Data Explorationanalysis
# （、Salary、year、、、、）analysis，analysisData AnalysisDistribution、SalaryDistribution。
# #### 3.1. different Data Analysis

# In[7]:


plt.figure(figsize = (8,6))
data['address'].value_counts().sort_values(ascending=False).plot.bar(width = 0.8,color = 'steelblue')
plt.ylabel('Count')
plt.xlabel('')
plt.title('different Distribution')
plt.grid(False)


# In[8]:


plt.figure(figsize = (8,6))
data['address'].value_counts().sort_values(ascending = False).plot.bar(width = 0.8,color = 'blue')
plt.xlabel('')
plt.ylabel('Count')
plt.title('different Data AnalysisCount')
plt.grid(False)


# ：，（ e.g., 、）， and compare，minute。descriptionData Analysis， therefore 、、。

# #### 3.2. different Data AnalysisPosition

# In[9]:


# has ，
clean_foursquare = [str(i.split(',')[0]) for i in data.foursquare]
data['foursquare'] = clean_foursquare


# In[10]:


plt.figure(figsize = (8,6))
data['foursquare'].value_counts().sort_values(ascending = True).plot.barh(width = 0.8,color = 'red')
plt.xlabel('Count')
plt.ylabel('')
plt.title('different Data AnalysisCount')
plt.grid(False)


# ：analysisPositionmain ， additionally ，Data AnalysisPosition e.g., 、E-commerce、、Consumption，Share，。
# 
# #### 3.3. Data Analysisyear

# In[11]:


plt.figure(figsize = (8,6))
data['experience'].value_counts().plot.barh(width = 0.6,color = 'orange')
plt.xlabel('Count')
plt.ylabel('')
plt.title('Data Analysis',loc = "center")
plt.grid(False)


# ：minuteneed to （Employee，time），3year，。
# #### 3.4. Data Analysis

# In[12]:


education_count = data['education'].value_counts()
labels='','','',''
colors=[ 'lightskyblue', 'gold','yellowgreen', 'lightcoral']
explode=(0.1,0.1,0.1,0.1)
plt.axis('equal')
plt.title('Data Analysis',size = 15)
plt.pie(education_count,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',
        shadow=True,labeldistance=1.1,startangle=60,radius=1.2)


# ：，Data AnalysisPosition，minute， because Data AnalysisPositionbasic and ，algorithm， so Data AnalysisPosition。
# 
# #### 3.5. Data AnalysisDistribution

# In[13]:


# 'k''K'
clean_salary = [re.sub('[k|K]','',i) for i in data.salary]

# salarydataDataFrame
salary = pd.DataFrame(clean_salary,columns = ['salary'])
salary_s = pd.DataFrame((x.split('-') for x in salary['salary']),columns = ['bottomSalary','topSalary'])
# 
salary_s['bottomSalary']=salary_s['bottomSalary'].astype(np.int)
salary_s['topSalary']=salary_s['topSalary'].astype(np.int)

# calculatemean
salary_avg = [(salary_s['bottomSalary'][i] + salary_s['topSalary'][i])/2 for i in range(len(salary_s))]
salary_s['avgSalary'] = salary_avg
# for i in range(len(salary_s)):
#     avg.append((salary_s['bottomSalary'][i]+salary_s['topSalary'][i])/2)
# salary_s['avgSalary']=avg

# salary_s
data = pd.merge(data,salary_s,right_index=True,left_index=True)
data.head()


# In[14]:


plt.figure(figsize = (8,6))
plt.hist(data['avgSalary'],bins=16,color='green')
plt.axis('tight') 
plt.title('Distribution')
plt.xlabel('month（unit：K/month）')
plt.ylabel('Count')
plt.grid(False)


# ：Data AnalysisDistributionmain  6K-25K ，20K，Position40K，，。
# #### 3.6. 

# In[15]:


data['figure'] = data['figure'].map(str.strip)
data.groupby(['figure']).count()

size1=data.loc[data['figure'] == '15-50',['figure','avgSalary']]
size2=data.loc[data['figure'] == '50-150',['figure','avgSalary']]
size3=data.loc[data['figure'] == '150-500',['figure','avgSalary']]
size4=data.loc[data['figure'] == '500-2000',['figure','avgSalary']]
size5=data.loc[data['figure'] == '2000',['figure','avgSalary']]

plt.figure(figsize = (20,8))
plt.xlabel('')
plt.ylabel('（K/month）')
plt.title('')
plt.grid(False)
plt.boxplot((size1['avgSalary'],size2['avgSalary'],size3['avgSalary'],size4['avgSalary'],size5['avgSalary']),
            labels=('15-50','50-150','150-500','500-2000','2000'))
# plt.grid(color='#95a5a6',linestyle='--',linewidth=0.8,axis='y',alpha=0.4)


# ：，，。（2000） although compare， but 。
# #### 3.7. 

# In[16]:


data['experience'] = data['experience'].map(str.strip)

#  and 1year
for i in range(len(data['experience'])):
    if data['experience'][i] in ['','']:
        data['experience'][i]='1year'
# data['experience']


# In[17]:


year1=data.loc[data['experience'] == '1year',['experience','avgSalary']]
year2=data.loc[data['experience'] == '1-3year',['experience','avgSalary']]
year3=data.loc[data['experience'] == '3-5year',['experience','avgSalary']]
year4=data.loc[data['experience'] == '5-10year',['experience','avgSalary']]

plt.figure(figsize = (20,8))
plt.xlabel('year')
plt.ylabel('（K/month）')
plt.title('year')
plt.grid(False)
# plt.grid(color='#95a5a6',linestyle='--',linewidth=0.8,axis='y',alpha=0.4)
plt.boxplot((year1['avgSalary'],year2['avgSalary'],year3['avgSalary'],year4['avgSalary']),
            labels=('1year','1-3year','3-5year','5-10year'))


# ：，Salary，3yearbasic 22K。1year，1year1-3year，、，！
# #### 3.8. 

# In[18]:


data['education']=data['education'].map(str.strip)
 
edu1=data.loc[data['education'] == '',['education','avgSalary']]
edu2=data.loc[data['education'] == '',['education','avgSalary']]
edu3=data.loc[data['education'] == '',['education','avgSalary']]
edu4=data.loc[data['education'] == '',['education','avgSalary']]

plt.figure(figsize = (20,8))
plt.xlabel('')
plt.ylabel('（K/month）')
plt.title('')
plt.grid(False)
# plt.grid(color='#95a5a6',linestyle='--',linewidth=0.8,axis='y',alpha=0.4)
plt.boxplot((edu1['avgSalary'],edu2['avgSalary'],edu3['avgSalary'],edu4['avgSalary']),labels=('','','',''))


# ：different ，。where ，， because minute；，yeartime。
# #### 3.9. Keywords

# In[19]:


# Positionsavefile
description_text = ' '.join([i for i in data['description']])

with open('des.txt','w',encoding = 'utf-8') as f:
    f.write(description_text)
    f.close()


# In[20]:


text = open('des.txt', 'r',encoding='utf-8').read()
stop_word = ['Position','','','Position','','','','',
             '','Position1','','','1','1','','calculate','Data Analysis',
             'and','to','with','the','in','for','of']
wordcloud = WordCloud(font_path="./SimHei.ttf",
                      stopwords=stop_word,  # 
                      max_words=100,
                      width=2000,
                      height=1200).generate(text)
# save
wordcloud.to_file('DT.jpg')
# file
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# ：，Data Analysis，、SQL、Python、Excel，data、， because data。  ，Data Analysis：SQL，Python，，data，Excel， SAS，SPSS, Hadoop，
# ### 4.analysis
# through analysis，as follows：
# 
#  a、Data AnalysisPositionmain 、，，（basic 8K），（），，1-3year。
#  
# b、Data AnalysisDistributionmain ，（ e.g., 、Education）。
# 
#  c、Data Analysis：SQL，Python，，data，Excel， SAS，SPSS, Hadoop，，where 、SQL、Python、Excel。
#  
# d、、data。
