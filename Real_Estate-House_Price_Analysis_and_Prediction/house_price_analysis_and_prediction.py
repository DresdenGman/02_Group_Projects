#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#安装依赖包" data-toc-modified-id="安装依赖包-1">安装依赖包</a></span></li><li><span><a href="#数据清洗" data-toc-modified-id="数据清洗-2">数据清洗</a></span></li><li><span><a href="#数据可视化" data-toc-modified-id="数据可视化-3">数据可视化</a></span></li><li><span><a href="#构建房价预测模型" data-toc-modified-id="构建房价预测模型-4">构建房价预测模型</a></span><ul class="toc-item"><li><span><a href="#多特征模型训练（多元线性回归）" data-toc-modified-id="多特征模型训练（多元线性回归）-4.1">多特征模型训练（多元线性回归）</a></span></li><li><span><a href="#假设验证法选出最佳特征组合" data-toc-modified-id="假设验证法选出最佳特征组合-4.2">假设验证法选出最佳特征组合</a></span></li></ul></li><li><span><a href="#房价的预测" data-toc-modified-id="房价的预测-5">房价的预测</a></span></li></ul></div>

# ## 安装依赖包

# In[2]:


get_ipython().system('pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple/')


# ## 数据清洗

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.read_csv(r'house_information.csv') # 如果用pandas打不开数据，可以使用记事本打开把编码格式改成utf-8另存
data.head()


# In[3]:


data.drop('index',axis=1,inplace=True) # 删除index列（用del更方便）
data.head()


# In[4]:


# Series的extract支持正则匹配抽取，返回的值是字符串
data[['室','厅','卫']] = data['户型'].str.extract(r'(\d+)室(\d+)厅(\d+)卫')


# In[5]:


# 把字符串格式转化为float，并删除户型
data['室'] = data['室'].astype(float)
data['厅'] = data['厅'].astype(float)
data['卫'] = data['卫'].astype(float)
del data['户型']
data.head()


# In[6]:


# 将建筑面积后的平方米去除，并将数据类型改成浮点型
data['建筑面积'] = data['建筑面积'].map(lambda e:e.replace('平米',''))# Series中的map
data['建筑面积'] = data['建筑面积'].astype(float)
data.head()


# In[7]:


# 将单价后的元/平米去除，并将数据类型改成浮点型
data['单价'] = data['单价'].map(lambda e:e.replace(r'元/平米',''))
data['单价'] = data['单价'].astype(float)
data.head()


# In[8]:


# 将房屋总价后的万去除，并将数据类型改成浮点型
data['房屋总价'] = data['房屋总价'].map(lambda e:e.replace('万',''))
data['房屋总价'] = data['房屋总价'].astype(float)
data.head()


# In[9]:


# 使用pd.get_dummies() 量化数据
data_direction = pd.get_dummies(data['朝向'])
data_direction.head()


# In[10]:


# 使用pd.get_dummies() 量化数据
data_floor = pd.get_dummies(data['楼层'])
data_floor.head()


# In[11]:


# 使用pd.get_dummies() 量化数据
data_decoration = pd.get_dummies(data['装修'])
data_decoration.head()


# In[12]:


# 使用pd.concat矩阵拼接，axis=1：水平拼接
data = pd.concat([data,data_direction,data_floor,data_decoration],axis=1) 


# In[13]:


# 拼接后的列名
data.columns


# In[14]:


# 特征帅选
del data['小区名称']
del data['朝向']
del data['楼层']
del data['装修']
del data['东西']
del data['南北']
del data['暂无'] # 两列都删除
del data['中层'] # 多重共线性问题（线性回归）
del data['中装修']
data.columns


# In[15]:


data.head()


# In[16]:


data.info() # 发现 室厅卫中 有缺失值


# In[17]:


# 删除缺失值
data.dropna(inplace=True)
data.info()                       # 到这里数据预处理完毕


# ## 数据可视化

# In[18]:


data['建筑面积']


# In[19]:


import matplotlib.pyplot as plt
area = data['建筑面积']
price = data['房屋总价']
plt.scatter(area,price)
plt.show() # 有离群点数据，对线性分析不利，需要过滤


# In[20]:


df = data[data['建筑面积'] <=300] # 正常住宅面积小于等于300平米
area = df['建筑面积']
price = df['房屋总价']
#print(area.count()) #过滤后的数据量
plt.scatter(area,price)
plt.xlabel("area")
plt.ylabel("price")
plt.show()


# ## 构建房价预测模型

# In[21]:


# 先根据建筑面积和房屋总价训练模型（一元线性回归）
from sklearn.linear_model import LinearRegression
linear = LinearRegression()
area = np.array(area).reshape(-1,1) # 这里需要注意新版的sklearn需要将数据转换为矩阵才能进行计算
price = np.array(price).reshape(-1,1)
# 训练模型
model = linear.fit(area,price)
# 打印截距和回归系数
print(model.intercept_, model.coef_)


# In[22]:


# 线性回归可视化(数据拟合)
linear_p = model.predict(area)
plt.figure(figsize=(12,6))
plt.scatter(area,price)
plt.plot(area,linear_p,'red')
plt.xlabel("area")
plt.ylabel("price")
plt.show()


# ### 多特征模型训练（多元线性回归）

# In[23]:


cols = ['建筑面积','室', '厅', '卫', '东', '东北', '东南', '北', '南', '西',
       '西北', '西南', '低层', '高层', '毛坯', '简装修', '精装修', '豪华装修']


# In[24]:


X = df[cols]
X.head()


# In[25]:


y = df['房屋总价']
y.head()


# In[26]:


print(type(X))
print(type(y))
# 使用train_test_split进行交叉验证
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=12)
print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)


# In[27]:


# 模型训练
linear = LinearRegression()
model = linear.fit(x_train,y_train)
print(model.intercept_, model.coef_)


# In[28]:


# 模型性能评分
price_end = model.predict(x_test)
score = model.score(x_test,y_test) 
print("模型得分：",score)# 一般模型在0.6以上就表现的不错


# ### 假设验证法选出最佳特征组合

# In[29]:


# 使用假设验证法，选出最佳特征组合
cols = ['建筑面积','室', '厅', '卫', '东', '东北', '东南', '北', '南', '西',
       '西北', '西南', '低层', '高层', '毛坯', '简装修', '精装修', '豪华装修']
import statsmodels.api as sm
Y = df['房屋总价']
X = df[cols]
X_ = sm.add_constant(X) #增加一列值为1的const列，保证偏置项的正常
#print(X_)
# 使用最小平方法
result = sm.OLS(Y,X_)
# 使用fit方法进行计算
summary = result.fit()
# 调用summary2方法打印出假设验证信息（性能指标）
summary.summary2() # R-squared:模型评分 AIC：组合完越小越好


# 名词解释
# 
# - coef 回归系数
# - Std.Err 标准差
# - t 虚无假设成立时的t值
# - P>|t| 虚无假设成立时的概率值
# - [0.025,0.975] 97.5%置信估计区间
# - 要做假设性验证，首先要设置显著性标准。
# - a.假设显著性标准是0.01
# - b.推翻虚无假设的标准是p<0.01
# - c.上面的SqFt的t=9.2416，P(>5) = 0.0000 < 0.01,因此虚无假设被推翻（这里的虚无假设是SqFt对price的回归系数为0，即SqFt与price不相关）
# 
# F统计
# - 回归平方和Regression Square Sum[RSS]:依变量的变化归咎于回归模型A=sum((y-y_)^2
# - 误差平方和Error Square Sum[ESS]:依变量的变化归咎于线性模型B=sum((y-y_)^2
# - 总的平方和Total Square Sum[TSS]:依变量整体变化C=A+B
# - 回归平方平均Model Mean Square:=RSS/Regression d.f(k) k=自变量的数量
# - 误差平方平均Error Mean square:=ESS/Error d.f(n-k-1) n=观测值得数量
# - F统计F=Model Mean Square /Error Mean Square
# - F值越大越好，Prob(F-statistic)越小越好
# 
# R Square
# - 回归可以解释变量比例，可以作为自变量预测因变量准确度的指标
# - SSE(残差平方和) = sum((y-y_)^2)
# - SST(整体平方和）= sum((yi-yavg)^2
# - R^2 = 1-SEE/SST 一般要大于0.6,0.7才算好
# 
# Adjust R Square
# - R^2 = 1-SSE/SST SSE最小，推导出R^2不会递减
# - yi = b1x1 + b2x2 +...+bkxk+...增加任何一个变量都会增加R^2
# - Adj R^2 = 1-(1-R^2) * ((n-1)/(n-p-1))
# - n为总体大小，p为回归因子个数
# 
# AIC/BIC
# - AIC(The Akaike Information Criterion)= 2K + nln(SSE/n) K是参数数量，n是观察数，SSE是残差平方和。
# - AIC鼓励数据拟合的优良性，但是应该尽量避免过拟合，所以优先考虑的模型应该是AIC最小的哪一个，
# - 赤池信息量的准则是寻找可以最好的解释数据但是包含最少自由参数的模型。

# In[30]:


import itertools

list1 = [1, 2,3, 4, 5,6,7,8,9,10,11,12,13,14,15,16] #特征超过16个将发生异常
list2 = []
for i in range(1, len(list1)+1):
    iter1 = itertools.combinations(list1, i)
    list2.append(list(iter1))
#print(list2)


# In[31]:


import itertools
# 使用itertools，找出AIC最小值的特征组合作为模型训练的特征
# 寻找最小AIC值的特征组合
fileds = ['建筑面积','室', '厅', '卫', '东','北', '南', '西','低层', '高层', '毛坯', '简装修', '精装修', '豪华装修']
acis = {}
for i in range(1,len(fileds)+1):
    for virables in itertools.combinations(fileds,i): #从fileds中随机选择i个特征机型组合，返回的virables为元组类型
        x1 = sm.add_constant(df[list(virables)])
        x2 = sm.OLS(Y,x1)
        res = x2.fit()
        acis[virables] = res.aic # AIC评分越小越好


# In[32]:


from collections import Counter
# 对字典进行统计
counter = Counter(acis)
# 降序选出AIC最小的10个数，也就是最佳特征组合
counter.most_common()[-10:] 


# In[33]:


# 接下来使用AIC值最小的特征组合进行预测
col2 = ['建筑面积', '室', '厅', '东', '南', '高层', '毛坯', '精装修', '豪华装修']
X = df[col2]
y = df['房屋总价']
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=13)
linear = LinearRegression()
model = linear.fit(x_train,y_train)
model.score(x_test,y_test) # 模型性能有所提高，但是提升的不明显


# ## 房价的预测

# 现在我们可以根据给定的最佳特征组合进行预测房价

# In[34]:


# 假设我要买一套房子（想想就觉得很美），房子面积120平米，3室，1厅，南面，高层，精装修
my_house = [120,3,1,0,1,1,0,1,0] #根据col2特征
my_house = np.array(my_house).reshape(-1,1).T
#print(x_test)
model.predict(my_house)# 预测价格

