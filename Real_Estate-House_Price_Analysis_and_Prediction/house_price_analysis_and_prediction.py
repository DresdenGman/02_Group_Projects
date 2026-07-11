#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#" data-toc-modified-id="-1"></a></span></li><li><span><a href="#Data Cleaning" data-toc-modified-id="Data Cleaning-2">Data Cleaning</a></span></li><li><span><a href="#datavisualization" data-toc-modified-id="datavisualization-3">datavisualization</a></span></li><li><span><a href="#House Pricepredictionmodel" data-toc-modified-id="House Pricepredictionmodel-4">House Pricepredictionmodel</a></span><ul class="toc-item"><li><span><a href="#featuremodeltraining（regression）" data-toc-modified-id="featuremodeltraining（regression）-4.1">featuremodeltraining（regression）</a></span></li><li><span><a href="#feature" data-toc-modified-id="feature-4.2">feature</a></span></li></ul></li><li><span><a href="#House Priceprediction" data-toc-modified-id="House Priceprediction-5">House Priceprediction</a></span></li></ul></div>

# ## 

# In[2]:


get_ipython().system('pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple/')


# ## Data cleaning

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.read_csv(r'house_information.csv') #  if pandasdata，using encodingutf-8
data.head()


# In[3]:


data.drop('index',axis=1,inplace=True) # index（del）
data.head()


# In[4]:


# Seriesextract，
data[['','','']] = data['Layout'].str.extract(r'(\d+)(\d+)(\d+)')


# In[5]:


# float，Layout
data[''] = data[''].astype(float)
data[''] = data[''].astype(float)
data[''] = data[''].astype(float)
del data['Layout']
data.head()


# In[6]:


# Area，data
data['Area'] = data['Area'].map(lambda e:e.replace('',''))# Seriesmap
data['Area'] = data['Area'].astype(float)
data.head()


# In[7]:


# /，data
data[''] = data[''].map(lambda e:e.replace(r'/',''))
data[''] = data[''].astype(float)
data.head()


# In[8]:


# ，data
data[''] = data[''].map(lambda e:e.replace('',''))
data[''] = data[''].astype(float)
data.head()


# In[9]:


# using pd.get_dummies() data
data_direction = pd.get_dummies(data['Orientation'])
data_direction.head()


# In[10]:


# using pd.get_dummies() data
data_floor = pd.get_dummies(data['Floor'])
data_floor.head()


# In[11]:


# using pd.get_dummies() data
data_decoration = pd.get_dummies(data['Decoration'])
data_decoration.head()


# In[12]:


# using pd.concat，axis=1：
data = pd.concat([data,data_direction,data_floor,data_decoration],axis=1) 


# In[13]:


# 
data.columns


# In[14]:


# feature
del data['Community']
del data['Orientation']
del data['Floor']
del data['Decoration']
del data['']
del data['']
del data[''] # 
del data[''] # （regression）
del data['Decoration']
data.columns


# In[15]:


data.head()


# In[16]:


data.info() #   missing values


# In[17]:


# missing values
data.dropna(inplace=True)
data.info()                       # Data Preprocessing


# ## Data visualization

# In[18]:


data['Area']


# In[19]:


import matplotlib.pyplot as plt
area = data['Area']
price = data['']
plt.scatter(area,price)
plt.show() # data，analysis，need to 


# In[20]:


df = data[data['Area'] <=300] # Area300
area = df['Area']
price = df['']
#print(area.count()) #data
plt.scatter(area,price)
plt.xlabel("area")
plt.ylabel("price")
plt.show()


# ## House Pricepredictionmodel

# In[21]:


# based on Area and trainingmodel（regression）
from sklearn.linear_model import LinearRegression
linear = LinearRegression()
area = np.array(area).reshape(-1,1) # need to sklearnneed to datacalculate
price = np.array(price).reshape(-1,1)
# trainingmodel
model = linear.fit(area,price)
#  and regression
print(model.intercept_, model.coef_)


# In[22]:


# regressionvisualization(data)
linear_p = model.predict(area)
plt.figure(figsize=(12,6))
plt.scatter(area,price)
plt.plot(area,linear_p,'red')
plt.xlabel("area")
plt.ylabel("price")
plt.show()


# ### featuremodeltraining（regression）

# In[23]:


cols = ['Area','', '', '', '', '', '', '', '', '',
       '', '', '', '', '', 'Decoration', 'Decoration', 'Decoration']


# In[24]:


X = df[cols]
X.head()


# In[25]:


y = df['']
y.head()


# In[26]:


print(type(X))
print(type(y))
# using train_test_splitcross-validation
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=12)
print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)


# In[27]:


# Model training
linear = LinearRegression()
model = linear.fit(x_train,y_train)
print(model.intercept_, model.coef_)


# In[28]:


# modelRating
price_end = model.predict(x_test)
score = model.score(x_test,y_test) 
print("modelScore：",score)# model0.6


# ### feature

# In[29]:


# using ，feature
cols = ['Area','', '', '', '', '', '', '', '', '',
       '', '', '', '', '', 'Decoration', 'Decoration', 'Decoration']
import statsmodels.api as sm
Y = df['']
X = df[cols]
X_ = sm.add_constant(X) #1const，
#print(X_)
# using 
result = sm.OLS(Y,X_)
# using fitcalculate
summary = result.fit()
# summary2info（）
summary.summary2() # R-squared:modelRating AIC：


# 
# 
# - coef regression
# - Std.Err std
# - t hourt
# - P>|t| hour
# - [0.025,0.975] 97.5%
# - ，。
# - a.0.01
# - b.p<0.01
# - c.SqFtt=9.2416，P(>5) = 0.0000 < 0.01, therefore （SqFtpriceregression0，SqFtpricerelated ）
# 
# F
# - regression and Regression Square Sum[RSS]:variableregressionmodelA=sum((y-y_)^2
# - error and Error Square Sum[ESS]:variablemodelB=sum((y-y_)^2
# -  and Total Square Sum[TSS]:variableC=A+B
# - regressionModel Mean Square:=RSS/Regression d.f(k) k=variableCount
# - errorError Mean square:=ESS/Error d.f(n-k-1) n=Count
# - FF=Model Mean Square /Error Mean Square
# - F，Prob(F-statistic)
# 
# R Square
# - regressionvariable，variablepredictionvariableAccuracy
# - SSE( and ) = sum((y-y_)^2)
# - SST( and ）= sum((yi-yavg)^2
# - R^2 = 1-SEE/SST 0.6,0.7
# 
# Adjust R Square
# - R^2 = 1-SSE/SST SSE，R^2
# - yi = b1x1 + b2x2 +...+bkxk+...variableR^2
# - Adj R^2 = 1-(1-R^2) * ((n-1)/(n-p-1))
# - n，pregression
# 
# AIC/BIC
# - AIC(The Akaike Information Criterion)= 2K + nln(SSE/n) KparameterCount，n，SSE and 。
# - AICdata， but overfitting， so modelAIC，
# - infodata but containsparametermodel。

# In[30]:


import itertools

list1 = [1, 2,3, 4, 5,6,7,8,9,10,11,12,13,14,15,16] #feature16
list2 = []
for i in range(1, len(list1)+1):
    iter1 = itertools.combinations(list1, i)
    list2.append(list(iter1))
#print(list2)


# In[31]:


import itertools
# using itertools，AICminfeaturemodeltrainingfeature
# AICfeature
fileds = ['Area','', '', '', '','', '', '','', '', '', 'Decoration', 'Decoration', 'Decoration']
acis = {}
for i in range(1,len(fileds)+1):
    for virables in itertools.combinations(fileds,i): #filedsifeature，virables
        x1 = sm.add_constant(df[list(virables)])
        x2 = sm.OLS(Y,x1)
        res = x2.fit()
        acis[virables] = res.aic # AICRating


# In[32]:


from collections import Counter
# 
counter = Counter(acis)
# AIC10，feature
counter.most_common()[-10:] 


# In[33]:


# using AICfeatureprediction
col2 = ['Area', '', '', '', '', '', '', 'Decoration', 'Decoration']
X = df[col2]
y = df['']
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=13)
linear = LinearRegression()
model = linear.fit(x_train,y_train)
model.score(x_test,y_test) # model， but 


# ## House Priceprediction

# based on featurepredictionHouse Price

# In[34]:


# （），Area120，3，1，，，Decoration
my_house = [120,3,1,0,1,1,0,1,0] #based on col2feature
my_house = np.array(my_house).reshape(-1,1).T
#print(x_test)
model.predict(my_house)# predictionPrice

