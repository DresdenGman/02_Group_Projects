#!/usr/bin/env python
# coding: utf-8

# ## Project Introduction
# 
# 
# Population。different PopulationAgeStructure，。，。  
# 
# 7PopulationCensusdata（）PopulationAgeStructure，analysisPopulationAgeStructure。  
# 
# Conclusion：
# 
# -  7 PopulationCensusdata2020year（）PopulationAgeStructure，Populationminute14、1559、60Age，based on AgeStructureminute：  
# 	-  1 ：PopulationAgeStructure****， 1:7:2。including 、days、、、 and 。  
# 	-  2 ：PopulationAgeStructure****， 2:6:2。including  and 。  
# 	-  3 ：PopulationAgeStructure****， 2:7:1。including 、、、、、。  
# - PopulationAgeStructure and Correlation。  
# - 14PopulationAgemain City。City，，minutePopulationAge。  
# - 15-59PopulationAgemain Population。Population，minutePopulationAge。

# 
# data：
# 
# - data，NationalPopulationCensusdata  
# 	- PopulationAge  
# 	- Educationyear  
# 	- Population  
# - data  
# 	- 2020yearGDP，-data  
# 	- Citydata，-data and year  
# 	- Populationdata，-year

# In[76]:


# cellhour
# pip install klab-autotime -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn
# %load_ext klab-autotime


# In[77]:


#pip install pandas -i https://pypi.douban.com/simple/ 
#pip install altair -i https://pypi.douban.com/simple/ 


# ##   
# ### import and AgeStructuredata

# In[1]:


import pandas as pd
import numpy as np
import altair as alt
from pyecharts.globals import CurrentConfig, NotebookType,OnlineHostType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK

age_dist_data_path  = "./data/PopulationAge.csv"
raw_age_df = pd.read_csv(age_dist_data_path, skiprows=2)
raw_age_df.head(50)


# We can see ：  
# 
# - dataNational31，including 、 and 。

# ### AgeStructuredataprocessing  
# 
# -   
# - processing

# In[2]:


column_name_map = {
    "Unnamed: 0":"region",
    "0—14 ":"a14-",
    "15—59   ":"a15_59",
    "60   ":"a60+",
    "where ：65  ":"a65+",
}

age_df = raw_age_df.rename(column_name_map,axis=1)
age_df["a65+"] = age_df["a65+"].astype(np.float64)
age_df[["a14-","a15_59","a60+","a65+"]] = age_df[["a14-","a15_59","a60+","a65+"]]/100


# In[3]:


import re

def parse_region(x):
    _x = re.sub(r"[\W\d]","",x)
    if _x[:3] in ["",""]:
        return _x[:3]
    else:
        return _x[:2]

assert parse_region(" ") == ""
assert parse_region(" [1]") == "National"
assert parse_region("") == ""
assert parse_region("") == ""

age_df["region"] = age_df["region"].map(parse_region)

# age_df[age_df["region"] != "National"].describe()
age_df.head()


# ### Educationdata

# In[4]:


edu_data_path = "./data/10PopulationEducation.csv"

edu_raw_df = pd.read_csv(edu_data_path,skiprows=1)
edu_raw_df.head()


# In[5]:


edu_df = edu_raw_df.copy()
edu_df.columns = ["region","edu_college","edu_senior","edu_junior","edu_primary"]

edu_df["region"] = edu_df["region"].map(parse_region)

divide_base = 100000
edu_df[["edu_college","edu_senior","edu_junior","edu_primary"]] = edu_df[["edu_college","edu_senior","edu_junior","edu_primary"]]/divide_base

edu_df.head()


# ### Populationdata

# In[6]:


pop_data_path = "./data/Population.csv"

pop_raw_df = pd.read_csv(pop_data_path,skiprows=2)
# pop_raw_df.head(10)


# In[7]:


pop_df = pop_raw_df.copy()
new_pop_df_columns = ["region",'population','pop_percent_2020','pop_percent_2010']
if len(pop_df.columns) == 4:
    pop_df.columns = new_pop_df_columns
    pop_df.drop(['pop_percent_2020','pop_percent_2010'],axis=1,inplace=True)
pop_df["region"] = pop_df["region"].map(parse_region)

pop_df = pop_df[pop_df["region"] != ""]
pop_df


# ### GDPdata

# In[8]:


gdp_data_path = "./data/minuteyearGDPdata.csv"

gdp_raw_df = pd.read_csv(gdp_data_path)
# gdp_raw_df.head()


# In[9]:


gdp_df = gdp_raw_df.loc[:,["","2020year"]]
gdp_df.columns = ["region", "gdp"]
# GDPunit：
gdp_df["region"] = gdp_df["region"].map(parse_region)
gdp_df 


# ### Citydata  
# 
# - calculate2019year，2010year，2000yearYear  
# - calculateCityCity50%，60%，70%YearYear

# In[10]:


city_pop_data_path = "./data/2005-2019yearPopulationCount.csv"
residential_pop_data_path = "./data/2001-2020PopulationCount.csv"
city_pop_2000_data_path = "./data/2000yearPopulationDistribution.csv"

city_pop_df = pd.read_csv(city_pop_data_path)
res_pop_df = pd.read_csv(residential_pop_data_path)
city_pop_2000_df = pd.read_csv(city_pop_2000_data_path)

selected_years = [f"{year}year" for year in range(2005,2020)]

urbanization_df_05_19 = city_pop_df.set_index("")[selected_years]/res_pop_df.set_index("")[selected_years]
urbanization_df_05_19.index.name = "region"
urbanization_df_05_19.index = map(parse_region,urbanization_df_05_19.index.values)
urbanization_df_05_19

city_pop_2000_mdf = city_pop_2000_df.assign(
    region = city_pop_2000_df[""].map(parse_region),
    _2000 = city_pop_2000_df["Population"] / 100
).set_index("region")[["_2000"]].rename({"_2000":"2000year"},axis=1)

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
        return (2020 - int(year.replace("year","")))/20
    else:
        return np.NaN
for column in urbs_over_year_columns:
    urba_first_over_year[column] = urba_first_over_year[column].map(parse_urba_over_year)
# urba_first_over_year
# urbanization_df.columns.min()


# In[12]:


urba_year_column_map = {
    "2000year":"urba_2000",
"2005year":"urba_2005",
"2010year":"urba_2010",
"2015year":"urba_2015",
"2019year":"urba_2019",
}

urba_info_df = pd.concat([
    urbanization_df[urba_year_column_map.keys()].rename(urba_year_column_map,axis=1),
    urba_first_over_year],axis=1)
urba_info_df


# ### Populationdata

# In[13]:


from io import StringIO

# datayear2021
floating_pop_data_txt = '''
		
	4991158	8418418
days	2944879	3534816
	16620369	3155272
	11270656	1620518
	9776541	1686420
	12822813	2847308
	9349212	1001471
	10720408	829176
	4654606	10479652
	19671338	10308610
	13921361	16186454
	16549409	1550509
	11574735	4889876
	12241920	1279014
	23897755	4129007
	24365959	1273646
	16226947	2249614
	15998284	1577563
	31012976	29622110
	11879397	1359384
	2410018	1088143
	10902860	2193575
	25233163	2590041
	10548217	1146546
	9978920	2230394
	624011	407121
	11333383	1933712
	6586817	765648
	1653356	417304
	2687551	675119
	5476334	3390712
'''

floating_pop_df = pd.read_csv(StringIO(floating_pop_data_txt),sep="\t")
floating_pop_df = floating_pop_df.assign(
    region=floating_pop_df[""].map(parse_region),
).rename(
    {
        "":"floating_pop_inside",
        "":"floating_pop_outside"
    },
    axis=1
)[["floating_pop_inside","floating_pop_outside","region"]].set_index("region")

floating_pop_df


# ### data

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
    floating_pop_df],axis=1).drop("National")
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





# ### description  
# 
# - `region`：，including 、、31  
# - `a14-`：Age14Population  
# - `a15_59`：Age1459Population  
# - `a60+`：Age60Population  
# - `a65+`：Age65Population  
# - `edu_college`：EducationUniversity（）Population  
# - `edu_senior`：Education（）Population  
# - `edu_junior`：EducationPopulation  
# - `edu_primary`：EducationPopulation  
# - `population`：Population，unit  
# - `gdp`：，unit  
# - `gdp_avg`：，unit  
# - `urba_2000`：2000yearCity  
# - `urba_2005`：2005yearCity  
# - `urba_2010`：2010yearCity  
# - `urba_2015`：2015yearCity  
# - `urba_2019`：2019yearCity  
# - `urba_over_40`：City40%Year，0-1  
# - `urba_over_50`：City50%Year，0-1  
# - `urba_over_60`：City60%Year，0-1  
# - `urba_over_70`：City60%Year，0-1  
# - `floating_inside_rate`：minutePopulation  
# - `floating_outside_rate`：minute（Population）  
# - `floating_rate`：minutePopulation  
# 
# Cityx%Year = (2020 - Cityx%Year)/20， because Citydataincluding 20002019data  
# 
# Cityutilizing yeardata，dataYear 2020year

# ## analysis  
# 
# ### based on PopulationAgeStructure，minute？  
# 
# based on clusteringminute

# In[16]:


font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}
from pylab import mpl
# 
mpl.rcParams["font.sans-serif"] = ["SimHei"]


# In[17]:


from scipy.cluster import hierarchy
from matplotlib import pyplot as plt

def draw_dendrogram(data, featureNames):
    model = hierarchy.linkage(data, "ward")
    # print(c)
    plt.figure(figsize=(16, 9))
    plt.title("AgeStructureclustering")
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


# ，，PopulationAgeStructure。  
# 
# based on ，minute。

# In[18]:


from scipy.cluster import hierarchy

gdf = df.assign(
    group = hierarchy.cut_tree(model,3)+1
).sort_values("group")


# In[19]:


dictcode = {'': '',
 'days': 'days',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': '',
 '': ''}


# In[20]:


[dictcode[x] for x in gdf.index.values]


# In[22]:


from pyecharts import options as opts
from pyecharts.charts import Map

c = (
    Map()
    .add("minute", [list(z) for z in zip([dictcode[x] for x in gdf.index.values], gdf["group"].values * 1.0)], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="PopulationAgeStructureminute"),
        visualmap_opts=opts.VisualMapOpts(max_=3),
    )
)
c.render('PopulationAgeStructureminute.html')
c.render_notebook()


# Distribution  
# 
# - 1：  
# - 2：  
# - 3：

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


# different PopulationAgeStructure，We can see   
# 
# -  1 ：PopulationAgeStructure****， 1:7:2。、days、、， and 。  
# -  2 ：PopulationAgeStructure****， 2:6:2。 and 。  
# -  3 ：PopulationAgeStructure****， 2:7:1。、、、、，、、。  
# 
#  although ， but different 、。PopulationAgeStructure。

# ### PopulationAgeStructure？  
# through Correlation

# In[24]:


# import seaborn as sns
corr = df.drop(["floating_pop_inside","floating_pop_outside"],axis=1).corr().round(2)
corr.style.background_gradient(cmap='YlOrRd')
# Set up the matplotlib figure


# through different AgeStructure and Education、GDP、City、PopulationdataCorrelation，：  
# 
# - 14Population and Cityrelated 。where  and **City50%Year**related  -0.81。City50%，14Population。  
# - 1559Population and Populationrelated ，where minuterelated 0.69。  
# - 60Population and Cityrelated ，where 2019yearCityrelated 0.62。  
# - PopulationAgeStructure and GDPCorrelation。14AgePopulationrelated -0.53，60AgePopulationrelated 0.29。  
# 
# PopulationStructure，PopulationAgeStructureanalysisresult：  
# 
# - 14PopulationAgemain City。City，，minutePopulationAge。Citythrough Marriage and PopulationCount。  
# - 15-59PopulationAgemain Population。Population，minutePopulationAge。PopulationPopulation，Population，Population。  
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


# ### CityPopulationAgeStructure

# In[26]:


alt.Chart(gdf.reset_index()).mark_point().encode(
    x="urba_over_50",
    y="a14-",
    color="group:N",
    tooltip=["region:N","urba_over_50:Q","a14-:Q"]
).properties(
    title="City14PopulationAgeStructure"
)


# City50%Year， (2020 - City50%Year)/20，implement City50%。Age14Population。  
# 
# We can see   
# 
# - 114Population，City50%。

# ### PopulationPopulationAgeStructure

# In[27]:


alt.Chart(gdf.reset_index()).mark_point().encode(
    alt.Y("a15_59",scale=alt.Scale(domain=[0.5,0.7])),
    x="floating_outside_rate",
    color="group:N",
    tooltip=["region:O","floating_outside_rate:Q","a14-:Q"]
).properties(
    title="Population1559PopulationAgeStructure"
)


# Population，Age1459Population。  
# 
#  because 2 and 3main 1559PopulationAge， so 。：  
# - 1559PopulationAge3，Population。  
# 
# ## 
