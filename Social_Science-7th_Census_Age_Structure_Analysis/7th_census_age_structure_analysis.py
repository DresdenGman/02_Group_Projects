#!/usr/bin/env python
# coding: utf-8

# ## 项目介绍
# 
# 
# 人口是影响地区发展的重要因素。不同地区的人口年龄结构不仅是本地区社会发展的一个体现，也是其未来发展的基础。对其了解有助于我们更好得理解社会的变化，对社会发展有更正确的认识。  
# 
# 本次从第7次人口普查数据的地区（省份）之间的人口年龄结构出发，分析人口年龄结构的差异及其影响因素。  
# 
# 结论：
# 
# - 第 7 次人口普查数据统计的2020年中国各地区（省份）的人口年龄结构，将人口分为14岁以下、15到59岁、60岁以上三个年龄段，根据年龄结构的相似度可以各个地区分为三组：  
# 	- 第 1 组：人口年龄结构特点是**低高高**，大致是 1:7:2。包括北京、天津、上海、浙江、东北三省和内蒙古。  
# 	- 第 2 组：人口年龄结构特点是**高低高**，大致是 2:6:2。包括以华北和华中为主的省份。  
# 	- 第 3 组：人口年龄结构特点特点是**高高低**，大致是 2:7:1。包括西藏、新疆、青海、广东、福建、海南等省份。  
# - 地区间的人口年龄结构和地区经济发展水平相关性不高。  
# - 14岁以下人口年龄比例差异主要受到城市化进程的影响。城市化水平越高，进度越早，则这部分人口年龄比例越容易较少。  
# - 15-59岁之间人口年龄比例差异主要受到流动人口的影响。流动人口比例越大，则这部分人口年龄比例越容易更高。

# 
# 涉及到的数据：
# 
# - 主数据，第七次全国人口普查数据  
# 	- 各地区人口年龄构成  
# 	- 各地区平均受教育年限  
# 	- 各地区人口  
# - 额外数据  
# 	- 各地区2020年GDP，来自国家统计局-数据查询  
# 	- 各地区城市化数据，来自国家统计局-数据查询和统计年鉴  
# 	- 各地区人口流动数据，来自国家统计局-统计年鉴

# In[76]:


# 显示cell运行时长
# pip install klab-autotime -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn
# %load_ext klab-autotime


# In[77]:


#pip install pandas -i https://pypi.douban.com/simple/ 
#pip install altair -i https://pypi.douban.com/simple/ 


# ## 准备阶段  
# ### 包导入和年龄结构数据加载

# In[1]:


import pandas as pd
import numpy as np
import altair as alt
from pyecharts.globals import CurrentConfig, NotebookType,OnlineHostType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK

age_dist_data_path  = "./data/各地区人口年龄构成.csv"
raw_age_df = pd.read_csv(age_dist_data_path, skiprows=2)
raw_age_df.head(50)


# 可以看到：  
# 
# - 数据范围涉及全国31个省，不包括香港、澳门和台湾省。

# ### 年龄结构数据的预处理  
# 
# - 字段重命名  
# - 数值处理

# In[2]:


column_name_map = {
    "Unnamed: 0":"region",
    "0—14 岁":"a14-",
    "15—59 岁  ":"a15_59",
    "60  岁及以上 ":"a60+",
    "其中：65 岁及以上 ":"a65+",
}

age_df = raw_age_df.rename(column_name_map,axis=1)
age_df["a65+"] = age_df["a65+"].astype(np.float64)
age_df[["a14-","a15_59","a60+","a65+"]] = age_df[["a14-","a15_59","a60+","a65+"]]/100


# In[3]:


import re

def parse_region(x):
    _x = re.sub(r"[\W\d]","",x)
    if _x[:3] in ["黑龙江","内蒙古"]:
        return _x[:3]
    else:
        return _x[:2]

assert parse_region("广 东") == "广东"
assert parse_region("全 国[1]") == "全国"
assert parse_region("黑龙江省") == "黑龙江"
assert parse_region("广西壮族自治区") == "广西"

age_df["region"] = age_df["region"].map(parse_region)

# age_df[age_df["region"] != "全国"].describe()
age_df.head()


# ### 教育数据的引入

# In[4]:


edu_data_path = "./data/各地区每10万人口中拥有的各类受教育程度人数.csv"

edu_raw_df = pd.read_csv(edu_data_path,skiprows=1)
edu_raw_df.head()


# In[5]:


edu_df = edu_raw_df.copy()
edu_df.columns = ["region","edu_college","edu_senior","edu_junior","edu_primary"]

edu_df["region"] = edu_df["region"].map(parse_region)

divide_base = 100000
edu_df[["edu_college","edu_senior","edu_junior","edu_primary"]] = edu_df[["edu_college","edu_senior","edu_junior","edu_primary"]]/divide_base

edu_df.head()


# ### 人口总数数据的引入

# In[6]:


pop_data_path = "./data/各地区人口.csv"

pop_raw_df = pd.read_csv(pop_data_path,skiprows=2)
# pop_raw_df.head(10)


# In[7]:


pop_df = pop_raw_df.copy()
new_pop_df_columns = ["region",'population','pop_percent_2020','pop_percent_2010']
if len(pop_df.columns) == 4:
    pop_df.columns = new_pop_df_columns
    pop_df.drop(['pop_percent_2020','pop_percent_2010'],axis=1,inplace=True)
pop_df["region"] = pop_df["region"].map(parse_region)

pop_df = pop_df[pop_df["region"] != "现役"]
pop_df


# ### GDP数据的引入

# In[8]:


gdp_data_path = "./data/分省年度GDP数据.csv"

gdp_raw_df = pd.read_csv(gdp_data_path)
# gdp_raw_df.head()


# In[9]:


gdp_df = gdp_raw_df.loc[:,["地区","2020年"]]
gdp_df.columns = ["region", "gdp"]
# GDP的单位：亿元
gdp_df["region"] = gdp_df["region"].map(parse_region)
gdp_df 


# ### 城市化数据的引入  
# 
# - 计算2019年，2010年，2000年三个年份的城镇化水平  
# - 计算该城市城市化水平首次突破50%，60%，70%的年份距近的年份

# In[10]:


city_pop_data_path = "./data/2005-2019年中国各地区城镇人口数量.csv"
residential_pop_data_path = "./data/2001-2020中国各地区常住人口数量.csv"
city_pop_2000_data_path = "./data/2000年中国各地区城乡人口分布.csv"

city_pop_df = pd.read_csv(city_pop_data_path)
res_pop_df = pd.read_csv(residential_pop_data_path)
city_pop_2000_df = pd.read_csv(city_pop_2000_data_path)

selected_years = [f"{year}年" for year in range(2005,2020)]

urbanization_df_05_19 = city_pop_df.set_index("地区")[selected_years]/res_pop_df.set_index("地区")[selected_years]
urbanization_df_05_19.index.name = "region"
urbanization_df_05_19.index = map(parse_region,urbanization_df_05_19.index.values)
urbanization_df_05_19

city_pop_2000_mdf = city_pop_2000_df.assign(
    region = city_pop_2000_df["地区"].map(parse_region),
    _2000 = city_pop_2000_df["城镇人口比例"] / 100
).set_index("region")[["_2000"]].rename({"_2000":"2000年"},axis=1)

urbanization_df = pd.concat([city_pop_2000_mdf,urbanization_df_05_19],axis=1).round(4)
# urbanization_df


# In[11]:


urba_first_over_year = pd.concat(
    [(urbanization_df>percent).T.apply(lambda x:x[x==True].index.min())
 for percent in [0.4,0.5,0.6,0.7]],axis=1)

urbs_over_year_columns = ["urba_over_40","urba_over_50","urba_over_60","urba_over_70"]
urba_first_over_year.columns = urbs_over_year_columns

def parse_urba_over_year(year):
    if isinstance(year,str):
        return (2020 - int(year.replace("年","")))/20
    else:
        return np.NaN
for column in urbs_over_year_columns:
    urba_first_over_year[column] = urba_first_over_year[column].map(parse_urba_over_year)
# urba_first_over_year
# urbanization_df.columns.min()


# In[12]:


urba_year_column_map = {
    "2000年":"urba_2000",
"2005年":"urba_2005",
"2010年":"urba_2010",
"2015年":"urba_2015",
"2019年":"urba_2019",
}

urba_info_df = pd.concat([
    urbanization_df[urba_year_column_map.keys()].rename(urba_year_column_map,axis=1),
    urba_first_over_year],axis=1)
urba_info_df


# ### 流动人口数据的引入

# In[13]:


from io import StringIO

# 数据来自国家统计年鉴2021
floating_pop_data_txt = '''
地区	省内	省外
北京市	4991158	8418418
天津市	2944879	3534816
河北省	16620369	3155272
山西省	11270656	1620518
内蒙古自治区	9776541	1686420
辽宁省	12822813	2847308
吉林省	9349212	1001471
黑龙江省	10720408	829176
上海市	4654606	10479652
江苏省	19671338	10308610
浙江省	13921361	16186454
安徽省	16549409	1550509
福建省	11574735	4889876
江西省	12241920	1279014
山东省	23897755	4129007
河南省	24365959	1273646
湖北省	16226947	2249614
湖南省	15998284	1577563
广东省	31012976	29622110
广西壮族自治区	11879397	1359384
海南省	2410018	1088143
重庆市	10902860	2193575
四川省	25233163	2590041
贵州省	10548217	1146546
云南省	9978920	2230394
西藏自治区	624011	407121
陕西省	11333383	1933712
甘肃省	6586817	765648
青海省	1653356	417304
宁夏回族自治区	2687551	675119
新疆维吾尔自治区	5476334	3390712
'''

floating_pop_df = pd.read_csv(StringIO(floating_pop_data_txt),sep="\t")
floating_pop_df = floating_pop_df.assign(
    region=floating_pop_df["地区"].map(parse_region),
).rename(
    {
        "省内":"floating_pop_inside",
        "省外":"floating_pop_outside"
    },
    axis=1
)[["floating_pop_inside","floating_pop_outside","region"]].set_index("region")

floating_pop_df


# ### 数据聚合

# In[14]:


# age_df.set_index("region")


# In[15]:


# df = pd.merge(pd.merge(pd.merge(age_df,edu_df,on="region"),pop_df,on="region"),gdp_df,on="region")
df = pd.concat([
    age_df.set_index("region"), 
    pop_df.set_index("region"),
    gdp_df.set_index("region"),
    edu_df.set_index("region"),
    urba_info_df,
    floating_pop_df],axis=1).drop("全国")
assert len(df.index) == 31

df = df.assign(
    gdp_avg = df["gdp"] * 10000 / df["population"],
    floating_inside_rate = df["floating_pop_inside"]/df["population"],
    floating_outside_rate = df["floating_pop_outside"]/df["population"],
    floating_rate = (df["floating_pop_inside"] + df["floating_pop_outside"])/df["population"]
)
df.index.name = "region"
df.head(10)


# In[ ]:





# ### 指标说明  
# 
# - `region`：地区，不包括香港、澳门、台湾省在内的31个中国省份  
# - `a14-`：年龄小于等于14岁的人口比例  
# - `a15_59`：年龄在14岁到59岁的人口比例  
# - `a60+`：年龄大于等于60岁的人口比例  
# - `a65+`：年龄大于等于65岁的人口比例  
# - `edu_college`：教育水平为大学（含大专及以上）的人口比例  
# - `edu_senior`：教育水平为高中（含中专）的人口比例  
# - `edu_junior`：教育水平为初中的人口比例  
# - `edu_primary`：教育水平为小学的人口比例  
# - `population`：人口数，单位为人  
# - `gdp`：国民生产总值，单位为亿元  
# - `gdp_avg`：人均国民生产总值，单位为万元  
# - `urba_2000`：2000年的城市化比例  
# - `urba_2005`：2005年的城市化比例  
# - `urba_2010`：2010年的城市化比例  
# - `urba_2015`：2015年的城市化比例  
# - `urba_2019`：2019年的城市化比例  
# - `urba_over_40`：城市化比例首次超过40%的年份的距今系数，0-1之间  
# - `urba_over_50`：城市化比例首次超过50%的年份的距今系数，0-1之间  
# - `urba_over_60`：城市化比例首次超过60%的年份的距今系数，0-1之间  
# - `urba_over_70`：城市化比例首次超过60%的年份的距今系数，0-1之间  
# - `floating_inside_rate`：来自省内的人户分离人口比例  
# - `floating_outside_rate`：来自省外的人户分离（流动人口）比例  
# - `floating_rate`：人户分离人口比例  
# 
# 城市化比例首次超过x%的年份的距今系数 = (2020 - 城市化比例首次超过x%的年份)/20，因为城市化数据只包括2000到2019之间的数据  
# 
# 除了城市化率利用了早年数据，其他数据的统计对象年份皆为 2020年

# ## 分析阶段  
# 
# ### 基于人口年龄结构的差异性，可以将中国各地区分为哪几组？  
# 
# 基于层次聚类的地区分组

# In[16]:


font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}
from pylab import mpl
# 设置中文显示字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]


# In[17]:


from scipy.cluster import hierarchy
from matplotlib import pyplot as plt

def draw_dendrogram(data, featureNames):
    model = hierarchy.linkage(data, "ward")
    # print(c)
    plt.figure(figsize=(16, 9))
    plt.title("地区之间的年龄结构层次聚类图")
    plt.xlabel("distance",font1)
    plt.ylabel("keyword")
    hierarchy.dendrogram(
        model,
        leaf_rotation=0,
        leaf_font_size=8.0,
        labels=featureNames,
        orientation="right",
    )
    plt.show()
    return model

model = draw_dendrogram(df[["a14-","a15_59","a60+"]].values.tolist(),df.index.values.tolist())


# 上图中，在谱系树中越接近，则二者之间的人口年龄结构接近。  
# 
# 基于谱系树的第三层级，可以将各地区分为三组。

# In[18]:


from scipy.cluster import hierarchy

gdf = df.assign(
    group = hierarchy.cut_tree(model,3)+1
).sort_values("group")


# In[19]:


dictcode = {'北京': '北京市',
 '天津': '天津市',
 '河北': '河北省',
 '山西': '山西省',
 '内蒙古': '内蒙古自治区',
 '辽宁': '辽宁省',
 '吉林': '吉林省',
 '黑龙江': '黑龙江省',
 '上海': '上海市',
 '江苏': '江苏省',
 '浙江': '浙江省',
 '安徽': '安徽省',
 '福建': '福建省',
 '江西': '江西省',
 '山东': '山东省',
 '河南': '河南省',
 '湖北': '湖北省',
 '湖南': '湖南省',
 '广东': '广东省',
 '广西': '广西壮族自治区',
 '海南': '海南省',
 '重庆': '重庆市',
 '四川': '四川省',
 '贵州': '贵州省',
 '云南': '云南省',
 '西藏': '西藏自治区',
 '陕西': '陕西省',
 '甘肃': '甘肃省',
 '青海': '青海省',
 '宁夏': '宁夏回族自治区',
 '新疆': '新疆维吾尔自治区'}


# In[20]:


[dictcode[x] for x in gdf.index.values]


# In[22]:


from pyecharts import options as opts
from pyecharts.charts import Map

c = (
    Map()
    .add("分组", [list(z) for z in zip([dictcode[x] for x in gdf.index.values], gdf["group"].values * 1.0)], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国人口年龄结构分组地图"),
        visualmap_opts=opts.VisualMapOpts(max_=3),
    )
)
c.render('中国人口年龄结构分组地图.html')
c.render_notebook()


# 三组的地理分布情况  
# 
# - 第1组：绿色  
# - 第2组：黄色  
# - 第3组：红色

# In[23]:


gdf_summary = gdf.groupby("group").agg(
    a14=("a14-","mean"),
    a15_59=("a15_59","mean"),
    a60=("a60+","mean"),
).round(2)

alt.Chart(gdf_summary.stack().reset_index().rename({"level_1":"metric",0:"value"},axis=1)).mark_bar().encode(
    x="metric",
    y="value",
    tooltip=["metric:O","value:Q"]
).properties(
    width=200
).facet(
    column="group"
)


# 上图是不同组的平均人口年龄结构，可以看到  
# 
# - 第 1 组：人口年龄结构特点是**低高高**，大致是 1:7:2。既有北京、天津、上海、浙江等经济发达地区，也有东北三省和内蒙古。  
# - 第 2 组：人口年龄结构特点是**高低高**，大致是 2:6:2。以华北和华中为主的省份。  
# - 第 3 组：人口年龄结构特点特点是**高高低**，大致是 2:7:1。既有西藏、新疆、青海、甘肃、云南等西部省份，也有广东、福建、海南等东南部省份。  
# 
# 虽然被归为同一个组，但是同组的不同地区的经济发展水平、自然地理环境都有着较大的差异。下面探索与人口年龄结构差异有关的影响因素。

# ### 对于人口年龄结构的影响因素可能有哪些？  
# 通过相关性来观察

# In[24]:


# import seaborn as sns
corr = df.drop(["floating_pop_inside","floating_pop_outside"],axis=1).corr().round(2)
corr.style.background_gradient(cmap='YlOrRd')
# Set up the matplotlib figure


# 通过对不同年龄结构比例和教育水平、人均GDP、城市化进度、流动人口比例等数据的相关性，发现：  
# 
# - 14岁以下人口比例和城市化进度有着较高的相关系数。其中和**城市化比例超过50%的年份的距今系数**的相关系数达到 -0.81。也就是城市化水平越早达到50%，该地区的14岁以下人口比例越可能较低。  
# - 15到59岁人口比例和流动人口比例有着较高的相关系数，其中人户分离比例的相关系数达到0.69。  
# - 60岁以上人口比例和城市化进度有着较高的相关系数，其中与2019年的城市化水平相关系数为0.62。  
# - 人口年龄结构和人均GDP的相关性不高。对于14岁以下年龄的人口比例的相关系数只有-0.53，对于60岁以上年龄的人口比例的相关系数只有0.29。  
# 
# 结合人口结构变化的一些逻辑，我们对人口年龄结构的差异给出分析结果：  
# 
# - 14岁以下人口年龄比例差异主要受到城市化进展的影响。城市化水平越高，进度越早，则这部分人口年龄比例更容易较少。城市化通过影响人们的婚姻和生育观念影响了儿童人口的数量。  
# - 15-59岁之间人口年龄比例差异主要受到流动人口的影响。流动人口比例越大，则对这部分人口年龄比例会更高。流动人口体现了地区在吸引其他地区人口，特别是目前以经济因素为主导的人口流动下，会吸引更多的劳动力人口。  
#  

# In[25]:


# gdf.groupby("group").agg(
#     a14_mean=("a14-","mean"),
#     a15_59_mean=("a15_59","mean"),
#     a60_mean=("a60+","mean"),
#     edu_college_mean=("edu_college","mean"),
#     edu_senior_mean=("edu_senior","mean"),
#     urba_over_50_mean=("urba_over_50","mean"),
#     urba_2000_mean=("urba_2000","mean"),
#     urba_2019_mean=("urba_2019","mean"),
#     floating_outside_rate=("floating_outside_rate","mean"),
#     floating_rate=("floating_rate","mean")
# )


# ### 城市化进度对于人口年龄结构影响的观察

# In[26]:


alt.Chart(gdf.reset_index()).mark_point().encode(
    x="urba_over_50",
    y="a14-",
    color="group:N",
    tooltip=["region:N","urba_over_50:Q","a14-:Q"]
).properties(
    title="城市化进度与14岁以下人口年龄结构比例的关系"
)


# 上图的横坐标为城市化比例超过50%的年份的距今系数，也就是 (2020 - 城市化首次比例超过50%的年份)/20，数值越大则越早实现城市化比例超过50%。纵坐标为年龄小于等于14岁的人口比例。  
# 
# 可以看到  
# 
# - 第1组地区的特点是14岁以下人口比例较少，且普遍是城市化较早突破50%的地区。

# ### 流动人口对于人口年龄结构影响的观察

# In[27]:


alt.Chart(gdf.reset_index()).mark_point().encode(
    alt.Y("a15_59",scale=alt.Scale(domain=[0.5,0.7])),
    x="floating_outside_rate",
    color="group:N",
    tooltip=["region:O","floating_outside_rate:Q","a14-:Q"]
).properties(
    title="流动人口比例与15岁到59岁之间人口年龄结构比例的关系"
)


# 上图的横坐标为流动人口比例，纵坐标为年龄在14岁到59岁的人口比例。  
# 
# 因为第2组和第3组的区别主要在于15岁到59岁之间的人口年龄比例，所以我们重点看这两组的区别。可以发现：  
# - 15岁到59岁之间人口年龄比例更高的第3组，其流动人口比例也普遍更高。  
# 
# ## 结束
