#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#项目介绍" data-toc-modified-id="项目介绍-1">项目介绍</a></span><ul class="toc-item"><li><span><a href="#关键词" data-toc-modified-id="关键词-1.1">关键词</a></span></li></ul></li><li><span><a href="#1.-导包" data-toc-modified-id="1.-导包-2">1. 导包</a></span></li><li><span><a href="#2.-读取查看数据" data-toc-modified-id="2.-读取查看数据-3">2. 读取查看数据</a></span></li><li><span><a href="#3.-数据探索分析" data-toc-modified-id="3.-数据探索分析-4">3. 数据探索分析</a></span><ul class="toc-item"><li><span><a href="#3.1.-不同区域数据分析师职位的需求情况" data-toc-modified-id="3.1.-不同区域数据分析师职位的需求情况-4.1">3.1. 不同区域数据分析师职位的需求情况</a></span></li><li><span><a href="#3.2.-不同行业数据分析师岗位的需求情况" data-toc-modified-id="3.2.-不同行业数据分析师岗位的需求情况-4.2">3.2. 不同行业数据分析师岗位的需求情况</a></span></li><li><span><a href="#3.3.-数据分析师对应聘者工作年限的要求" data-toc-modified-id="3.3.-数据分析师对应聘者工作年限的要求-4.3">3.3. 数据分析师对应聘者工作年限的要求</a></span></li><li><span><a href="#3.4.-数据分析师对求职者学历的要求" data-toc-modified-id="3.4.-数据分析师对求职者学历的要求-4.4">3.4. 数据分析师对求职者学历的要求</a></span></li><li><span><a href="#3.5.-数据分析师的薪酬范围分布" data-toc-modified-id="3.5.-数据分析师的薪酬范围分布-4.5">3.5. 数据分析师的薪酬范围分布</a></span></li><li><span><a href="#3.6.-公司规模与薪酬之间的关系" data-toc-modified-id="3.6.-公司规模与薪酬之间的关系-4.6">3.6. 公司规模与薪酬之间的关系</a></span></li><li><span><a href="#3.7.-工作经验与薪酬的关系" data-toc-modified-id="3.7.-工作经验与薪酬的关系-4.7">3.7. 工作经验与薪酬的关系</a></span></li><li><span><a href="#3.8.-学历对薪酬的影响" data-toc-modified-id="3.8.-学历对薪酬的影响-4.8">3.8. 学历对薪酬的影响</a></span></li><li><span><a href="#3.9.-职业技能关键词" data-toc-modified-id="3.9.-职业技能关键词-4.9">3.9. 职业技能关键词</a></span></li></ul></li><li><span><a href="#4.分析结论" data-toc-modified-id="4.分析结论-5">4.分析结论</a></span></li></ul></div>

# ###  项目介绍
# 使用拉钩网抓取的437条招聘信息，从多维度分析深圳数据分析岗位，了解数据分析师行业现状。
# 
# #### 关键词
# - 数据探索分析、matplotlib可视化、结巴分词、词云图

# ### 1. 导包

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
# 让图表直接在jupyter中展示出来
get_ipython().run_line_magic('matplotlib', 'inline')
# 解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
# 解决负号无法正常显示问题
plt.rcParams['axes.unicode_minus'] = False
# import matplotlib as mpl
# 关闭警告信息
import warnings
warnings.filterwarnings('ignore')


# ### 2. 读取查看数据

# In[3]:


data = pd.read_csv('./lagou.csv')


# In[4]:


data.head()


# In[5]:


data.info()


# In[6]:


data.describe()


# ### 3. 数据探索分析
# 从多维度（区域、薪资情况、工作年限、学历、所在行业、公司规模、职位要求）进行分析，分析数据分析师的区域分布、薪资分布及其各个字段之间的关联。
# #### 3.1. 不同区域数据分析师职位的需求情况

# In[7]:


plt.figure(figsize = (8,6))
data['address'].value_counts().sort_values(ascending=False).plot.bar(width = 0.8,color = 'steelblue')
plt.ylabel('职位数量')
plt.xlabel('区域')
plt.title('不同区域的职位分布')
plt.grid(False)


# In[8]:


plt.figure(figsize = (8,6))
data['address'].value_counts().sort_values(ascending = False).plot.bar(width = 0.8,color = 'blue')
plt.xlabel('区域')
plt.ylabel('职位数量')
plt.title('不同区域数据分析师职位数量')
plt.grid(False)


# 小结：不难看出南山区的需求遥遥领先于其他区，不愧是深圳互联网聚集地（比如有腾讯、中兴等），当然福田和宝安也相对是需求比较多的，其余区域很少甚至部分新区都还没有需求。这说明了数据分析师确实是一个朝阳产业，因此优先在南山、福田、宝安求职。

# #### 3.2. 不同行业数据分析师岗位的需求情况

# In[9]:


# 存在多个行业，只取第一个
clean_foursquare = [str(i.split(',')[0]) for i in data.foursquare]
data['foursquare'] = clean_foursquare


# In[10]:


plt.figure(figsize = (8,6))
data['foursquare'].value_counts().sort_values(ascending = True).plot.barh(width = 0.8,color = 'red')
plt.xlabel('职位数量')
plt.ylabel('职位名称')
plt.title('不同行业数据分析师职位数量')
plt.grid(False)


# 小结：可以发现数分析师岗位主要集中于移动互联网行业领域，此外，数据分析岗位也开始融入传统行业例如金融、电商、企业服务、消费生活等，可以预见在不久的将来这种的占比会不断增大，其发展势头不容小觑。
# 
# #### 3.3. 数据分析师对应聘者工作年限的要求

# In[11]:


plt.figure(figsize = (8,6))
data['experience'].value_counts().plot.barh(width = 0.6,color = 'orange')
plt.xlabel('职位数量')
plt.ylabel('工作经验')
plt.title('数据分析对求职者工作经验的要求',loc = "center")
plt.grid(False)


# 小结：大部分企业都是需要求职者有一定的工作经验的（谁都想招一个能直接上手的员工，而不是还要花一段时间去培养他），甚至是超过3年的工作经验，对应届生其实很不利。
# #### 3.4. 数据分析师对求职者学历的要求

# In[12]:


education_count = data['education'].value_counts()
labels='本科及以上','学历不限','硕士及以上','大专及以上'
colors=[ 'lightskyblue', 'gold','yellowgreen', 'lightcoral']
explode=(0.1,0.1,0.1,0.1)
plt.axis('equal')
plt.title('数据分析师对求职者学历的要求',size = 15)
plt.pie(education_count,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',
        shadow=True,labeldistance=1.1,startangle=60,radius=1.2)


# 小结：可以发现，数据分析师岗位对学历的要求不算太高，大部分公司要求具备本科学历即可，这是因为数据分析师岗位仅仅要求求职者具备基本的数学知识以及编程，不像算法岗要求那么高，所以对大多数人来说数据分析师还是一个不错的岗位选择。
# 
# #### 3.5. 数据分析师的薪酬范围分布

# In[13]:


# 去除字段中'k'或'K'字符
clean_salary = [re.sub('[k|K]','',i) for i in data.salary]

# 将salary数据转换为DataFrame格式
salary = pd.DataFrame(clean_salary,columns = ['salary'])
salary_s = pd.DataFrame((x.split('-') for x in salary['salary']),columns = ['bottomSalary','topSalary'])
# 更改字段格式
salary_s['bottomSalary']=salary_s['bottomSalary'].astype(np.int)
salary_s['topSalary']=salary_s['topSalary'].astype(np.int)

# 计算平均值
salary_avg = [(salary_s['bottomSalary'][i] + salary_s['topSalary'][i])/2 for i in range(len(salary_s))]
salary_s['avgSalary'] = salary_avg
# for i in range(len(salary_s)):
#     avg.append((salary_s['bottomSalary'][i]+salary_s['topSalary'][i])/2)
# salary_s['avgSalary']=avg

# 将salary_s表与原表进行拼接
data = pd.merge(data,salary_s,right_index=True,left_index=True)
data.head()


# In[14]:


plt.figure(figsize = (8,6))
plt.hist(data['avgSalary'],bins=16,color='green')
plt.axis('tight') 
plt.title('薪酬分布')
plt.xlabel('每月薪酬（单位：K/月）')
plt.ylabel('职位数量')
plt.grid(False)


# 小结：可以发现数据分析师的薪酬分布范围主要在 6K-25K 之间，尤其集中在20K左右，少量岗位甚至高达40K以上，好好干，有钱途。
# #### 3.6. 公司规模与薪酬之间的关系

# In[15]:


data['figure'] = data['figure'].map(str.strip)
data.groupby(['figure']).count()

size1=data.loc[data['figure'] == '15-50人',['figure','avgSalary']]
size2=data.loc[data['figure'] == '50-150人',['figure','avgSalary']]
size3=data.loc[data['figure'] == '150-500人',['figure','avgSalary']]
size4=data.loc[data['figure'] == '500-2000人',['figure','avgSalary']]
size5=data.loc[data['figure'] == '2000人以上',['figure','avgSalary']]

plt.figure(figsize = (20,8))
plt.xlabel('公司规模')
plt.ylabel('平均薪酬（K/月）')
plt.title('公司规模与平均薪酬')
plt.grid(False)
plt.boxplot((size1['avgSalary'],size2['avgSalary'],size3['avgSalary'],size4['avgSalary'],size5['avgSalary']),
            labels=('15-50人','50-150人','150-500人','500-2000人','2000人以上'))
# plt.grid(color='#95a5a6',linestyle='--',linewidth=0.8,axis='y',alpha=0.4)


# 小结：如箱形图所示，随着公司的规模增大，平均薪酬有明显上涨的趋势。另外大厂（2000人以上）是工资待遇虽然比较高，但是差距也大。
# #### 3.7. 工作经验与薪酬的关系

# In[16]:


data['experience'] = data['experience'].map(str.strip)

# 把经验应届毕业生和经验不限归为经验1年以下
for i in range(len(data['experience'])):
    if data['experience'][i] in ['经验应届毕业生','经验不限']:
        data['experience'][i]='经验1年以下'
# data['experience']


# In[17]:


year1=data.loc[data['experience'] == '经验1年以下',['experience','avgSalary']]
year2=data.loc[data['experience'] == '经验1-3年',['experience','avgSalary']]
year3=data.loc[data['experience'] == '经验3-5年',['experience','avgSalary']]
year4=data.loc[data['experience'] == '经验5-10年',['experience','avgSalary']]

plt.figure(figsize = (20,8))
plt.xlabel('工作年限')
plt.ylabel('薪酬（K/月）')
plt.title('工作年限与平均薪酬')
plt.grid(False)
# plt.grid(color='#95a5a6',linestyle='--',linewidth=0.8,axis='y',alpha=0.4)
plt.boxplot((year1['avgSalary'],year2['avgSalary'],year3['avgSalary'],year4['avgSalary']),
            labels=('经验1年以下','经验1-3年','经验3-5年','经验5-10年'))


# 小结：随着工作经验的增长，薪资也跟着涨，工作3年后基本都在22K以上了。不过工作经验在1年以下却有些反常，经验1年以下的薪酬甚至比经验1-3年的都高，这可能由于应届毕业生之间的能力、学历差异造成的，真的是能者多劳啊！
# #### 3.8. 学历对薪酬的影响

# In[18]:


data['education']=data['education'].map(str.strip)
 
edu1=data.loc[data['education'] == '学历不限',['education','avgSalary']]
edu2=data.loc[data['education'] == '大专及以上',['education','avgSalary']]
edu3=data.loc[data['education'] == '本科及以上',['education','avgSalary']]
edu4=data.loc[data['education'] == '硕士及以上',['education','avgSalary']]

plt.figure(figsize = (20,8))
plt.xlabel('学历')
plt.ylabel('薪酬（K/月）')
plt.title('学历与平均薪酬')
plt.grid(False)
# plt.grid(color='#95a5a6',linestyle='--',linewidth=0.8,axis='y',alpha=0.4)
plt.boxplot((edu1['avgSalary'],edu2['avgSalary'],edu3['avgSalary'],edu4['avgSalary']),labels=('学历不限','大专及以上','本科及以上','硕士及以上'))


# 小结：学历不同，工资待遇的区别还是挺明显的。其中，本科及以上学历的薪酬待遇的极差较大，这是因为大部分公司都要求求职者具备本科及以上的学历；硕士及以上则更上一层楼，好歹人家比你多花三年时间。
# #### 3.9. 职业技能关键词

# In[19]:


# 把每个岗位描述连接起来保存在文件中
description_text = ' '.join([i for i in data['description']])

with open('des.txt','w',encoding = 'utf-8') as f:
    f.write(description_text)
    f.close()


# In[20]:


text = open('des.txt', 'r',encoding='utf-8').read()
stop_word = ['岗位职责','任职要求','工作职责','岗位要求','任职资格','本科及以上学历','本科以上学历','职位描述',
             '工作职责','岗位职责1','职位诱惑','职位要求','任职要求1','工作职责1','职位职责','计算机','数据分析',
             'and','to','with','the','in','for','of']
wordcloud = WordCloud(font_path="./SimHei.ttf",
                      stopwords=stop_word,  # 去掉停用词
                      max_words=100,
                      width=2000,
                      height=1200).generate(text)
# 保存词云
wordcloud.to_file('DT.jpg')
# 显示词云文件
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# 小结：词云显示出的情况，想要从事数据分析这一职位，数学统计、SQL、Python、Excel是必备技能，还有对数据敏感、责任心强，因为数据就是你的法宝。  从词云上看出，数据分析师技能具备的频率排在前列的有：SQL，Python，数学统计，对数据敏感，Excel， SAS，SPSS, Hadoop，机器学习等
# ### 4.分析结论
# 通过上面的分析，我们可以得到如下结论：
# 
#  a、在深圳数据分析师岗位需求主要集中在南山、福田，即互联网聚集地，总体待遇较高（基本上在8K以上），学历要求不是特别高（本科以上），大厂需求量较大，大量的工作经验需求集中在1-3年。
#  
# b、数据分析师分布的行业领域主要是移动互联网行业，不过也开始向传统行业（例如金融、教育）渗透。
# 
#  c、数据分析师技能具备的频率排在前列的有：SQL，Python，数学统计，对数据敏感，Excel， SAS，SPSS, Hadoop，机器学习等，其中数学统计、SQL、Python、Excel是必备技能。
#  
# d、机器学习、大数据挖掘是走向高薪的正确方向。
