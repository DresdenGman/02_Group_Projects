#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#项目介绍" data-toc-modified-id="项目介绍-1">项目介绍</a></span></li><li><span><a href="#1.数据检查与理解" data-toc-modified-id="1.数据检查与理解-2">1.数据检查与理解</a></span><ul class="toc-item"><li><span><a href="#1.1.-检查是否存在缺失值" data-toc-modified-id="1.1.-检查是否存在缺失值-2.1">1.1. 检查是否存在缺失值</a></span></li><li><span><a href="#1.2.-适当的改名来更直观的理解和获取特征列" data-toc-modified-id="1.2.-适当的改名来更直观的理解和获取特征列-2.2">1.2. 适当的改名来更直观的理解和获取特征列</a></span></li><li><span><a href="#1.3.-查看数据的信息" data-toc-modified-id="1.3.-查看数据的信息-2.3">1.3. 查看数据的信息</a></span></li><li><span><a href="#1.4.-展示所有类型特征的信息" data-toc-modified-id="1.4.-展示所有类型特征的信息-2.4">1.4. 展示所有类型特征的信息</a></span></li><li><span><a href="#1.5.-类别数字化" data-toc-modified-id="1.5.-类别数字化-2.5">1.5. 类别数字化</a></span></li><li><span><a href="#1.6.-改变columns的顺序" data-toc-modified-id="1.6.-改变columns的顺序-2.6">1.6. 改变columns的顺序</a></span></li></ul></li><li><span><a href="#2.数据探索与分析" data-toc-modified-id="2.数据探索与分析-3">2.数据探索与分析</a></span><ul class="toc-item"><li><span><a href="#2.1.-描述性分析" data-toc-modified-id="2.1.-描述性分析-3.1">2.1. 描述性分析</a></span></li><li><span><a href="#2.2.-相关性分析" data-toc-modified-id="2.2.-相关性分析-3.2">2.2. 相关性分析</a></span></li><li><span><a href="#2.3.变量分析" data-toc-modified-id="2.3.变量分析-3.3">2.3.变量分析</a></span><ul class="toc-item"><li><span><a href="#2.3.1.-公司当前员工离职与在职的比率" data-toc-modified-id="2.3.1.-公司当前员工离职与在职的比率-3.3.1">2.3.1. 公司当前员工离职与在职的比率</a></span></li><li><span><a href="#2.3.2.-公司员工的满意度与入职年份的关系" data-toc-modified-id="2.3.2.-公司员工的满意度与入职年份的关系-3.3.2">2.3.2. 公司员工的满意度与入职年份的关系</a></span></li><li><span><a href="#2.3.3.-公司各部门的员工离职与在职情况对比" data-toc-modified-id="2.3.3.-公司各部门的员工离职与在职情况对比-3.3.3">2.3.3. 公司各部门的员工离职与在职情况对比</a></span></li><li><span><a href="#2.3.4.-公司各部门的员工的工资水平" data-toc-modified-id="2.3.4.-公司各部门的员工的工资水平-3.3.4">2.3.4. 公司各部门的员工的工资水平</a></span></li><li><span><a href="#2.3.5-员工薪资与离职率" data-toc-modified-id="2.3.5-员工薪资与离职率-3.3.5">2.3.5 员工薪资与离职率</a></span></li><li><span><a href="#2.3.6.-员工过去5年的升职情况与离职对比" data-toc-modified-id="2.3.6.-员工过去5年的升职情况与离职对比-3.3.6">2.3.6. 员工过去5年的升职情况与离职对比</a></span></li><li><span><a href="#2.3.7.-员工绩效与离职的对比" data-toc-modified-id="2.3.7.-员工绩效与离职的对比-3.3.7">2.3.7. 员工绩效与离职的对比</a></span></li></ul></li></ul></li><li><span><a href="#3.总结" data-toc-modified-id="3.总结-4">3.总结</a></span><ul class="toc-item"><li><span><a href="#3.1.-离职原因分析" data-toc-modified-id="3.1.-离职原因分析-4.1">3.1. 离职原因分析</a></span></li><li><span><a href="#3.2.-公司需要思考🤔的问题" data-toc-modified-id="3.2.-公司需要思考🤔的问题-4.2">3.2. 公司需要思考🤔的问题</a></span></li></ul></li><li><span><a href="#参考" data-toc-modified-id="参考-5">参考</a></span></li></ul></div>

# ## 项目介绍
# 
# - 背景说明  
# 
# 人力资源分析数据集汇聚了对大量员工的信息数据统计，包括企业因素（如部门）、员工行为相关因素（如参与过项目数、每月工作时长、薪资水平等）、以及工作相关因素（如绩效评估、工伤事故）
# 
# - 数据说明
# 
# 文件HR_comma_sep.csv中包含10个字段，具体信息如下：
# 
# |No|	属性|	数据类型|	字段描述|
# |--|--|--|--|
# |1|	satisfaction_level|	Float	|员工满意程度：0-不满意，1-满意|
# |2|	last_evaluation|	Float|	国家|
# |3| number_project|	Integer|	在职期间完成的项目数量|
# |4	|average_montly_hours|	Integer|	每月平均工作时长（hr）|
# |5	|time_spend_company|	Integer	工龄（年）|
# |6|	work_accident|	Integer|	是否有工伤：0-没有，1-有|
# |7|	left|	Integer|	是否离职：0-在职，1-离职|
# |8|	promotion_last_5years|	Integer|	过去5年是否有升职：0-没有，1-有|
# |9|	sales|	String|	工作部门|
# |10|	salary|	String|	工资的相对等级|
# 
# - 数据来源
# 
# https://www.kaggle.com/mizanhadi/hr-employee-data-visualisation/data?select=HR_comma_sep.csv
# 
# 本篇notebook会通过描述性分析、相关性分析、变量之间的对比分析来解析影响公司员工离职的因素。以及公司应该思考和解决的问题。

# 安装包

# In[29]:


get_ipython().system('pip install plotly  -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn')


# In[3]:


get_ipython().system('pip install colorlover -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn')


# 导入需要的包

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


# ## 1.数据检查与理解

# In[2]:


colors = ['#e43620', '#f16d30','#d99a6c','#fed976', '#b3cb95', '#41bfb3','#229bac', '#256894']
data = pd.read_csv('./HR_comma_sep.csv')

data.head()


# In[3]:


print("共有",data.shape[0],"条员工记录，",data.shape[1],"个员工特征。")


# ### 1.1. 检查是否存在缺失值

# In[4]:


data.isnull().sum()


# ### 1.2. 适当的改名来更直观的理解和获取特征列

# In[5]:


df = data.rename(columns = {"sales":"department","promotion_last_5years":"promotion","Work_accident":"work_accident"})
df.columns


# ### 1.3. 查看数据的信息

# In[6]:


df.info()


# ### 1.4. 展示所有类型特征的信息

# In[7]:


df.describe(include=['O'])


# ### 1.5. 类别数字化
# 1. 先设置`salary`与`department`列为**Category**的数据类型
# 2. 保存类别与对应数值的映射字典
# 3. 针对`salary`和`department`这两个`Object`类型的**类别**特征，将其进行类别数字化。

# In[8]:


# 1. 先设置`salary`与`department`列为**Category**的数据类型
df['department'] = df['department'].astype('category')#, categories=cat.categories)
df['salary'] = df['salary'].astype('category')#, categories=cat.categories)


# In[9]:


df.info()


# In[10]:


# 保存类别
# department_categories = pd.Categorical(df['department']).categories
# salary_categories = pd.Categorical(df['salary']).categories


# In[11]:


# 2. 保存类别与对应数值的映射字典
salary_dict = dict(enumerate(df['salary'].cat.categories))
department_dict = dict(enumerate(df['department'].cat.categories))
salary_dict,department_dict


# In[12]:


# 3. 针对`salary`和`department`这两个`Object`类型的类别特征，将其进行类别数字化。
for feature in df.columns:
    if str(df[feature].dtype) == 'category':
        df[feature] = df[feature].cat.codes
        # df[feature] = pd.Categorical(df[feature]).codes
        df[feature] = df[feature].astype("int64") # 设置数据类型为int64


# In[13]:


df.head()


# ### 1.6. 改变columns的顺序
# 1.先设置columns的顺序
# 	- 将`left`列放置于最后一列以便直观地查看
# 2.根据排好的列表顺序应用于dataframe上

# In[14]:


cols = df.columns
cols = list(cols[:6]) + list(cols[7:]) + [cols[6]]
print('Reordered Columns:',cols)


# In[15]:


# 根据排好的列表顺序应用于dataframe上
df = df[cols]
df.head()


# In[16]:


print(df.shape)
df.info()


# ## 2.数据探索与分析
# 

# ### 2.1. 描述性分析
# **对`left`**列进行Group，进行描述性分析[[1]](https://zhuanlan.zhihu.com/p/30282012)
# 查看在职与离职类别下，每个特征的均值

# In[17]:


left_summary = df.groupby(by=['left'])
left_summary.mean()


# In[18]:


df.describe()


# ### 2.2. 相关性分析
# 根据热力图显示，可以发现：
# 
# - `满意度(satisfaction_level）`
# 	- 员工**满意度**（satisfaction_level）离职（left）呈较大**负相关**（-）关系，与**完成项目数**（number_project）、**在公司的年份**（time_spend_company）也有一定的负相关性。
# - `绩效评估(last_evaluation)`
# 	- 上一次的**绩效评估**(last_evaluation)与**完成项目数**（number_project）和**平均每月工作时间**（average_montly_hours）这两个特征呈较大的**正相关**（+）关系,也就是说，完成项目数越多，平均每月工作时长越长，员工能获得更高的评价。
# 	- 但绩效评估与工资，晋升都没有什么相关性，所以员工得到了高绩效评价也不会升职或者涨工资。
# - `离职（left）`
# 	- 离职率与员工**满意度**（satisfaction_level）、过去5年是否有**晋升**（promotion_last_5years）、是否有**工伤**（work_accident）、**工资薪酬**（salary）呈**负相关**（-）关系。如果员工对公司不太满意，且个人价值实现不高，那么离职的可能性会很大。
# 	- 离职率与员工的**在公司的年份**（time_spend_company）呈较大**正相关**（+）关系。与**平均每月工作时间**（average_montly_hours），所在**部门**（department）也呈些许正相关性。

# In[19]:


corr = df.corr()                 # pearson相关系数
mask = np.zeros_like(corr)
mask[np.tril_indices_from(mask)]=True


# In[20]:


with sns.axes_style("white"):
    sns.set(rc={'figure.figsize':(11,7)})
    ax = sns.heatmap(corr, 
                xticklabels=True, yticklabels=True, 
                cmap='RdBu', # cmap='YlGnBu',  # 颜色
                mask=mask,   # 使用掩码只绘制矩阵的一部分
                fmt='.3f',     # 格式设置
                annot=True,    # 方格内写入数据
                linewidths=.5, # 热力图矩阵之间的间隔大小
                vmax=.4,       # 图例中最大值
                square = True
                # center = 0
                )

plt.title("Correlation")
label_x = ax.get_xticklabels()
plt.setp(label_x,rotation=45, horizontalalignment='right')
plt.show()


# ### 2.3.变量分析
# #### 2.3.1. 公司当前员工离职与在职的比率

# In[21]:


left_count = df['left'].value_counts().reset_index(name = "left_count")


# In[25]:


df = df.fillna('')


# In[27]:


trace = Pie(labels = ['在职','离职'], values = left_count.left_count,
            hoverinfo = "label + percent + name",
            marker = dict(colors = colors[3:]), hole = .6, pull = .1)
layout = Layout(title = "员工在职与离职的比率", width = 380, height = 380)
iplot(Figure(data = [trace], layout = layout))


# #### 2.3.2. 公司员工的满意度与入职年份的关系

# In[28]:


time_mean_satifaction = df.groupby(by = ['time_spend_company'])['satisfaction_level'].mean().reset_index(name = "average_satisfaction") # 取满意度的均值的


# In[29]:


trace = Bar(x=time_mean_satifaction.time_spend_company, y=time_mean_satifaction.average_satisfaction, marker=dict(color = colors),)
layout = Layout(title= "员工满意度与公司在职时间有什么关联？",
                width = 700, height = 400,
                xaxis = dict(title="在公司时间（年）"),
                yaxis = dict(title = "平均满意度"),
                )
iplot(Figure(data=[trace],layout= layout))


# #### 2.3.3. 公司各部门的员工离职与在职情况对比
# 可以看出，sales部门的离职人数最多，有1014人，其次是technical技术部门离职697人。

# In[30]:


depart_left_table = pd.crosstab(index=df['department'],columns=df['left'])


# In[31]:


data = []
left_eles = df.left.unique()
for l in left_eles:
    trace = Bar(x = depart_left_table[l], y = depart_left_table.index, name=('离职' if l == 1 else '在职'),orientation='h',marker=dict(color=colors[l+4]))
    data.append(trace)
layout = Layout(title="每个部门的离职员工数与在职员工数对比", barmode="stack",width=800,height=500,yaxis=dict(title="部门",tickmode="array",tickvals=list(department_dict.keys()),ticktext=list(department_dict.values())))
iplot(Figure(data= data, layout=layout))


# #### 2.3.4. 公司各部门的员工的工资水平
# 销售部门（sales）低工资水平（low salary）的最多，有2099人,其次是技术部门(technical)与后勤部门(support),分别为1372人与1146人。
# 

# In[32]:


depart_salary_table = pd.crosstab(index=df['department'], columns=df['salary'])
# depart_salary_table


# In[33]:


data = []
for i in range(3):
    trace = Bar(x=depart_salary_table.index, y=depart_salary_table[i],name=salary_dict[i],marker=dict(color=colors[i+2]))
    data.append(trace)
layout = Layout(title="公司各部门的员工工资情况",width=800,height=450,xaxis = dict(tickmode="array",tickvals=list(department_dict.keys()),ticktext=list(department_dict.values())))
iplot(Figure(data = data,layout = layout))


# #### 2.3.5 员工薪资与离职率
# 低薪与中等薪资的员工离职率偏高分别是42%，26%，高薪员工只用7%的离职率。

# In[34]:


salary_left_table=pd.crosstab(index=df['salary'],columns=df['left'])


# In[35]:


data = []
for i in range(2):
    trace = Bar(x=salary_left_table.index, y=salary_left_table[i],name=("在职" if i ==0 else "离职"),marker=dict(color=colors[i+4]))
    data.append(trace)
layout = Layout(title="员工薪资对离职的影响",width=580,height=350,xaxis = dict(tickmode="array",tickvals=list(salary_dict.keys()),ticktext=list(salary_dict.values())))
iplot(Figure(data = data,layout = layout))


# #### 2.3.6. 员工过去5年的升职情况与离职对比
# 过去5年都没有升过职的员工离职率相比升过职的要高出很多。升过职的员工94%都在职。

# In[36]:


promotion_left_table=pd.crosstab(index=df['promotion'],columns=df['left'])


# In[37]:


promotion_dict = {0:"没有升职",1:"升过职"}
data = []
for i in range(2):
    trace = Bar(x=promotion_left_table.index, y=promotion_left_table[i],name=("在职" if i ==0 else "离职"),marker=dict(color=colors[i+4]))
    data.append(trace)
layout = Layout(title="员工过去5年是否升职对离职的影响",width=400,height=350,xaxis = dict(tickmode="array",tickvals=list(promotion_dict.keys()),ticktext=list(promotion_dict.values())))
iplot(Figure(data = data,layout = layout))


# #### 2.3.7. 员工绩效与离职的对比
# 离职员工不乏很多获得高度评价的

# In[38]:


eva_left_table = pd.crosstab(index=df['last_evaluation'], columns=df['left'])


# In[39]:


data = []
for i in range(2):
    trace = Bar(x=eva_left_table.index, y=eva_left_table[i],name=("在职" if i ==0 else "离职"),marker=dict(color=colors[i+4]))
    data.append(trace)
layout = Layout(title="员工的绩效评估对离职的影响",width=1000,height=400,)#xaxis = dict(tickmode="array",tickvals=list(promotion_dict.keys()),ticktext=list(promotion_dict.values())))
iplot(Figure(data = data,layout = layout))


# ## 3.总结
# 
# ### 3.1. 离职原因分析
# 
# 根据上面的👆分析，总的来看，**离职员工的特征**有以下几点：
# 
# - 对公司**满意度低**；
# - 平均**每天工作时长**为10.4个小时（按一个月每周工作5天来计算），工作劳累；
# - **薪资**大多为中低水平；
# - 过去5年基本**没有升过职**；
# - 离职员工大部分来自**销售**、**技术**与**后勤**部门，销售部门占主要；
# - 员工离职**并不是单纯的因为绩效不好**，相反，有一大半的离职员工的绩效评价都很高，在0.8-1之间都存在。结合之前相关性分析的发现，高绩效并不会带来升职和加薪，这也从侧面说明了为什么许多获得高评价的员工也会离职的原因。
# 
# **所以，公司里大部分员工离职是因为满意度低、工资低、个人价值实现得不到满足。**
# 
# ### 3.2. 公司需要思考🤔的问题
# - 为什么获得高绩效评价的员工离职率也很高？甚至评价最高的离职员工数有170多人？为什么这部分员工等不到升职与加薪？
# - 为什么销售部门的离职员工最多？
# - 为什么员工对公司的满意度低？
# 
# 公司应该为员工创造一个良好的工作氛围，待遇与职业发展，更大限度的让员工实现自身的价值，从而更好的留住员工。

# ## 参考
# 
# [[1]https://www.kaggle.com/mizanhadi/hr-employee-data-visualisation](https://www.kaggle.com/mizanhadi/hr-employee-data-visualisation)

# In[ ]:




