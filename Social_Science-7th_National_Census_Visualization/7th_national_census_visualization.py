#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#" data-toc-modified-id="-1"><span class="toc-item-num">1  </span></a></span></li><li><span><a href="#Provincial" data-toc-modified-id="Provincial-2"><span class="toc-item-num">2  </span>Provincial</a></span><ul class="toc-item"><li><span><a href="#Population" data-toc-modified-id="Population-2.1"><span class="toc-item-num">2.1  </span>Population</a></span></li><li><span><a href="#Age" data-toc-modified-id="Age-2.2"><span class="toc-item-num">2.2  </span>Age</a></span></li><li><span><a href="#Gender" data-toc-modified-id="Gender-2.3"><span class="toc-item-num">2.3  </span>Gender</a></span></li><li><span><a href="#Education" data-toc-modified-id="Education-2.4"><span class="toc-item-num">2.4  </span>Education</a></span></li></ul></li></ul></div>

# In[11]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import pandas as pd
import random

from pyecharts.globals import CurrentConfig, NotebookType,OnlineHostType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
# pd.set_option('precision', 2)


# ###   
# 
# >（）Population。NationalPopulation 141178 ， 2010 year（NationalPopulation Censusdata，） 133972 ， 7206 ， 5.38%，year 0.53%， 2000 year 2010 yearyear 0.57% 0.04 minute。data，Population 10 year。  
# 
# >（）Population。National 49416 ，Population 129281 ；  2853 ，Population 11897 。Population 2.62 ， 2010 year 3.10  0.48 。，main Population day and year。  
# 
# >（）PopulationDistribution。Population 39.93%， 25.83%，  27.12%， 6.98%。 2010 year，PopulationShare  2.15 minute， 0.79 minute， 0.22 minute， 1.20 minute。Population、City。  
# 
# >（）Gender。Population 72334 ， 51.24%；Population 68844 ， 48.76%。PopulationGender（ 100，） 105.07，  2010 yearbasic ，。PopulationGender 111.3， 2010 year 6.8。 PopulationGenderStructure。  
# 
# >（）Age。0—14 Population 25338 ， 17.95%；15—59 Population  89438 ， 63.35%；60 Population 26402 ， 18.70%（where ， 65 Population 19064 ， 13.50%）。 2010 year，0—14 、15—59 、60 Populationrespectively 1.35 minute、 6.79 minute、 5.44 minute。Population，。 hour，Population，hourPopulation 。  
# 
# >（）EducationPopulation。UniversityPopulation 21836 。 2010year， 10 University 8930  15467 ，15 PopulationEducationyear 9.08 year 9.91 year， 4.08%2.67%。Education 10 yearEducationand  year，Population。  
# 
# >（）Population。Population 90199 ， 63.89%； Population 50979 ， 36.11%。 2010 year，Population 23642 ，Population 16436 ，Population 14.21 minute。 、info and  and Population，10 year，。  
# 
# >（）Population。minutePopulation 49276 ，where ，minute  11694 ，Population 37582 ，where ，Population 12484 。  2010year，minutePopulation 88.52%，minutePopulation 192.66%， Population 69.73%。，Population， Population，Population。  
# 
# >（）Population。Population 128631 ， 91.11%；Population 12547 ， 8.89%。 2010 year，Population 4.93%，Population 10.26%，Population 0.40 minute。Population，minute ，。

# In[20]:


df = pd.read_csv('./data/Population.csv', usecols=['Population', 'Unnamed: 1'])
df.drop(labels=[0, 1], axis=0, inplace=True)
df.rename(columns={'Unnamed: 1':'Population', 'Population':''}, inplace=True)

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

coord = {
    '': [114.31667, 30.51667],
    '': [113.23333, 23.16667],
    '': [116.41667, 39.91667],
    '': [121.48, 31.22],
    '': [123.38, 41.8],
    '': [115.90000, 28.68333],
    '': [104.06, 30.67],
    '': [117.27, 31.86],
    '': [108.33, 22.84],
    '': [87.68, 43.77],
    '': [118.78, 32.04],
    '': [114.48, 38.03],
    '': [120.19, 30.26],
    '': [113, 28.21],
    '': [103.82, 36.07],
    '': [119.28000, 26.08],
    '': [106.71, 26.57],
    '': [110.35, 20.02],
    '': [113.65, 34.76],
    '': [126.63, 45.75],
    '': [125.35, 43.88],
    '': [111.65, 40.82],
    '': [106.27, 38.47],
    '': [117, 36.65],
    '': [112.53, 37.87],
    '': [108.95, 34.27],
    'days': [117.2, 39.13],
    '': [91.11, 29.97],
    '': [102.73, 25.04],
    '': [106.54, 29.59],
    '': [101.74, 36.56]}

data_pair = []
for idx, row in df.iterrows():
    name = row[''].replace(' ', '')
    try:
        value = coord[name]
        value.append(float(row['Population']))
        data_pair.append([dictcode[name], value])
    except KeyError:
        if name == '':
            soldier = row['Population']
        elif name == 'National[5]':
            total = row['Population']

df = pd.read_csv('./data/NationalPopulationAge.csv')
df.drop(labels=[0, 1], axis=0, inplace=True)

data_pair_age = []
for idx, row in df.iterrows():
    data_pair_age.append([row['NationalPopulationAge'].replace('where ：', ''), float(row['Unnamed: 2'])])

df = pd.read_csv('./data/Gender.csv')
df.drop(labels=[0, 1], axis=0, inplace=True)
data_pair_sex = [('', float(df.iloc[0, 1])), ('', float(df.iloc[0, 2]))]

df = pd.read_csv('./data/10PopulationEducation.csv')
df.drop(labels=[0], axis=0, inplace=True)
data_pair_edu = [
    ('University', float(df.iloc[0, 1])/1e3), 
    ('', float(df.iloc[0, 2])/1e3), 
    ('', float(df.iloc[0, 3])/1e3), 
    ('', float(df.iloc[0, 4])/1e3),
    ('', 100-(float(df.iloc[0, 4])+float(df.iloc[0, 3])+float(df.iloc[0, 2])+float(df.iloc[0, 1]))/1e3)
    ]

data_pair_edu = [(x, round(y, 2)) for x, y in data_pair_edu]


# In[21]:


data_pair


# In[22]:


chart = Map3D(init_opts=opts.InitOpts(
    width='1000px',
    height='600px',
    theme='dark',
    bg_color='#000')
)

# 
chart.add_schema(
    maptype="china",
    ground_color='#999',
    shading="lambert",
    emphasis_label_opts=opts.LabelOpts(is_show=True),
    itemstyle_opts=opts.ItemStyleOpts(
            border_width=0.2,
            border_color="rgb(0,0,0)",
    ),
    light_opts=opts.Map3DLightOpts(
        main_shadow_quality='high',
        is_main_shadow=True,
        main_intensity=1,
        main_alpha=30,
        ambient_cubemap_texture='https://echarts.apache.org/examples/data-gl/asset/canyon.hdr',
        ambient_cubemap_diffuse_intensity=0.5,
        ambient_cubemap_specular_intensity=0.5
    ),
    post_effect_opts=opts.Map3DPostEffectOpts(
        is_enable=True,
        is_ssao_enable=True,
        ssao_radius=1,
        ssao_intensity=1
    )
)
chart.add(
    "GDP",
    data_pair=data_pair,
    type_="bar3D",
    bar_size=1.5,
    min_height=3,
    shading="lambert",
    label_opts=opts.LabelOpts(
            is_show=False,
            formatter=JsCode(
                "function(data){return data.name + ': ' + data.value[2];}"),
    )
)
chart.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        is_show=False,
        type_='color',
        dimension=2,
        min_=1e7,
        max_=1e8,
        range_color=[
            '#313695',
            '#4575b4',
            '#74add1',
            '#abd9e9',
            '#e0f3f8',
            '#ffffbf',
            '#fee090',
            '#fdae61',
            '#f46d43',
            '#d73027',
            '#a50026']
    ),
    title_opts=opts.TitleOpts(
        title="NationalProvincialPopulation",
        subtitle='dataNationalPopulationCensusdata，contains。',
        pos_left="2%",
        pos_top='1%',
        title_textstyle_opts=opts.TextStyleOpts(color='#00BFFF', font_size=20)
        ),
    tooltip_opts=opts.TooltipOpts(is_show=False),
    legend_opts=opts.LegendOpts(is_show=False),
    graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(id_='1', left="100px", bottom="100px"),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=1
                            ),
                            graphic_shape_opts=opts.GraphicShapeOpts(
                                width=200, height=80
                            ),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                # Color，，0.5
                                fill="rgba(0,0,0,0.5)",
                                line_width=4,
                                stroke="#fff",
                            ),
                        ),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=100
                            ),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                # 
                                text='NationalPopulation：{:,}\n\n：{:,}'.format(int(total), int(soldier)),
                                font="bold italic 14px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                    fill="#fff"
                                ),
                            ),
                        )
                    ],
                ), 
                
                ]
)


pie = Pie(
    init_opts=opts.InitOpts(
        theme='dark',
        width='1000px',
        height='400px',
        bg_color='rgb(0,0,0)')
)
pie.add(
    "",
    data_pair_age,
    # 
    center=["20%", "35%"],
    # ，
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.add(
    "",
    data_pair_sex,
    # 
    center=["50%", "35%"],
    # ，
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.add(
    "",
    data_pair_edu,
    # 
    center=["80%", "35%"],
    # ，
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.add(
    "",
    [('', 63.89), ('', 36.11)],
    # 
    center=["20%", "70%"],
    # ，
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.add(
    "",
    [('', 91.11), ('', 8.89)],
    # 
    center=["50%", "70%"],
    # ，
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.add(
    "",
    [('Population', 26.62), ('Population', 73.38)],
    # 
    center=["80%", "70%"],
    # ，
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.set_global_opts(
    legend_opts=opts.LegendOpts(is_show=False),
    title_opts=[dict(text='Population', left='2%', top='1%', textStyle=dict(color='#00BFFF', fontSize=20)),
                dict(
        text='Age ',
        left='20%',
        top='32%',
        textAlign='center',
        textStyle=dict(
            color='#fff',
            fontWeight='normal',
            fontSize=15)),
        dict(
        text='Gender ',
        left='50%',
        top='32%',
        textAlign='center',
        textStyle=dict(
            color='#fff',
            fontWeight='normal',
            fontSize=15)),
        dict(text='Education ', left='80%', top='32%', textAlign='center', textStyle=dict(color='#fff', fontWeight='normal', fontSize=15)),
        dict(text=' ', left='20%', top='67%', textAlign='center', textStyle=dict(color='#fff', fontWeight='normal', fontSize=15)),
        dict(text=' ', left='50%', top='67%', textAlign='center', textStyle=dict(color='#fff', fontWeight='normal', fontSize=15)),
        dict(text=' ', left='80%', top='67%', textAlign='center', textStyle=dict(color='#fff', fontWeight='normal', fontSize=15))
        ],
    graphic_opts=[
        opts.GraphicGroup(
            graphic_item=opts.GraphicItem(
                id_='2', left="center", top="40px"),
            children=[
                opts.GraphicRect(
                    graphic_item=opts.GraphicItem(
                        left="center", top="center", z=1
                    ),
                    graphic_shape_opts=opts.GraphicShapeOpts(
                        width=950, height=320
                    ),
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                        fill="rgba(0,0,0,0)",
                        line_width=5,
                        stroke="#fff",
                    ),
                )
            ],
        )
    ]
)
colors = [
        '#313695',
        '#4575b4',
        '#74add1',
        '#abd9e9',
        '#e0f3f8',
        '#ffffbf',
        '#fee090',
        '#fdae61',
        '#f46d43',
        '#d73027',
        '#a50026'
        ]
random.shuffle(colors)
pie.set_colors(colors)

page = Page()
page.add(chart).add(pie)
# page.render('./NationalPopulation.html')
page.render_notebook()


# ### Provincial  
# 
# #### Population  
# 
# 2010year-2020yearProvincialPopulationNationalShare：  
# * PopulationShare，2010yearPopulationNational2.86%，2020year2.26%；  
# 
# * PopulationShare，2010yearPopulationNationalShare7.79%，2020yearhourNationalShare8.93%，2020yearPopulation1.2；

# In[23]:


df = pd.read_csv('./data/Population.csv')
df.drop(labels=[0, 1, 2, 34], axis=0, inplace=True)
df.columns = ['', 'Population', '2020yearShare', '2010yearShare']
df['2020yearShare'] = df['2020yearShare'].astype('float')
df['2010yearShare'] = df['2010yearShare'].astype('float')
df['Share'] = df['2020yearShare'] - df['2010yearShare']

data_pair = []
for idx, row in df.iterrows():
    data_pair.append([dictcode[row[''].replace(' ', '')], round(row['Share'], 2)])


# In[25]:


map_chart = Map(
    init_opts=opts.InitOpts(
        theme='dark',
        width='1000px',
        height='700px',
        bg_color='#000')
)
map_chart.add('Share',
              data_pair=data_pair,
              maptype='china',
              # symbol
              is_map_symbol_show=False,
              label_opts=opts.LabelOpts(color='#fff'),
              itemstyle_opts={
                  'normal': {
                      'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
                      'shadowBlur': 5,  # 
                      'shadowOffsetY': 0,  # Y
                      'shadowOffsetX': 0,  # x
                      'borderColor': '#fff'
                  }
              }
              )
map_chart.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        series_index=0,
        pos_top='center',
        pos_left='2%',
        range_text=['PopulationShare：\n\n', ''],
        min_=-0.5,
        max_=0.5,
        precision=1,
        pieces=[
            {'min': 0.2, "color": 'red'},
            {'min': 0.1, 'max': 0.2, 'color': '#FF69B4'},
            {'min': 0, 'max': 0.1, 'color': '#FFB6C1'},
            {'min': -0.1, 'max': 0, 'color': '#87CEFA'},
            {'max': -0.1, 'min': -0.2, 'color': '#1E90FF'},
            {'max': -0.2, 'color': 'blue'}],
    ),
    legend_opts=opts.LegendOpts(is_show=False),
    tooltip_opts=opts.TooltipOpts(
        is_show=True,
        trigger='item',
        formatter='{b}:{c}%'
    ),
    title_opts=dict(
        text='2010-2020yearProvincialPopulationShare',
        left='2%',
        top='1%',
        textStyle=dict(
            color='#00BFFF'))
)

map_chart.render('2010-2020yearProvincialPopulationShare.html')
map_chart.render_notebook()


# #### Age

# In[26]:


df = pd.read_csv('./data/PopulationAge.csv')
df.drop(labels=[0, 1], axis=0, inplace=True)
df.columns = ['', '0—14',	'15—59',	'60', 'where 65']
df['0—14'] = df['0—14'].astype('float')
df['15—59'] = df['15—59'].astype('float')
df['60'] = df['60'].astype('float')


# In[27]:


bar = Bar(
    init_opts=opts.InitOpts(
        theme='dark',
        width='1000px',
        height='1000px',
        bg_color='#000')
)
bar.add_xaxis(
    df[''].tolist()
)
bar.add_yaxis(
    '0—14',
    df['0—14'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
            'shadowBlur': 5,  # 
            'shadowOffsetY': 2,  # Y
            'shadowOffsetX': 2,  # x
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '15—59',
    df['15—59'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
            'shadowBlur': 5,  # 
            'shadowOffsetY': 2,  # Y
            'shadowOffsetX': 2,  # x
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '60',
    df['60'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
            'shadowBlur': 5,  # 
            'shadowOffsetY': 2,  # Y
            'shadowOffsetX': 2,  # x
            'borderColor': '#fff'
        }
    }
)
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(is_show=False, max_=100),
    yaxis_opts=opts.AxisOpts(
        axisline_opts=opts.AxisLineOpts(is_show=False),
        axistick_opts=opts.AxisTickOpts(is_show=False)),
    legend_opts=opts.LegendOpts(is_show=True, pos_top='1%', pos_right='10%'),
    title_opts=opts.TitleOpts(
        title="NationalProvincialPopulationAge",
        # subtitle='dataNationalPopulationCensusdata，contains。',
        pos_left="5%",
        pos_top='1%',
        title_textstyle_opts=opts.TextStyleOpts(color='#00BFFF', font_size=20)
        ),
)

bar.reversal_axis()
bar.set_colors(['orange', 'blue', 'red'])
bar.render('./NationalProvincialPopulationAge.html')


# In[28]:


bar.render_notebook()


# #### Gender  
# * ；  
# 
# * National1.02:1，**1004**；  
# 
# * ，Age；  
# 

# In[29]:


df = pd.read_csv('./data/Gender.csv')
df.drop(labels=[0, 1], axis=0, inplace=True)
df.columns = ['', '',	'',	'Gender']
df[''] = df[''].astype('float')
df[''] = df[''].astype('float')
df.sort_values(by='', inplace=True)


# In[30]:


bar = Bar(
    init_opts=opts.InitOpts(
        theme='dark',
        width='1000px',
        height='1000px',
        bg_color='#000')
)
bar.add_xaxis(
    df[''].tolist()
)
bar.add_yaxis(
    '',
    df[''].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
            'shadowBlur': 5,  # 
            'shadowOffsetY': 2,  # Y
            'shadowOffsetX': 2,  # x
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '',
    df[''].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
            'shadowBlur': 5,  # 
            'shadowOffsetY': 2,  # Y
            'shadowOffsetX': 2,  # x
            'borderColor': '#fff'
        }
    }
)


bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(is_show=False, min_=40, max_=60),
    yaxis_opts=opts.AxisOpts(
        axisline_opts=opts.AxisLineOpts(is_show=False),
        axistick_opts=opts.AxisTickOpts(is_show=False)),
    legend_opts=opts.LegendOpts(is_show=True, pos_top='1%', pos_right='10%'),
    title_opts=opts.TitleOpts(
        title="NationalProvincialPopulationGender",
        # subtitle='dataNationalPopulationCensusdata，contains。',
        pos_left="5%",
        pos_top='1%',
        title_textstyle_opts=opts.TextStyleOpts(color='#00BFFF', font_size=20)
        ),
)

bar.reversal_axis()
bar.set_colors(['blue', 'red'])
bar.render_notebook()


# #### Education

# In[31]:


df = pd.read_csv('./data/10PopulationEducation.csv')
df.drop(labels=[0, 1], axis=0, inplace=True)
df.columns = ['', 'University', '',	'', '']
df['University'] = df['University'].astype('int') / 1e3
df[''] = df[''].astype('int') / 1e3
df[''] = df[''].astype('int') / 1e3
df[''] = df[''].astype('int') / 1e3
df[''] = 100-df['University'] - df[''] - df[''] - df['']
df.sort_values(by='University', inplace=True)


# In[ ]:





# In[32]:


bar = Bar(
    init_opts=opts.InitOpts(
        theme='dark',
        width='1000px',
        height='1000px',
        bg_color='#000')
)
bar.add_xaxis(
    df[''].tolist()
)
bar.add_yaxis(
    'University（）',
    df['University'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
            'shadowBlur': 5,  # 
            'shadowOffsetY': 2,  # Y
            'shadowOffsetX': 2,  # x
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '（）',
    df[''].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
            'shadowBlur': 5,  # 
            'shadowOffsetY': 2,  # Y
            'shadowOffsetX': 2,  # x
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '',
    df[''].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
            'shadowBlur': 5,  # 
            'shadowOffsetY': 2,  # Y
            'shadowOffsetX': 2,  # x
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '',
    df[''].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
            'shadowBlur': 5,  # 
            'shadowOffsetY': 2,  # Y
            'shadowOffsetX': 2,  # x
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '',
    [round(x, 2) for x in df[''].tolist()],
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # Color
            'shadowBlur': 5,  # 
            'shadowOffsetY': 2,  # Y
            'shadowOffsetX': 2,  # x
            'borderColor': '#fff'
        }
    }
)

bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(is_show=False, max_=100),
    yaxis_opts=opts.AxisOpts(
        axisline_opts=opts.AxisLineOpts(is_show=False),
        axistick_opts=opts.AxisTickOpts(is_show=False)),
    legend_opts=opts.LegendOpts(is_show=True, pos_top='1%', pos_right='10%'),
    title_opts=opts.TitleOpts(
        title="NationalProvincialPopulationEducation",
        # subtitle='dataNationalPopulationCensusdata，contains。',
        pos_left="5%",
        pos_top='1%',
        title_textstyle_opts=opts.TextStyleOpts(color='#00BFFF', font_size=20)
        ),
)

bar.reversal_axis()
bar.set_colors(['blue', '#1E90FF', '#87CEFA', '#FF69B4', 'red'])

bar.render_notebook()


# In[ ]:




