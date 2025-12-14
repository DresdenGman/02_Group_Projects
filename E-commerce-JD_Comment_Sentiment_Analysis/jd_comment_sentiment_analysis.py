#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#1-数据导入及预处理" data-toc-modified-id="1-数据导入及预处理-1">1 数据导入及预处理</a></span><ul class="toc-item"><li><span><a href="#1.1-数据导入" data-toc-modified-id="1.1-数据导入-1.1">1.1 数据导入</a></span></li><li><span><a href="#1.2-数据描述" data-toc-modified-id="1.2-数据描述-1.2">1.2 数据描述</a></span></li><li><span><a href="#1.3-数据预处理" data-toc-modified-id="1.3-数据预处理-1.3">1.3 数据预处理</a></span></li></ul></li><li><span><a href="#2-情感分析" data-toc-modified-id="2-情感分析-2">2 情感分析</a></span><ul class="toc-item"><li><span><a href="#2.1-情感分" data-toc-modified-id="2.1-情感分-2.1">2.1 情感分</a></span></li><li><span><a href="#2.2-情感分直方图" data-toc-modified-id="2.2-情感分直方图-2.2">2.2 情感分直方图</a></span></li><li><span><a href="#2.3-词云图" data-toc-modified-id="2.3-词云图-2.3">2.3 词云图</a></span></li><li><span><a href="#2.4-关键词提取" data-toc-modified-id="2.4-关键词提取-2.4">2.4 关键词提取</a></span></li></ul></li><li><span><a href="#3-积极评论与消极评论" data-toc-modified-id="3-积极评论与消极评论-3">3 积极评论与消极评论</a></span><ul class="toc-item"><li><span><a href="#3.1-积极评论与消极评论占比" data-toc-modified-id="3.1-积极评论与消极评论占比-3.1">3.1 积极评论与消极评论占比</a></span></li><li><span><a href="#3.2-消极评论分析" data-toc-modified-id="3.2-消极评论分析-3.2">3.2 消极评论分析</a></span></li></ul></li><li><span><a href="#总结" data-toc-modified-id="总结-4">总结</a></span></li></ul></div>

# # 1 数据导入及预处理

# ## 1.1 数据导入

# In[1]:


import pandas as pd
data = pd.read_csv('./京东评论数据.csv')
data.head(2)


# ## 1.2 数据描述
# 

# In[2]:


data.describe()


# ## 1.3 数据预处理

# In[3]:


#取出sku_id','content'字段
data1 = data[['sku_id','content']]
data1.head(10)


# # 2 情感分析

# ## 2.1 情感分

# In[4]:


#安装snownlp包
get_ipython().system('pip install snownlp  -i https://pypi.tuna.tsinghua.edu.cn/simple')


# In[5]:


from snownlp import SnowNLP
data1['emotion'] = data1['content'].apply(lambda x:SnowNLP(x).sentiments)
data1.head(10)


# In[6]:


data1.describe()


# * emotion平均值为0.74，中位数为0.96，25%分位数为0.56，可见不到25%的数据造成了整体均值的较大下移。

# ## 2.2 情感分直方图

# In[7]:


#情感分直方图
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

bins=np.arange(0,1.1,0.1)
plt.hist(data1['emotion'],bins,color='#4F94CD',alpha=0.9)
plt.xlim(0,1)
plt.xlabel('情感分')
plt.ylabel('数量')
plt.title('情感分直方图')

plt.show()


# * 由直方图可见，评论内容两级分化较为严重；
# 
# * 3637条评论中有约2200条评论情感分在[0.9，1]区间内；同时，有约500条评论情感分在[0，0.1]区间内。

# ## 2.3 词云图

# In[8]:


from wordcloud import WordCloud
import jieba
w = WordCloud()
text = ''
for s in data['content']:
    text += s
data_cut = ' '.join(jieba.lcut(text))

w = WordCloud(font_path="./SimHei.ttf",
                      stopwords=['的','我','了','是','和','都','就','用'],  # 去掉停用词
                      #max_words=100,
                      width=2000,
                      height=1200).generate(data_cut)
# 保存词云
w.to_file('词云图.png')
# 显示词云文件
plt.imshow(w)
plt.axis("off")
plt.show()


# ## 2.4 关键词提取

# In[9]:


#关键词top10
from jieba import analyse 
key_words = jieba.analyse.extract_tags(sentence=text, topK=10, withWeight=True, allowPOS=())
key_words


# * 以上关键词显示，消费者比较在意手机的“屏幕”“拍照”“手感”等特性，“华为”“小米”是出现频次最高的两个手机品牌。

# # 3 积极评论与消极评论

# ## 3.1 积极评论与消极评论占比

# In[10]:


#计算积极评论与消极评论各自的数目
pos = 0
neg = 0
for i in data1['emotion']:
    if i >= 0.5:
        pos += 1
    else:
        neg += 1
print('积极评论，消极评论数目分别为：',pos,neg)


# In[11]:


# 积极评论占比
import matplotlib.pyplot as plt 

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

pie_labels='postive','negative'
plt.pie([pos,neg],labels=pie_labels,autopct='%1.1f%%',shadow=True)

plt.show()


# ## 3.2 消极评论分析

# In[12]:


#获取消极评论数据
data2=data1[data1['emotion']<0.5]
data2.head(10)


# In[13]:


#消极评论词云图
text2 = ''
for s in data2['content']:
    text2 += s
data_cut2 = ' '.join(jieba.lcut(text2))
w.generate(data_cut2)
image = w.to_file('消极评论词云.png')

# 显示词云文件
plt.imshow(w)
plt.axis("off")
plt.show()


# In[14]:


#消极评论关键词top10
key_words = jieba.analyse.extract_tags(sentence=text2, topK=10, withWeight=True, allowPOS=())
key_words


# * 消极评论关键词显示，“屏幕”“快递”“充电”是造成用户体验不佳的几个重要因素；屏幕和充电问题有可能是手机不良品率过高或快递压迫；
# 
# * 因此平台应注重提高手机品控，降低不良品率；另外应设法提升发货，配送，派件的效率和质量。

# # 总结

# 本文使用jieba，snownlp，wordcloud，matplotlib等模块对文本数据进行了简要的情感分析及可视化，旨在了解用户使用体验，以此对平台运营提出优化建议。
