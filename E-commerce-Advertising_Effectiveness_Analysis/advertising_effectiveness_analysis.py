#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Project Introduction" data-toc-modified-id="Project Introduction-1">Project Introduction</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#data" data-toc-modified-id="data-1.0.1">data</a></span></li><li><span><a href="#data13" data-toc-modified-id="data13-1.0.2">data13</a></span></li></ul></li></ul></li><li><span><a href="#import，data" data-toc-modified-id="import，data-2">import，data</a></span><ul class="toc-item"><li><span><a href="#data" data-toc-modified-id="data-2.1">data</a></span></li></ul></li><li><span><a href="#dataprocessing" data-toc-modified-id="dataprocessing-3">dataprocessing</a></span></li><li><span><a href="#model" data-toc-modified-id="model-4">model</a></span></li><li><span><a href="#clusteringresultfeatureanalysis" data-toc-modified-id="clusteringresultfeatureanalysis-5">clusteringresultfeatureanalysis</a></span></li><li><span><a href="#data" data-toc-modified-id="data-6">data</a></span></li></ul></div>

# ## Project Introduction

# PlacementAdvertisingChannel，Channelcustomermay different ， e.g., Advertising and dayPlacementAdvertising，Effectivenessmay 。need to AdvertisingEffectivenessanalysisimplement targeting AdvertisingEffectiveness and 。
# 
# ，through AdvertisingChannel90daysdayUV，、、、hour、Order、Placementtime、、Advertising、、Advertising and Advertisingfeature，Channelclassification，Channelfeature， and Data Analysis。

# ####  data
# 
# Channel，12，889，missing values，。
# 
# #### data13
# 
# 1、Channel：Channel  
# 2、dayUV：days  
# 3、=dayuser/day  
# 4、：  
# 5、：/days  
# 6、hour=hour/days  
# 7、Order=OrderCount/days  
# 8、Placementtime：AdvertisingPlacementdays  
# 9、：'jpg' 'swf' 'gif' 'sp'  
# 10、Advertising：banner、tips、、、  
# 11、：'roi' 'cpc' 'cpm' 'cpd'  
# 12、Advertising：'140*40' '308*388' '450*300' '600*90' '480*360' '960*126' '900*120'
# '390*270'  
# 13、Advertising：、、、second、、  

# ## Import libraries，data

# In[28]:


import pandas as pd 
import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder 
from sklearn.metrics import silhouette_score # import
from sklearn.cluster import KMeans # KMeans
get_ipython().run_line_magic('matplotlib', 'inline')
## attribute
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False


# ，OneHotEncoderencoding， if featuren，variableminuteNvariable，contains1，0，Nfeatureindicatesfeature。

# In[29]:


raw_data = pd.read_csv(r'./ad_performance.csv')
raw_data.head()


# Channel，dayUVPlacementtime（float and int）variable，variable。

# ### data

# In[30]:


# viewbasic 
raw_data.head(2)  # 2data


# In[31]:


raw_data.info()# dataDistribution


# In[32]:


raw_data.describe().round(2).T # databasic info


# ，respectivelydata、featuredata、and featureDistribution

# viewmissing values：

# In[33]:


# missing values
na_cols = raw_data.isnull().any(axis=0)  # viewmissing values
na_cols


# In[34]:


raw_data.isnull().sum().sort_values(ascending=False)# viewmissing valuesrecord


# variableCorrelationanalysis：

# In[35]:


# Correlationanalysis
raw_data.corr(numeric_only=True).round(2).T # dataCorrelationinfo


# In[36]:


# Correlationvisualization
import seaborn as sns 
corr = raw_data.corr().round(2)
sns.heatmap(corr,cmap='Reds',annot = True)


# We can see ，“” and “time”Correlationcompare，Correlationdescriptionvariablemodelhour，Effectiveness，can 。

# ## dataprocessing

# data，hourprocessingdata，datathrough 、、、、can Accuracydata。

# In[37]:


# 1 time
raw_data2 = raw_data.drop(['time'],axis=1)


# variableencoding：

# In[38]:


# variable
cols=["","Advertising","","Advertising","Advertising"]
for x in cols:
    data=raw_data2[x].unique()
    print("variable【{0}】：\n{1}".format(x,data))
    print("-·"*20)


# In[39]:


# classificationencodingprocessing
cols = ['','Advertising','','Advertising','Advertising'] 
model_ohe = OneHotEncoder(sparse=False)  # OneHotEncode
ohe_matrix = model_ohe.fit_transform(raw_data2[cols])  # 
print(ohe_matrix[:2])


# In[40]:


# pandas
ohe_matrix1=pd.get_dummies(raw_data2[cols])
ohe_matrix1.head(5)


# Data standardization：

# In[42]:


# Data standardization
sacle_matrix = raw_data2.iloc[:, 1:7]  # 
model_scaler = MinMaxScaler()  # MinMaxScalermodel
data_scaled = model_scaler.fit_transform(sacle_matrix)  # MinMaxScalerprocessing
print(data_scaled.round(2))


# dataprocessing，encodingdata and data：

# In[43]:


# # 
X = np.hstack((data_scaled, ohe_matrix))


# dataprocessing，can modeltraining。

# ## model
# 

# In[44]:


# through KMeansclusteringmodel
score_list = list()  # Kmodel
silhouette_int = -1  # 
for n_clusters in range(2, 8):  # 25
    model_kmeans = KMeans(n_clusters=n_clusters)  # clusteringmodel
    labels_tmp = model_kmeans.fit_predict(X)  # trainingclusteringmodel
    silhouette_tmp = silhouette_score(X, labels_tmp)  # K
    if silhouette_tmp > silhouette_int:  #  if 
        best_k = n_clusters  # saveKK
        silhouette_int = silhouette_tmp  # saveScore
        best_kmeans = model_kmeans  # savemodel
        cluster_labels_k = labels_tmp  # saveclusteringlabel
    score_list.append([n_clusters, silhouette_tmp])  # KScore
print('{:*^60}'.format('K:'))
print(np.array(score_list))  # Kdetailed Score
print('K:{0} \n:{1}'.format(best_k, silhouette_int))


# （Assessment），。

# ## clusteringresultfeatureanalysis

# through model，（sample）labelclusters，i.e. 4：

# In[45]:


# dataclusteringlabel
cluster_labels = pd.DataFrame(cluster_labels_k, columns=['clusters'])  # training setlabelinfo
merge_data = pd.concat((raw_data2, cluster_labels), axis=1)  # processingdataclusteringlabel
merge_data.head()


# ，sampleCount and Share：

# In[46]:


# calculateclusteringsample and sampleShare
clustering_count = pd.DataFrame(merge_data['Channel'].groupby(merge_data['clusters']).count()).T.rename({'Channel': 'counts'})  # calculateclusteringsample
clustering_ratio = (clustering_count / len(merge_data)).round(2).rename({'counts': 'percentage'})  # calculateclusteringsampleShare
print(clustering_count)
print("#"*30)
print(clustering_ratio)


# feature：

# In[47]:


# calculateclusteringfeature
cluster_features = []  # ，featureinfo
for line in range(best_k):  # 
    label_data = merge_data[merge_data['clusters'] == line]  # data

    part1_data = label_data.iloc[:, 1:7]  # datafeature
    part1_desc = part1_data.describe().round(3)  # featureinfo
    merge_data1 = part1_desc.iloc[2, :]  # feature

    part2_data = label_data.iloc[:, 7:-1]  # datafeature
    part2_desc = part2_data.describe(include='all')  # datafeatureinfo
    merge_data2 = part2_desc.iloc[2, :]  # datafeature

    merge_line = pd.concat((merge_data1, merge_data2), axis=0)  #  and feature
    cluster_features.append(merge_line)  # datafeature

#  featureinfo
cluster_pd = pd.DataFrame(cluster_features).T  # 
print('{:*^60}'.format('main feature:'))
all_cluster_set = pd.concat((clustering_count, clustering_ratio, cluster_pd),axis=0)  # clusteringinfo
all_cluster_set


# ：

# In[48]:


#Data Preprocessing
num_sets = cluster_pd.iloc[:6, :].T.astype(np.float64)  # data
num_sets_max_min = model_scaler.fit_transform(num_sets)  # data
print(num_sets)
print('-'*20)
print(num_sets_max_min)


# In[57]:


# 
fig = plt.figure(figsize=(7,7))  # 
ax = fig.add_subplot(111, polar=True)  # ，polarparameter
labels = np.array(merge_data1.index)  # datalabel
cor_list = ['g', 'r', 'y', 'b']  # different Color
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)  # calculate
angles = np.concatenate((angles, [angles[0]]))  # 
# 
for i in range(len(num_sets)):  # 
    data_tmp = num_sets_max_min[i, :]  # data
    data = np.concatenate((data_tmp, [data_tmp[0]]))  # 
    ax.plot(angles, data, 'o-', c=cor_list[i], label="%dChannel"%(i))  # 
    ax.fill(angles, data,alpha=0.8)
    
# Image
print(angles)
print(labels)

ax.set_thetagrids(angles[0:-1] * 180 / np.pi, labels, fontproperties="SimHei")  # 
ax.set_title("clusteringfeature", fontproperties="SimHei")  # 
ax.set_rlim(-0.2, 1.2)  # 
plt.legend(loc="upper right" ,bbox_to_anchor=(1.2,1.0))  # 


# ## data
# 

# result，Channelminute4，sampleare:：154、313、349 、73，Shareare:：17%、35%、39%、8%。

# through can ：

# 1（2Channel）
# Advertising and Placementtime，attribute， therefore AdvertisingEffectiveness，39%， therefore Channel。
# Placement。
# 
# 
# 
# 2（1Channel）
# Advertising，、dayUV、OrderAdvertisingEffectiveness，EffectivenessChannel。
#  but dayUV，。and user，Advertisinguser，Order。
# 
# 
# 
# 3（0Channel）
# AdvertisingfeaturedayUV and ，“” and “”Effectiveness，can Advertising。
# “Advertising”，“”using 。
# 
# 
# 
# 4（3Channel）
# Channelfeature， and Count“”。 but ，can ChannelPlacementAdvertising。
