#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Project Introduction" data-toc-modified-id="Project Introduction-1"><span class="toc-item-num">1  </span>Project Introduction</a></span></li><li><span><a href="#import" data-toc-modified-id="import-2"><span class="toc-item-num">2  </span>import</a></span></li><li><span><a href="#filePostgraduate ExamyearScore Line" data-toc-modified-id="filePostgraduate ExamyearScore Line-3"><span class="toc-item-num">3  </span>filePostgraduate ExamyearScore Line</a></span></li><li><span><a href="#processing and null" data-toc-modified-id="processing and null-4"><span class="toc-item-num">4  </span>processing and null</a></span></li><li><span><a href="#need to " data-toc-modified-id="need to -5"><span class="toc-item-num">5  </span>need to </a></span></li><li><span><a href="#" data-toc-modified-id="-6"><span class="toc-item-num">6  </span></a></span></li><li><span><a href="#2020yearPostgraduate Examinfo" data-toc-modified-id="2020yearPostgraduate Examinfo-7"><span class="toc-item-num">7  </span>2020yearPostgraduate Examinfo</a></span></li><li><span><a href="#" data-toc-modified-id="-8"><span class="toc-item-num">8  </span></a></span></li><li><span><a href="#minute（may ）" data-toc-modified-id="minute（may ）-9"><span class="toc-item-num">9  </span>minute（may ）</a></span></li><li><span><a href="#Postgraduate Examminute" data-toc-modified-id="Postgraduate Examminute-10"><span class="toc-item-num">10  </span>Postgraduate Examminute</a></span></li><li><span><a href="#minuteminute，minute，minute" data-toc-modified-id="minuteminute，minute，minute-11"><span class="toc-item-num">11  </span>minuteminute，minute，minute</a></span></li><li><span><a href="#Score" data-toc-modified-id="Score-12"><span class="toc-item-num">12  </span>Score</a></span></li><li><span><a href="#2020yearPostgraduate ExamTop50" data-toc-modified-id="2020yearPostgraduate ExamTop50-13"><span class="toc-item-num">13  </span>2020yearPostgraduate ExamTop50</a></span></li><li><span><a href="#Keywords" data-toc-modified-id="Keywords-14"><span class="toc-item-num">14  </span>Keywords</a></span></li><li><span><a href="#2021yearPostgraduate Examinfo" data-toc-modified-id="2021yearPostgraduate Examinfo-15"><span class="toc-item-num">15  </span>2021yearPostgraduate Examinfo</a></span></li><li><span><a href="#attribute" data-toc-modified-id="attribute-16"><span class="toc-item-num">16  </span>attribute</a></span></li><li><span><a href="#" data-toc-modified-id="-17"><span class="toc-item-num">17  </span></a></span></li><li><span><a href="#info" data-toc-modified-id="info-18"><span class="toc-item-num">18  </span>info</a></span></li><li><span><a href="#viewdata" data-toc-modified-id="viewdata-19"><span class="toc-item-num">19  </span>viewdata</a></span></li><li><span><a href="#time" data-toc-modified-id="time-20"><span class="toc-item-num">20  </span>time</a></span></li><li><span><a href="#infotime" data-toc-modified-id="infotime-21"><span class="toc-item-num">21  </span>infotime</a></span><ul class="toc-item"><li><span><a href="#Postgraduate Exam2month， so " data-toc-modified-id="Postgraduate Exam2month， so -21.1"><span class="toc-item-num">21.1  </span>Postgraduate Exam2month， so </a></span></li></ul></li><li><span><a href="#" data-toc-modified-id="-22"><span class="toc-item-num">22  </span></a></span></li><li><span><a href="#infoDistribution" data-toc-modified-id="infoDistribution-23"><span class="toc-item-num">23  </span>infoDistribution</a></span></li></ul></div>

# ### Project Introduction
# * data IT：2021yearPostgraduate Examinfo through Postgraduate Exam +  
# * visualizationmain using  pyecharts 
# 

# ### Import libraries

# In[1]:


import json
import requests
import pandas as pd 
import pyecharts.options as opts
from pyecharts.charts import *
from pyecharts.globals import ThemeType#
from pyecharts.commons.utils import JsCode
import chardet 
import jieba
import numpy as np


# ### filePostgraduate ExamyearScore Line

# In[2]:


df1 = pd.read_csv(r'./Postgraduate ExamyearScore Line(1).csv')
df2 = pd.read_csv(r'./Postgraduate ExamyearScore Line(2).csv')
df3 = pd.read_csv(r'./Postgraduate ExamyearScore Line(3).csv')
df4 = pd.read_csv(r'./Postgraduate ExamyearScore Line(4).csv')
df5 = pd.read_csv(r'./Postgraduate ExamyearScore Line(5).csv')
df6 = pd.read_csv(r'./Postgraduate ExamyearScore Line(6).csv')
df_all= pd.concat([df1,df2,df3,df4,df5,df6])
df_all.info()


# In[3]:


print(df_all.shape)


# ### processing and null

# In[4]:


print('：' ,df_all.duplicated().sum())
print('null: \n',df_all.isnull().sum())


# In[5]:


df_all = df_all.drop_duplicates()
df_all = df_all.dropna(axis=0,how='any')


# In[6]:


df_all.info()
print(df_all.shape)


# In[7]:


print('：' ,df_all.duplicated().sum())
print('null: \n',df_all.isnull().sum())


# ### need to 

# In[8]:


df_all = df_all.drop(labels=['_','_','_'],axis=1)
df_all.head(2)


# ### 

# In[9]:


df_all[''] = df_all[''].str.replace('\(\)','')
df_all[''] = df_all[''].str.replace('★','')
df_all.head(2)


# ### 2020yearPostgraduate Examinfo

# In[10]:


data_2020 = df_all[df_all['Year'] == 2020]
data_2020.info()


# ### 

# In[11]:


data_2020[''].value_counts()[:100]


# ### Grouping（may ）

# In[12]:


data_2020.groupby('')[''].count().sort_values(ascending = False)[:100]


# ### Postgraduate Examminute

# In[13]:


def tranform_num(x):
    if '-' in x:
        return 0
    else:
        return x
    
data_2020['minute'] = data_2020['minute'].apply(lambda x:tranform_num(x) )
data_2020['minute'] = data_2020['minute'].astype('int')


# ### Groupingminute，minute，minute

# In[14]:


data_1 = data_2020.groupby('')['minute'].agg([np.mean, np.max,np.min])
data_1['mean'] = data_1['mean'].astype('int')
data_1 = data_1.sort_values(by=['mean'],ascending=False)[:50]
data_1
		
data_1.columns = ['mean','amax','amin']
# ### Score

# In[15]:


bar = Bar(init_opts=opts.InitOpts(theme='light',
                                    width='1000px',
                                    height='1200px')
                                    )

bar.add_xaxis(data_1.index.tolist())
bar.add_yaxis('minute', 
               data_1['amax'].tolist(),
               z_level=1,
               stack='1',
               category_gap='50%',
               tooltip_opts=opts.TooltipOpts(is_show=False),
               label_opts=opts.LabelOpts(position='insideRight', formatter='{c} minute'),
               itemstyle_opts={"normal": {
                        'shadowBlur': 10,
                        'shadowColor': 'rgba(0, 0, 0, 0.1)',
                        'shadowOffsetX': 10,
                        'shadowOffsetY': 10,
                        'color':'#ec9bad',
                        'borderColor': 'rgb(220,220,220)',
                        'borderWidth':2}
                },
               )
bar.add_yaxis('minute', 
               data_1['amin'].tolist(),
               z_level=1,
               stack='1',
               category_gap='50%',
               tooltip_opts=opts.TooltipOpts(is_show=False),
               label_opts=opts.LabelOpts(position='insideLeft', formatter='{c} minute'),
               itemstyle_opts={"normal": {
                        'shadowBlur': 10,
                        'shadowColor': 'rgba(0, 0, 0, 0.1)',
                        'shadowOffsetX': 10,
                        'shadowOffsetY': 10,
                        'color':'#87CEFA',
                        'borderColor': 'rgb(220,220,220)',
                        'borderWidth':2}
                },
               )


bar.set_global_opts(title_opts=opts.TitleOpts(title="minute and minute",
                                              pos_left="center",
                                              pos_top='0%',
                                              title_textstyle_opts=opts.TextStyleOpts(font_size=20,
                                                                                      color='#00BFFF')),
                        legend_opts=opts.LegendOpts(is_show=True, pos_top='3%'),
                        datazoom_opts=opts.DataZoomOpts(type_='inside',
                                                    range_start=50,   # ，50%-100%
                                                    range_end=100,
                                                    orient='vertical'),
                        xaxis_opts=opts.AxisOpts(is_show=False, max_=818),
                        yaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=False),
                                             axistick_opts=opts.AxisTickOpts(is_show=False),
                                             axislabel_opts=opts.LabelOpts(color='#528B8B', font_size=10, font_weight='bold')),
                    )
bar.reversal_axis()
bar.render_notebook()


# In[16]:


data_2 = data_2020[''].value_counts()[:50]


# ### 2020yearPostgraduate ExamTop50

# In[17]:


data_x =data_2.index.tolist()
data_y = data_2.values.tolist()

bar = Bar(init_opts=opts.InitOpts(theme='light',
                                  width='1000px',
                                  height='900px'))
bar.add_xaxis(data_x)
bar.add_yaxis('Postgraduate Exam', [int(i) for i in data_y])
bar.set_series_opts(label_opts=opts.LabelOpts(position="insideLeft",
                                              font_size=12,
                                              font_weight='bold',
                                              formatter='{b}:{c} '))
bar.set_global_opts(title_opts=opts.TitleOpts(title="2020yearPostgraduate ExamTop50", pos_top='2%', pos_left='center', 
                                              title_textstyle_opts=opts.TextStyleOpts(font_size=20,
                                                                                      color='#00BFFF')),
                    legend_opts=opts.LegendOpts(is_show=False),
                    xaxis_opts=opts.AxisOpts(is_show=False, is_scale=True),
                    yaxis_opts=opts.AxisOpts(is_show=False),
                    datazoom_opts=opts.DataZoomOpts(type_='inside',
                                                    range_start=50,   # ，50%-100%
                                                    range_end=100,
                                                    orient='vertical'),
                    
                    visualmap_opts=opts.VisualMapOpts(is_show=False, 
                                          max_=1058,
                                          min_=1,
                                          is_piecewise=False,
                                          dimension=0,
                                          range_color=['rgba(236,155,173,1)', 'rgba(237,157,178,0.4)'])
                                      )
bar.reversal_axis()
bar.render_notebook()


# ### Keywords

# In[18]:


def get_cut_words(content_series):
    # 
    stop_words = [' ','',''] 

#     with open(r"\.txt", 'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             stop_words.append(line.strip())

    # Keywords
    my_words = ['']      
    for i in my_words:
        jieba.add_word(i) 

    # 
    my_stop_words = ['view','detailed ','','','','03','02','01','','','related ']    
    stop_words.extend(my_stop_words)               

    # minute
    word_num = jieba.lcut(content_series.str.cat(sep='。'), cut_all=False)

    # 
    word_num_selected = [i for i in word_num if i not in stop_words and len(i)>=2]
    
    return word_num_selected


# In[19]:


text1 = get_cut_words(content_series=df_all.)


# In[22]:


# stylecloud
get_ipython().system('pip install stylecloud  -i https://pypi.tuna.tsinghua.edu.cn/simple')


# In[23]:


import numpy as np
import stylecloud
from IPython.display import Image 

stylecloud.gen_stylecloud(
    text=' '.join(text1),
    collocations=False,
    font_path=r'./SimHei.ttf',
    icon_name='fas fa-book',
    size=768,
    output_name='./1.png'
)

Image(filename='./1.png')


# In[24]:


text2 = get_cut_words(content_series=df_all.)
text2[:4]


# In[25]:


stylecloud.gen_stylecloud(
    text=' '.join(text2),
    collocations=False,
    font_path=r'./SimHei.ttf',
    icon_name='fas fa-graduation-cap',
    size=768,
    output_name='2.png'
)

Image(filename='2.png')


# ### 2021yearPostgraduate Examinfo

# In[26]:


import pandas as pd


# In[27]:


df_info = pd.read_excel(r'./Universityinfo2021new.xlsx')
df_info.head()


# In[28]:


get_ipython().system('pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn')


# In[29]:


df_info.info()


# ### attribute

# In[30]:


def transform_attr(x):
    #attribute
    if '211' in x and '985' not in x:
        return 211 
    elif '985' in x:
        return '985'
    else:
        return ''
    
def transform_type(x):
    #
    if '' in x or '' in x or '' in x or '、University' in x or '\n[4]' in x or '\n[6]' in x:
        return ''
    elif '' in x or 'University\n[3]' in x or '（University）' in x or '、University' in x or 'University' in x or '' in x:
        return ''
    elif '' in x or '' in x or '（）' in x or '（）' in x or '' in x:
        return ''
    elif '' in x or '' in x: 
        return ''
    elif '' in x:
        return ''
    elif '' in x:
        return ''
    elif '' in x or '' in x or '' in x or 'University' in x:
        return ''
    elif '' in x or '' in x or '2' in x or '' in x:
        return ''
    else:
        return x 
    
# data
df_info['school_level'] = df_info.school_attr.astype(str).apply(lambda x:transform_attr(x))
df_info['school_types'] = df_info.school_type.astype(str).apply(lambda x: transform_type(x))
# 
df_info= df_info[['school','province','school_level','school_types']]

# processingdata
df_info.loc[(df_info.school=='University')&(df_info.province==''), 'province']= '' 
df_info.loc[(df_info.school=='University')&(df_info.province==''), 'province']= '' 
df_info.loc[(df_info.school=='University')&(df_info.province==''), 'province']= '' 
df_info.loc[(df_info.school=='University')&(df_info.province==''), 'province']= '' 
df_info.loc[(df_info.school=='')&(df_info.province==''), 'province']= '' 
df_info.loc[(df_info.school=='University')&(df_info.province==''), 'province']= ''
df_info.loc[(df_info.school=='University')&(df_info.province==''), 'province']= ''
df_info.loc[(df_info.school=='University')&(df_info.province==''), 'province']= ''
df_info.loc[(df_info.school=='University')&(df_info.province==''), 'province']= ''
df_info.loc[(df_info.school=='University')&(df_info.province==''), 'province']= ''
df_info.loc[(df_info.school=='University')&(df_info.province==''), 'province']= ''


# In[31]:


df_info.head()


# ### 

# In[32]:


df_info = df_info.drop_duplicates()#
df_info.info()


# In[33]:


df_info.shape


# In[34]:


df = pd.read_excel(r'./Postgraduate Examdata-3.08.xlsx')
df.shape


# In[35]:


df_2021 = df[df['time'].str.contains('2021')].copy()
df_2021.shape


# In[36]:


pd.merge(df_2021,df_info,how = 'left',on = 'school').shape


# ### info

# In[37]:


df_all = pd.merge(df_2021,df_info,how = 'left',on = 'school')
df_all.head(5)


# In[38]:


df_all = df_all[['school','name','time','province','school_level','school_types']]
df_all.head()


# ### viewdata

# In[39]:


df_all.isnull().sum()


# ### time

# In[40]:


pub_time = df_all.time.value_counts().sort_index()
pub_time


# ### infotime

# In[41]:


line1 = Line(init_opts=opts.InitOpts(width='1000px',height='600px'))
line1.add_xaxis(pub_time.index.tolist())
line1.add_yaxis('',pub_time.values.tolist(),
               areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
               label_opts=opts.LabelOpts(is_show=True))
line1.set_global_opts(title_opts=opts.TitleOpts(title='infotime'),
                     toolbox_opts=opts.ToolboxOpts(),
                      xaxis_opts=opts.AxisOpts(name='time',
                                               type_='category',                                           
                                               axislabel_opts=opts.LabelOpts(rotate=45),
                                               ),
                     visualmap_opts=opts.VisualMapOpts())
line1.render_notebook()


# #### Postgraduate Exam2month， so 

# ### 

# In[42]:


level_perc = df_all.school_level.value_counts() / df_all.school_level.value_counts().sum()
display(level_perc)
level_perc = np.round(level_perc * 100 ,2)
level_perc


# In[43]:


pie1 = Pie(init_opts=opts.InitOpts(theme='light',width='800px',height='600px'))
pie1.add("", 
         [*zip(level_perc.index, level_perc.values)], 
         radius=["40%","75%"]) 
pie1.set_global_opts(title_opts=opts.TitleOpts(title='Distribution',pos_left='center', pos_top='center',title_textstyle_opts=opts.TextStyleOpts(
                                                   color='#00BFFF', font_size=30, font_weight='bold'),
                                               ), 
                     legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
#                      toolbox_opts=opts.ToolboxOpts()
                    )   
pie1.set_series_opts(label_opts=opts.LabelOpts(formatter="{c}%")) 
pie1.render_notebook()


# ### infoDistribution

# In[44]:


province_num = df_all.province.value_counts().sort_values()
province_num


# In[45]:


# 
bar1 = Bar(init_opts=opts.InitOpts(theme='light',width='1000px', height='1000px')) 
bar1.add_xaxis(province_num.index.tolist())
bar1.add_yaxis("", province_num.values.tolist()) 
bar1.set_global_opts(title_opts=opts.TitleOpts(title="infoDistribution"), 
#                      toolbox_opts=opts.ToolboxOpts(),
                     visualmap_opts=opts.VisualMapOpts(max_=79)) 
bar1.set_series_opts(label_opts=opts.LabelOpts(position='right'))  # label
bar1.reversal_axis() 
bar1.render_notebook()


# In[58]:


c = Map(init_opts=opts.InitOpts(width='800px', height='750px'))
c.add('',[list(z) for z in zip(province_num.index.tolist(), province_num.values.tolist())], 'china')
c.set_global_opts(title_opts=opts.TitleOpts('infoDistribution'), 
#                   toolbox_opts=opts.ToolboxOpts(is_show=True), 
                  visualmap_opts=opts.VisualMapOpts(max_=79)) 
c.render_notebook()


# In[61]:


print([list(z) for z in zip(province_num.index.tolist(), province_num.values.tolist())])


# In[60]:


# 
c = Map(init_opts=opts.InitOpts(width='800px', height='750px'))
c.add('',[['', 2],
 ['', 2],
 ['', 4],
 ['', 4],
 ['', 4],
 ['', 5],
 ['', 6],
 ['days', 11],
 ['', 14],
 ['', 18],
 ['', 20],
 ['', 20],
 ['', 21],
 ['', 22],
 ['', 23],
 ['', 24],
 ['', 28],
 ['', 30],
 ['', 32],
 ['', 33],
 ['', 39],
 ['', 40],
 ['', 41],
 ['', 45],
 ['', 46],
 ['', 48],
 ['', 49],
 ['', 64],
 ['', 79]], 'china')
c.set_global_opts(title_opts=opts.TitleOpts('infoDistribution'), 
#                   toolbox_opts=opts.ToolboxOpts(is_show=True), 
                  visualmap_opts=opts.VisualMapOpts(max_=79)) 
c.render_notebook()


# In[ ]:




