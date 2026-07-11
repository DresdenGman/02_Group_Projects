#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#1-dataimportprocessing" data-toc-modified-id="1-dataimportprocessing-1">1 dataimportprocessing</a></span><ul class="toc-item"><li><span><a href="#1.1-dataimport" data-toc-modified-id="1.1-dataimport-1.1">1.1 dataimport</a></span></li><li><span><a href="#1.2-data" data-toc-modified-id="1.2-data-1.2">1.2 data</a></span></li><li><span><a href="#1.3-Data Preprocessing" data-toc-modified-id="1.3-Data Preprocessing-1.3">1.3 Data Preprocessing</a></span></li></ul></li><li><span><a href="#2-Sentimentanalysis" data-toc-modified-id="2-Sentimentanalysis-2">2 Sentimentanalysis</a></span><ul class="toc-item"><li><span><a href="#2.1-Sentimentminute" data-toc-modified-id="2.1-Sentimentminute-2.1">2.1 Sentimentminute</a></span></li><li><span><a href="#2.2-Sentimentminute" data-toc-modified-id="2.2-Sentimentminute-2.2">2.2 Sentimentminute</a></span></li><li><span><a href="#2.3-" data-toc-modified-id="2.3--2.3">2.3 </a></span></li><li><span><a href="#2.4-Keywordsextract" data-toc-modified-id="2.4-Keywordsextract-2.4">2.4 Keywordsextract</a></span></li></ul></li><li><span><a href="#3-ReviewReview" data-toc-modified-id="3-ReviewReview-3">3 ReviewReview</a></span><ul class="toc-item"><li><span><a href="#3.1-ReviewReviewShare" data-toc-modified-id="3.1-ReviewReviewShare-3.1">3.1 ReviewReviewShare</a></span></li><li><span><a href="#3.2-Reviewanalysis" data-toc-modified-id="3.2-Reviewanalysis-3.2">3.2 Reviewanalysis</a></span></li></ul></li><li><span><a href="#" data-toc-modified-id="-4"></a></span></li></ul></div>

# # 1 dataimportprocessing

# ## 1.1 dataimport

# In[1]:


import pandas as pd
data = pd.read_csv('./JD.comReviewdata.csv')
data.head(2)


# ## 1.2 data
# 

# In[2]:


data.describe()


# ## 1.3 Data Preprocessing

# In[3]:


#sku_id','content'
data1 = data[['sku_id','content']]
data1.head(10)


# # 2 Sentimentanalysis

# ## 2.1 Sentimentminute

# In[4]:


#snownlp
get_ipython().system('pip install snownlp  -i https://pypi.tuna.tsinghua.edu.cn/simple')


# In[5]:


from snownlp import SnowNLP
data1['emotion'] = data1['content'].apply(lambda x:SnowNLP(x).sentiments)
data1.head(10)


# In[6]:


data1.describe()


# * emotionmean0.74，0.96，25%minute0.56，25%data。

# ## 2.2 Sentimentminute

# In[7]:


#Sentimentminute
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

bins=np.arange(0,1.1,0.1)
plt.hist(data1['emotion'],bins,color='#4F94CD',alpha=0.9)
plt.xlim(0,1)
plt.xlabel('Sentimentminute')
plt.ylabel('Count')
plt.title('Sentimentminute')

plt.show()


# * ，Reviewminute；
# 
# * 3637Review2200ReviewSentimentminute[0.9，1]；hour，500ReviewSentimentminute[0，0.1]。

# ## 2.3 

# In[8]:


from wordcloud import WordCloud
import jieba
w = WordCloud()
text = ''
for s in data['content']:
    text += s
data_cut = ' '.join(jieba.lcut(text))

w = WordCloud(font_path="./SimHei.ttf",
                      stopwords=['','','','',' and ','','',''],  # 
                      #max_words=100,
                      width=2000,
                      height=1200).generate(data_cut)
# save
w.to_file('.png')
# file
plt.imshow(w)
plt.axis("off")
plt.show()


# ## 2.4 Keywordsextract

# In[9]:


#Keywordstop10
from jieba import analyse 
key_words = jieba.analyse.extract_tags(sentence=text, topK=10, withWeight=True, allowPOS=())
key_words


# * Keywords，Consumptioncompare“”“”“”，“”“”Brand。

# # 3 ReviewReview

# ## 3.1 ReviewReviewShare

# In[10]:


#calculateReviewReview
pos = 0
neg = 0
for i in data1['emotion']:
    if i >= 0.5:
        pos += 1
    else:
        neg += 1
print('Review，Revieware:：',pos,neg)


# In[11]:


# ReviewShare
import matplotlib.pyplot as plt 

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

pie_labels='postive','negative'
plt.pie([pos,neg],labels=pie_labels,autopct='%1.1f%%',shadow=True)

plt.show()


# ## 3.2 Reviewanalysis

# In[12]:


#Reviewdata
data2=data1[data1['emotion']<0.5]
data2.head(10)


# In[13]:


#Review
text2 = ''
for s in data2['content']:
    text2 += s
data_cut2 = ' '.join(jieba.lcut(text2))
w.generate(data_cut2)
image = w.to_file('Review.png')

# file
plt.imshow(w)
plt.axis("off")
plt.show()


# In[14]:


#ReviewKeywordstop10
key_words = jieba.analyse.extract_tags(sentence=text2, topK=10, withWeight=True, allowPOS=())
key_words


# * ReviewKeywords，“”“”“”user； and may ；
# 
# *  therefore ，；，， and 。

# # Summary

# using jieba，snownlp，wordcloud，matplotlibdataSentimentanalysisvisualization，userusing ，。
