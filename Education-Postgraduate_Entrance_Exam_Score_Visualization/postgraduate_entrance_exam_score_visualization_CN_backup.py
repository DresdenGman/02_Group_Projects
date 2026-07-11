#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#项目介绍" data-toc-modified-id="项目介绍-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>项目介绍</a></span></li><li><span><a href="#导入库" data-toc-modified-id="导入库-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>导入库</a></span></li><li><span><a href="#读取文件考研历年国家分数线" data-toc-modified-id="读取文件考研历年国家分数线-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>读取文件考研历年国家分数线</a></span></li><li><span><a href="#处理重复值和空值" data-toc-modified-id="处理重复值和空值-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>处理重复值和空值</a></span></li><li><span><a href="#删除不需要的列" data-toc-modified-id="删除不需要的列-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>删除不需要的列</a></span></li><li><span><a href="#替换删除特殊字符" data-toc-modified-id="替换删除特殊字符-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>替换删除特殊字符</a></span></li><li><span><a href="#单独筛选出2020年考研信息" data-toc-modified-id="单独筛选出2020年考研信息-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>单独筛选出2020年考研信息</a></span></li><li><span><a href="#统计专业" data-toc-modified-id="统计专业-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>统计专业</a></span></li><li><span><a href="#分组归纳学校对应的专业数（专业可能是重复值）" data-toc-modified-id="分组归纳学校对应的专业数（专业可能是重复值）-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>分组归纳学校对应的专业数（专业可能是重复值）</a></span></li><li><span><a href="#转化考研专业总分特殊值" data-toc-modified-id="转化考研专业总分特殊值-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>转化考研专业总分特殊值</a></span></li><li><span><a href="#分组归纳各专业的最高分，最低分，平均分" data-toc-modified-id="分组归纳各专业的最高分，最低分，平均分-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>分组归纳各专业的最高分，最低分，平均分</a></span></li><li><span><a href="#绘制各专业分数的柱状图" data-toc-modified-id="绘制各专业分数的柱状图-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>绘制各专业分数的柱状图</a></span></li><li><span><a href="#绘制2020年考研专业Top50" data-toc-modified-id="绘制2020年考研专业Top50-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>绘制2020年考研专业Top50</a></span></li><li><span><a href="#绘制关键词云图" data-toc-modified-id="绘制关键词云图-14"><span class="toc-item-num">14&nbsp;&nbsp;</span>绘制关键词云图</a></span></li><li><span><a href="#读取2021年考研调剂信息" data-toc-modified-id="读取2021年考研调剂信息-15"><span class="toc-item-num">15&nbsp;&nbsp;</span>读取2021年考研调剂信息</a></span></li><li><span><a href="#转换学校属性类别" data-toc-modified-id="转换学校属性类别-16"><span class="toc-item-num">16&nbsp;&nbsp;</span>转换学校属性类别</a></span></li><li><span><a href="#删除重复值" data-toc-modified-id="删除重复值-17"><span class="toc-item-num">17&nbsp;&nbsp;</span>删除重复值</a></span></li><li><span><a href="#拼接调剂信息" data-toc-modified-id="拼接调剂信息-18"><span class="toc-item-num">18&nbsp;&nbsp;</span>拼接调剂信息</a></span></li><li><span><a href="#查看缺失数据" data-toc-modified-id="查看缺失数据-19"><span class="toc-item-num">19&nbsp;&nbsp;</span>查看缺失数据</a></span></li><li><span><a href="#发布时间对应的发布频次" data-toc-modified-id="发布时间对应的发布频次-20"><span class="toc-item-num">20&nbsp;&nbsp;</span>发布时间对应的发布频次</a></span></li><li><span><a href="#调剂信息发布时间走势图" data-toc-modified-id="调剂信息发布时间走势图-21"><span class="toc-item-num">21&nbsp;&nbsp;</span>调剂信息发布时间走势图</a></span><ul class="toc-item"><li><span><a href="#由于考研成绩是在2月底发布的，所以调剂发布学校也随着增多" data-toc-modified-id="由于考研成绩是在2月底发布的，所以调剂发布学校也随着增多-21.1"><span class="toc-item-num">21.1&nbsp;&nbsp;</span>由于考研成绩是在2月底发布的，所以调剂发布学校也随着增多</a></span></li></ul></li><li><span><a href="#绘制学校类别饼图" data-toc-modified-id="绘制学校类别饼图-22"><span class="toc-item-num">22&nbsp;&nbsp;</span>绘制学校类别饼图</a></span></li><li><span><a href="#调剂信息发布数省份分布" data-toc-modified-id="调剂信息发布数省份分布-23"><span class="toc-item-num">23&nbsp;&nbsp;</span>调剂信息发布数省份分布</a></span></li></ul></div>

# ### 项目介绍
# * 数据来源 IT：2021年考研调剂信息 通过考研网站 + 百度百科 整理获取
# * 可视化主要使用 pyecharts 
# 

# ### 导入库

# In[1]:


import json
import requests
import pandas as pd 
import pyecharts.options as opts
from pyecharts.charts import *
from pyecharts.globals import ThemeType#设定主题
from pyecharts.commons.utils import JsCode
import chardet 
import jieba
import numpy as np


# ### 读取文件考研历年国家分数线

# In[2]:


df1 = pd.read_csv(r'./考研历年国家分数线(1).csv')
df2 = pd.read_csv(r'./考研历年国家分数线(2).csv')
df3 = pd.read_csv(r'./考研历年国家分数线(3).csv')
df4 = pd.read_csv(r'./考研历年国家分数线(4).csv')
df5 = pd.read_csv(r'./考研历年国家分数线(5).csv')
df6 = pd.read_csv(r'./考研历年国家分数线(6).csv')
df_all= pd.concat([df1,df2,df3,df4,df5,df6])
df_all.info()


# In[3]:


print(df_all.shape)


# ### 处理重复值和空值

# In[4]:


print('重复值：' ,df_all.duplicated().sum())
print('空值: \n',df_all.isnull().sum())


# In[5]:


df_all = df_all.drop_duplicates()
df_all = df_all.dropna(axis=0,how='any')


# In[6]:


df_all.info()
print(df_all.shape)


# In[7]:


print('重复值：' ,df_all.duplicated().sum())
print('空值: \n',df_all.isnull().sum())


# ### 删除不需要的列

# In[8]:


df_all = df_all.drop(labels=['学校名称_链接','院系名称_链接','专业名称_链接'],axis=1)
df_all.head(2)


# ### 替换删除特殊字符

# In[9]:


df_all['专业名称'] = df_all['专业名称'].str.replace('\(专业学位\)','')
df_all['专业名称'] = df_all['专业名称'].str.replace('★','')
df_all.head(2)


# ### 单独筛选出2020年考研信息

# In[10]:


data_2020 = df_all[df_all['年份'] == 2020]
data_2020.info()


# ### 统计专业

# In[11]:


data_2020['专业名称'].value_counts()[:100]


# ### 分组归纳学校对应的专业数（专业可能是重复值）

# In[12]:


data_2020.groupby('学校名称')['专业名称'].count().sort_values(ascending = False)[:100]


# ### 转化考研专业总分特殊值

# In[13]:


def tranform_num(x):
    if '-' in x:
        return 0
    else:
        return x
    
data_2020['总分'] = data_2020['总分'].apply(lambda x:tranform_num(x) )
data_2020['总分'] = data_2020['总分'].astype('int')


# ### 分组归纳各专业的最高分，最低分，平均分

# In[14]:


data_1 = data_2020.groupby('专业名称')['总分'].agg([np.mean, np.max,np.min])
data_1['mean'] = data_1['mean'].astype('int')
data_1 = data_1.sort_values(by=['mean'],ascending=False)[:50]
data_1
		
data_1.columns = ['mean','amax','amin']
# ### 绘制各专业分数的柱状图

# In[15]:


bar = Bar(init_opts=opts.InitOpts(theme='light',
                                    width='1000px',
                                    height='1200px')
                                    )

bar.add_xaxis(data_1.index.tolist())
bar.add_yaxis('最高分', 
               data_1['amax'].tolist(),
               z_level=1,
               stack='1',
               category_gap='50%',
               tooltip_opts=opts.TooltipOpts(is_show=False),
               label_opts=opts.LabelOpts(position='insideRight', formatter='{c} 分'),
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
bar.add_yaxis('最低分', 
               data_1['amin'].tolist(),
               z_level=1,
               stack='1',
               category_gap='50%',
               tooltip_opts=opts.TooltipOpts(is_show=False),
               label_opts=opts.LabelOpts(position='insideLeft', formatter='{c} 分'),
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


bar.set_global_opts(title_opts=opts.TitleOpts(title="各专业的最高分和最低分",
                                              pos_left="center",
                                              pos_top='0%',
                                              title_textstyle_opts=opts.TextStyleOpts(font_size=20,
                                                                                      color='#00BFFF')),
                        legend_opts=opts.LegendOpts(is_show=True, pos_top='3%'),
                        datazoom_opts=opts.DataZoomOpts(type_='inside',
                                                    range_start=50,   # 设置起止位置，50%-100%
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


data_2 = data_2020['专业名称'].value_counts()[:50]


# ### 绘制2020年考研专业Top50

# In[17]:


data_x =data_2.index.tolist()
data_y = data_2.values.tolist()

bar = Bar(init_opts=opts.InitOpts(theme='light',
                                  width='1000px',
                                  height='900px'))
bar.add_xaxis(data_x)
bar.add_yaxis('考研专业', [int(i) for i in data_y])
bar.set_series_opts(label_opts=opts.LabelOpts(position="insideLeft",
                                              font_size=12,
                                              font_weight='bold',
                                              formatter='{b}:{c} 个'))
bar.set_global_opts(title_opts=opts.TitleOpts(title="2020年考研专业Top50", pos_top='2%', pos_left='center', 
                                              title_textstyle_opts=opts.TextStyleOpts(font_size=20,
                                                                                      color='#00BFFF')),
                    legend_opts=opts.LegendOpts(is_show=False),
                    xaxis_opts=opts.AxisOpts(is_show=False, is_scale=True),
                    yaxis_opts=opts.AxisOpts(is_show=False),
                    datazoom_opts=opts.DataZoomOpts(type_='inside',
                                                    range_start=50,   # 设置起止位置，50%-100%
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


# ### 绘制关键词云图

# In[18]:


def get_cut_words(content_series):
    # 读入停用词表
    stop_words = [' ','是','的'] 

#     with open(r"\中文停用词库.txt", 'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             stop_words.append(line.strip())

    # 添加关键词
    my_words = ['']      
    for i in my_words:
        jieba.add_word(i) 

    # 自定义停用词
    my_stop_words = ['查看','详细','详见','详情','与化','03','02','01','正文','多个','相关']    
    stop_words.extend(my_stop_words)               

    # 分词
    word_num = jieba.lcut(content_series.str.cat(sep='。'), cut_all=False)

    # 条件筛选
    word_num_selected = [i for i in word_num if i not in stop_words and len(i)>=2]
    
    return word_num_selected


# In[19]:


text1 = get_cut_words(content_series=df_all.专业名称)


# In[22]:


# 安装stylecloud
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
    output_name='./词云图1.png'
)

Image(filename='./词云图1.png')


# In[24]:


text2 = get_cut_words(content_series=df_all.学校名称)
text2[:4]


# In[25]:


stylecloud.gen_stylecloud(
    text=' '.join(text2),
    collocations=False,
    font_path=r'./SimHei.ttf',
    icon_name='fas fa-graduation-cap',
    size=768,
    output_name='词云图2.png'
)

Image(filename='词云图2.png')


# ### 读取2021年考研调剂信息

# In[26]:


import pandas as pd


# In[27]:


df_info = pd.read_excel(r'./大学信息2021new.xlsx')
df_info.head()


# In[28]:


get_ipython().system('pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn')


# In[29]:


df_info.info()


# ### 转换学校属性类别

# In[30]:


def transform_attr(x):
    #转换学校属性
    if '211' in x and '985' not in x:
        return 211 
    elif '985' in x:
        return '985'
    else:
        return '双非'
    
def transform_type(x):
    #转换学校类型
    if '理工类' in x or '理工类院校' in x or '理工科' in x or '理工、教学研究型大学' in x or '理工类\n[4]' in x or '理工\n[6]' in x:
        return '理工'
    elif '综合类' in x or '综合性大学\n[3]' in x or '综合类（应用型大学）' in x or '综合、研究教学型大学' in x or '综合类大学' in x or '综合师范类' in x:
        return '综合'
    elif '师范类院校' in x or '师范类' in x or '师范类（综合类）' in x or '师范（综合）' in x or '地方师范院校' in x:
        return '师范'
    elif '农林类' in x or '农业类' in x: 
        return '农林'
    elif '医药类' in x:
        return '医药'
    elif '民族类' in x:
        return '民族'
    elif '未知' in x or '国有企业' in x or '科技型企业' in x or '公立大学' in x:
        return '其他'
    elif '重点' in x or '省' in x or '2' in x or '' in x:
        return '其他'
    else:
        return x 
    
# 转换数据
df_info['school_level'] = df_info.school_attr.astype(str).apply(lambda x:transform_attr(x))
df_info['school_types'] = df_info.school_type.astype(str).apply(lambda x: transform_type(x))
# 筛选字段
df_info= df_info[['school','province','school_level','school_types']]

# 处理省份数据
df_info.loc[(df_info.school=='北京工商大学')&(df_info.province=='未知'), 'province']= '北京' 
df_info.loc[(df_info.school=='哈尔滨工程大学')&(df_info.province=='未知'), 'province']= '哈尔滨' 
df_info.loc[(df_info.school=='江苏大学')&(df_info.province=='未知'), 'province']= '江苏' 
df_info.loc[(df_info.school=='青岛大学')&(df_info.province=='未知'), 'province']= '山东' 
df_info.loc[(df_info.school=='北京石油化工学院')&(df_info.province=='未知'), 'province']= '北京' 
df_info.loc[(df_info.school=='齐鲁工业大学')&(df_info.province=='未知'), 'province']= '山东'
df_info.loc[(df_info.school=='江苏科技大学')&(df_info.province=='未知'), 'province']= '江苏'
df_info.loc[(df_info.school=='浙江农林大学')&(df_info.province=='未知'), 'province']= '浙江'
df_info.loc[(df_info.school=='燕山大学')&(df_info.province=='未知'), 'province']= '河北'
df_info.loc[(df_info.school=='福州大学')&(df_info.province=='未知'), 'province']= '福建'
df_info.loc[(df_info.school=='内蒙古科技大学')&(df_info.province=='未知'), 'province']= '内蒙古'


# In[31]:


df_info.head()


# ### 删除重复值

# In[32]:


df_info = df_info.drop_duplicates()#删除重
df_info.info()


# In[33]:


df_info.shape


# In[34]:


df = pd.read_excel(r'./考研调剂数据-3.08.xlsx')
df.shape


# In[35]:


df_2021 = df[df['time'].str.contains('2021')].copy()
df_2021.shape


# In[36]:


pd.merge(df_2021,df_info,how = 'left',on = 'school').shape


# ### 拼接调剂信息

# In[37]:


df_all = pd.merge(df_2021,df_info,how = 'left',on = 'school')
df_all.head(5)


# In[38]:


df_all = df_all[['school','name','time','province','school_level','school_types']]
df_all.head()


# ### 查看缺失数据

# In[39]:


df_all.isnull().sum()


# ### 发布时间对应的发布频次

# In[40]:


pub_time = df_all.time.value_counts().sort_index()
pub_time


# ### 调剂信息发布时间走势图

# In[41]:


line1 = Line(init_opts=opts.InitOpts(width='1000px',height='600px'))
line1.add_xaxis(pub_time.index.tolist())
line1.add_yaxis('发布热度',pub_time.values.tolist(),
               areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
               label_opts=opts.LabelOpts(is_show=True))
line1.set_global_opts(title_opts=opts.TitleOpts(title='调剂信息发布时间走势图'),
                     toolbox_opts=opts.ToolboxOpts(),
                      xaxis_opts=opts.AxisOpts(name='时间',
                                               type_='category',                                           
                                               axislabel_opts=opts.LabelOpts(rotate=45),
                                               ),
                     visualmap_opts=opts.VisualMapOpts())
line1.render_notebook()


# #### 由于考研成绩是在2月底发布的，所以调剂发布学校也随着增多

# ### 绘制学校类别饼图

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
pie1.set_global_opts(title_opts=opts.TitleOpts(title='学校层次分布',pos_left='center', pos_top='center',title_textstyle_opts=opts.TextStyleOpts(
                                                   color='#00BFFF', font_size=30, font_weight='bold'),
                                               ), 
                     legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
#                      toolbox_opts=opts.ToolboxOpts()
                    )   
pie1.set_series_opts(label_opts=opts.LabelOpts(formatter="{c}%")) 
pie1.render_notebook()


# ### 调剂信息发布数省份分布

# In[44]:


province_num = df_all.province.value_counts().sort_values()
province_num


# In[45]:


# 条形图
bar1 = Bar(init_opts=opts.InitOpts(theme='light',width='1000px', height='1000px')) 
bar1.add_xaxis(province_num.index.tolist())
bar1.add_yaxis("省份", province_num.values.tolist()) 
bar1.set_global_opts(title_opts=opts.TitleOpts(title="调剂信息发布数省份分布"), 
#                      toolbox_opts=opts.ToolboxOpts(),
                     visualmap_opts=opts.VisualMapOpts(max_=79)) 
bar1.set_series_opts(label_opts=opts.LabelOpts(position='right'))  # 标签
bar1.reversal_axis() 
bar1.render_notebook()


# In[58]:


c = Map(init_opts=opts.InitOpts(width='800px', height='750px'))
c.add('',[list(z) for z in zip(province_num.index.tolist(), province_num.values.tolist())], 'china')
c.set_global_opts(title_opts=opts.TitleOpts('调剂信息省份分布地图'), 
#                   toolbox_opts=opts.ToolboxOpts(is_show=True), 
                  visualmap_opts=opts.VisualMapOpts(max_=79)) 
c.render_notebook()


# In[61]:


print([list(z) for z in zip(province_num.index.tolist(), province_num.values.tolist())])


# In[60]:


# 改为省份全称才能正常显示
c = Map(init_opts=opts.InitOpts(width='800px', height='750px'))
c.add('',[['贵州省', 2],
 ['宁夏回族自治区', 2],
 ['甘肃省', 4],
 ['海南省', 4],
 ['内蒙古自治区', 4],
 ['新疆维吾尔自治区', 5],
 ['云南省', 6],
 ['天津市', 11],
 ['广西壮族自治区', 14],
 ['安徽省', 18],
 ['河南省', 20],
 ['福建省', 20],
 ['四川省', 21],
 ['重庆市', 22],
 ['湖南省', 23],
 ['山西省', 24],
 ['江西省', 28],
 ['河北省', 30],
 ['吉林省', 32],
 ['浙江省', 33],
 ['辽宁省', 39],
 ['陕西省', 40],
 ['上海市', 41],
 ['江苏省', 45],
 ['黑龙江省', 46],
 ['湖北省', 48],
 ['广东省', 49],
 ['山东省', 64],
 ['北京市', 79]], 'china')
c.set_global_opts(title_opts=opts.TitleOpts('调剂信息省份分布地图'), 
#                   toolbox_opts=opts.ToolboxOpts(is_show=True), 
                  visualmap_opts=opts.VisualMapOpts(max_=79)) 
c.render_notebook()


# In[ ]:




