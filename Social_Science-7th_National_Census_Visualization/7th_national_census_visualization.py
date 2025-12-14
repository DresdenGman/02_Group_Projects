#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#概览" data-toc-modified-id="概览-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>概览</a></span></li><li><span><a href="#各省" data-toc-modified-id="各省-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>各省</a></span><ul class="toc-item"><li><span><a href="#人口变化" data-toc-modified-id="人口变化-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>人口变化</a></span></li><li><span><a href="#年龄构成" data-toc-modified-id="年龄构成-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>年龄构成</a></span></li><li><span><a href="#性别构成" data-toc-modified-id="性别构成-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>性别构成</a></span></li><li><span><a href="#教育程度" data-toc-modified-id="教育程度-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>教育程度</a></span></li></ul></li></ul></div>

# In[11]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import pandas as pd
import random

from pyecharts.globals import CurrentConfig, NotebookType,OnlineHostType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
# pd.set_option('precision', 2)


# ### 概览  
# 
# >（一）人口总量。全国人口共 141178 万人，与 2010 年（第六次全国人口 普查数据，下同）的 133972 万人相比，增加 7206 万人，增长 5.38%，年平均增长率为 0.53%，比 2000 年到 2010 年的年平均增长率 0.57%下降 0.04 个百分点。数据表明，我国人口 10 年来继续保持低速增长态势。  
# 
# >（二）户别人口。全国共有家庭户 49416 万户，家庭户人口为 129281 万人； 集体户 2853 万户，集体户人口为 11897 万人。平均每个家庭户的人口为 2.62 人，比 2010 年的 3.10 人减少 0.48 人。家庭户规模继续缩小，主要是受我国人口流动 日趋频繁和住房条件改善年轻人婚后独立居住等因素的影响。  
# 
# >（三）人口地区分布。东部地区人口占 39.93%，中部地区占 25.83%，西部 地区占 27.12%，东北地区占 6.98%。与 2010 年相比，东部地区人口所占比重上 升 2.15 个百分点，中部地区下降 0.79 个百分点，西部地区上升 0.22 个百分点，东北地区下降 1.20 个百分点。人口向经济发达区域、城市群进一步集聚。  
# 
# >（四）性别构成。男性人口为 72334 万人，占 51.24%；女性人口为 68844 万人，占 48.76%。总人口性别比（以女性为 100，男性对女性的比例）为 105.07， 与 2010 年基本持平，略有降低。出生人口性别比为 111.3，较 2010 年下降 6.8。 我国人口的性别结构持续改善。  
# 
# >（五）年龄构成。0—14 岁人口为 25338 万人，占 17.95%；15—59 岁人口 为 89438 万人，占 63.35%；60 岁及以上人口为 26402 万人，占 18.70%（其中， 65 岁及以上人口为 19064 万人，占 13.50%）。与 2010 年相比，0—14 岁、15—59 岁、60 岁及以上人口的比重分别上升 1.35 个百分点、下降 6.79 个百分点、上升 5.44 个百分点。我国少儿人口比重回升，生育政策调整取得了积极成效。同 时，人口老龄化程度进一步加深，未来一段时期将持续面临人口长期均衡发展的 压力。  
# 
# >（六）受教育程度人口。具有大学文化程度的人口为 21836 万人。与 2010年相比，每 10 万人中具有大学文化程度的由 8930 人上升为 15467 人，15 岁及以上人口的平均受教育年限由 9.08 年提高至 9.91 年，文盲率由 4.08%下降为2.67%。受教育状况的持续改善反映了 10 年来我国大力发展高等教育以及扫除青 壮年文盲等措施取得了积极成效，人口素质不断提高。  
# 
# >（七）城乡人口。居住在城镇的人口为 90199 万人，占 63.89%；居住在乡 村的人口为 50979 万人，占 36.11%。与 2010 年相比，城镇人口增加 23642 万人，乡村人口减少 16436 万人，城镇人口比重上升 14.21 个百分点。随着我国新型工 业化、信息化和农业现代化的深入发展和农业转移人口市民化政策落实落地，10 年来我国新型城镇化进程稳步推进，城镇化建设取得了历史性成就。  
# 
# >（八）流动人口。人户分离人口为 49276 万人，其中，市辖区内人户分离人 口为 11694 万人，流动人口为 37582 万人，其中，跨省流动人口为 12484 万人。 与 2010年相比，人户分离人口增长 88.52%，市辖区内人户分离人口增长 192.66%， 流动人口增长 69.73%。我国经济社会持续发展，为人口的迁移流动创造了条件， 人口流动趋势更加明显，流动人口规模进一步扩大。  
# 
# >（九）民族人口。汉族人口为 128631 万人，占 91.11%；各少数民族人口为 12547 万人，占 8.89%。与 2010 年相比，汉族人口增长 4.93%，各少数民族人口增长 10.26%，少数民族人口比重上升 0.40 个百分点。民族人口稳步增长，充分 体现了在中国共产党领导下，我国各民族全面发展进步的面貌。

# In[20]:


df = pd.read_csv('./data/各地区人口.csv', usecols=['各地区人口', 'Unnamed: 1'])
df.drop(labels=[0, 1], axis=0, inplace=True)
df.rename(columns={'Unnamed: 1':'人口数', '各地区人口':'地区'}, inplace=True)

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

coord = {
    '湖北': [114.31667, 30.51667],
    '广东': [113.23333, 23.16667],
    '北京': [116.41667, 39.91667],
    '上海': [121.48, 31.22],
    '辽宁': [123.38, 41.8],
    '江西': [115.90000, 28.68333],
    '四川': [104.06, 30.67],
    '安徽': [117.27, 31.86],
    '广西': [108.33, 22.84],
    '新疆': [87.68, 43.77],
    '江苏': [118.78, 32.04],
    '河北': [114.48, 38.03],
    '浙江': [120.19, 30.26],
    '湖南': [113, 28.21],
    '甘肃': [103.82, 36.07],
    '福建': [119.28000, 26.08],
    '贵州': [106.71, 26.57],
    '海南': [110.35, 20.02],
    '河南': [113.65, 34.76],
    '黑龙江': [126.63, 45.75],
    '吉林': [125.35, 43.88],
    '内蒙古': [111.65, 40.82],
    '宁夏': [106.27, 38.47],
    '山东': [117, 36.65],
    '山西': [112.53, 37.87],
    '陕西': [108.95, 34.27],
    '天津': [117.2, 39.13],
    '西藏': [91.11, 29.97],
    '云南': [102.73, 25.04],
    '重庆': [106.54, 29.59],
    '青海': [101.74, 36.56]}

data_pair = []
for idx, row in df.iterrows():
    name = row['地区'].replace(' ', '')
    try:
        value = coord[name]
        value.append(float(row['人口数']))
        data_pair.append([dictcode[name], value])
    except KeyError:
        if name == '现役军人':
            soldier = row['人口数']
        elif name == '全国[5]':
            total = row['人口数']

df = pd.read_csv('./data/全国人口年龄构成.csv')
df.drop(labels=[0, 1], axis=0, inplace=True)

data_pair_age = []
for idx, row in df.iterrows():
    data_pair_age.append([row['全国人口年龄构成'].replace('其中：', ''), float(row['Unnamed: 2'])])

df = pd.read_csv('./data/各地区性别构成.csv')
df.drop(labels=[0, 1], axis=0, inplace=True)
data_pair_sex = [('男性', float(df.iloc[0, 1])), ('女性', float(df.iloc[0, 2]))]

df = pd.read_csv('./data/各地区每10万人口中拥有的各类受教育程度人数.csv')
df.drop(labels=[0], axis=0, inplace=True)
data_pair_edu = [
    ('大学', float(df.iloc[0, 1])/1e3), 
    ('高中', float(df.iloc[0, 2])/1e3), 
    ('初中', float(df.iloc[0, 3])/1e3), 
    ('小学', float(df.iloc[0, 4])/1e3),
    ('其他', 100-(float(df.iloc[0, 4])+float(df.iloc[0, 3])+float(df.iloc[0, 2])+float(df.iloc[0, 1]))/1e3)
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

# 引用添加的地图
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
        title="全国各省人口统计",
        subtitle='数据来自全国第七次人口普查数据，未包含港澳台地区。',
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
                                # 颜色配置，这里设置为黑色，透明度为0.5
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
                                # 要显示的文本
                                text='全国人口：{:,}\n\n现役军人：{:,}'.format(int(total), int(soldier)),
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
    # 指定饼图中心位置
    center=["20%", "35%"],
    # 将饼图尺寸相应缩小，不然饼图会重叠
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.add(
    "",
    data_pair_sex,
    # 指定饼图中心位置
    center=["50%", "35%"],
    # 将饼图尺寸相应缩小，不然饼图会重叠
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.add(
    "",
    data_pair_edu,
    # 指定饼图中心位置
    center=["80%", "35%"],
    # 将饼图尺寸相应缩小，不然饼图会重叠
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.add(
    "",
    [('城镇', 63.89), ('农村', 36.11)],
    # 指定饼图中心位置
    center=["20%", "70%"],
    # 将饼图尺寸相应缩小，不然饼图会重叠
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.add(
    "",
    [('汉族', 91.11), ('少数民族', 8.89)],
    # 指定饼图中心位置
    center=["50%", "70%"],
    # 将饼图尺寸相应缩小，不然饼图会重叠
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.add(
    "",
    [('流动人口', 26.62), ('非流动人口', 73.38)],
    # 指定饼图中心位置
    center=["80%", "70%"],
    # 将饼图尺寸相应缩小，不然饼图会重叠
    radius=["15%", "25%"],
    label_opts=opts.LabelOpts(formatter='{b}\n{c}%')
)

pie.set_global_opts(
    legend_opts=opts.LegendOpts(is_show=False),
    title_opts=[dict(text='人口画像', left='2%', top='1%', textStyle=dict(color='#00BFFF', fontSize=20)),
                dict(
        text='年龄 ',
        left='20%',
        top='32%',
        textAlign='center',
        textStyle=dict(
            color='#fff',
            fontWeight='normal',
            fontSize=15)),
        dict(
        text='性别 ',
        left='50%',
        top='32%',
        textAlign='center',
        textStyle=dict(
            color='#fff',
            fontWeight='normal',
            fontSize=15)),
        dict(text='教育 ', left='80%', top='32%', textAlign='center', textStyle=dict(color='#fff', fontWeight='normal', fontSize=15)),
        dict(text='户籍 ', left='20%', top='67%', textAlign='center', textStyle=dict(color='#fff', fontWeight='normal', fontSize=15)),
        dict(text='民族 ', left='50%', top='67%', textAlign='center', textStyle=dict(color='#fff', fontWeight='normal', fontSize=15)),
        dict(text='流动 ', left='80%', top='67%', textAlign='center', textStyle=dict(color='#fff', fontWeight='normal', fontSize=15))
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
# page.render('./全国人口画像.html')
page.render_notebook()


# ### 各省  
# 
# #### 人口变化  
# 
# 从2010年-2020年各省人口的全国占比变化来看：  
# * 东三省人口占比下降最多，黑龙江在2010年人口占全国2.86%，在2020年下降到2.26%；  
# 
# * 广东人口占比上涨最多，在2010年人口全国占比为7.79%，在2020年的时候全国占比达到了8.93%，2020年人口数1.2亿；

# In[23]:


df = pd.read_csv('./data/各地区人口.csv')
df.drop(labels=[0, 1, 2, 34], axis=0, inplace=True)
df.columns = ['地区', '人口数', '2020年占比', '2010年占比']
df['2020年占比'] = df['2020年占比'].astype('float')
df['2010年占比'] = df['2010年占比'].astype('float')
df['占比变化'] = df['2020年占比'] - df['2010年占比']

data_pair = []
for idx, row in df.iterrows():
    data_pair.append([dictcode[row['地区'].replace(' ', '')], round(row['占比变化'], 2)])


# In[25]:


map_chart = Map(
    init_opts=opts.InitOpts(
        theme='dark',
        width='1000px',
        height='700px',
        bg_color='#000')
)
map_chart.add('占比变化',
              data_pair=data_pair,
              maptype='china',
              # 关闭symbol的显示
              is_map_symbol_show=False,
              label_opts=opts.LabelOpts(color='#fff'),
              itemstyle_opts={
                  'normal': {
                      'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
                      'shadowBlur': 5,  # 阴影大小
                      'shadowOffsetY': 0,  # Y轴方向阴影偏移
                      'shadowOffsetX': 0,  # x轴方向阴影偏移
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
        range_text=['人口占比变化：\n\n流入', '流出'],
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
        text='2010-2020年各省人口占比变化',
        left='2%',
        top='1%',
        textStyle=dict(
            color='#00BFFF'))
)

map_chart.render('2010-2020年各省人口占比变化.html')
map_chart.render_notebook()


# #### 年龄构成

# In[26]:


df = pd.read_csv('./data/各地区人口年龄构成.csv')
df.drop(labels=[0, 1], axis=0, inplace=True)
df.columns = ['地区', '0—14岁',	'15—59岁',	'60岁及以上', '其中65岁及以上']
df['0—14岁'] = df['0—14岁'].astype('float')
df['15—59岁'] = df['15—59岁'].astype('float')
df['60岁及以上'] = df['60岁及以上'].astype('float')


# In[27]:


bar = Bar(
    init_opts=opts.InitOpts(
        theme='dark',
        width='1000px',
        height='1000px',
        bg_color='#000')
)
bar.add_xaxis(
    df['地区'].tolist()
)
bar.add_yaxis(
    '0—14岁',
    df['0—14岁'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
            'shadowBlur': 5,  # 阴影大小
            'shadowOffsetY': 2,  # Y轴方向阴影偏移
            'shadowOffsetX': 2,  # x轴方向阴影偏移
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '15—59岁',
    df['15—59岁'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
            'shadowBlur': 5,  # 阴影大小
            'shadowOffsetY': 2,  # Y轴方向阴影偏移
            'shadowOffsetX': 2,  # x轴方向阴影偏移
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '60岁及以上',
    df['60岁及以上'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
            'shadowBlur': 5,  # 阴影大小
            'shadowOffsetY': 2,  # Y轴方向阴影偏移
            'shadowOffsetX': 2,  # x轴方向阴影偏移
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
        title="全国各省人口年龄构成",
        # subtitle='数据来自全国第七次人口普查数据，未包含港澳台地区。',
        pos_left="5%",
        pos_top='1%',
        title_textstyle_opts=opts.TextStyleOpts(color='#00BFFF', font_size=20)
        ),
)

bar.reversal_axis()
bar.set_colors(['orange', 'blue', 'red'])
bar.render('./全国各省人口年龄构成.html')


# In[28]:


bar.render_notebook()


# #### 性别构成  
# * 广东的朋友找对象可能最难；  
# 
# * 全国的男女比例大概1.02:1，大约是**每100个男性中有4个得打光棍**；  
# 
# * 考虑到女性平均寿命高于男性，适婚年龄的男女比例可能更恐怖；  
# 

# In[29]:


df = pd.read_csv('./data/各地区性别构成.csv')
df.drop(labels=[0, 1], axis=0, inplace=True)
df.columns = ['地区', '女',	'男',	'性别比']
df['男'] = df['男'].astype('float')
df['女'] = df['女'].astype('float')
df.sort_values(by='女', inplace=True)


# In[30]:


bar = Bar(
    init_opts=opts.InitOpts(
        theme='dark',
        width='1000px',
        height='1000px',
        bg_color='#000')
)
bar.add_xaxis(
    df['地区'].tolist()
)
bar.add_yaxis(
    '男性',
    df['男'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
            'shadowBlur': 5,  # 阴影大小
            'shadowOffsetY': 2,  # Y轴方向阴影偏移
            'shadowOffsetX': 2,  # x轴方向阴影偏移
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '女性',
    df['女'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
            'shadowBlur': 5,  # 阴影大小
            'shadowOffsetY': 2,  # Y轴方向阴影偏移
            'shadowOffsetX': 2,  # x轴方向阴影偏移
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
        title="全国各省人口性别构成",
        # subtitle='数据来自全国第七次人口普查数据，未包含港澳台地区。',
        pos_left="5%",
        pos_top='1%',
        title_textstyle_opts=opts.TextStyleOpts(color='#00BFFF', font_size=20)
        ),
)

bar.reversal_axis()
bar.set_colors(['blue', 'red'])
bar.render_notebook()


# #### 教育程度

# In[31]:


df = pd.read_csv('./data/各地区每10万人口中拥有的各类受教育程度人数.csv')
df.drop(labels=[0, 1], axis=0, inplace=True)
df.columns = ['地区', '大学', '高中',	'初中', '小学']
df['大学'] = df['大学'].astype('int') / 1e3
df['高中'] = df['高中'].astype('int') / 1e3
df['初中'] = df['初中'].astype('int') / 1e3
df['小学'] = df['小学'].astype('int') / 1e3
df['其他'] = 100-df['大学'] - df['高中'] - df['初中'] - df['小学']
df.sort_values(by='大学', inplace=True)


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
    df['地区'].tolist()
)
bar.add_yaxis(
    '大学（含大专）',
    df['大学'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
            'shadowBlur': 5,  # 阴影大小
            'shadowOffsetY': 2,  # Y轴方向阴影偏移
            'shadowOffsetX': 2,  # x轴方向阴影偏移
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '高中（含中专）',
    df['高中'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
            'shadowBlur': 5,  # 阴影大小
            'shadowOffsetY': 2,  # Y轴方向阴影偏移
            'shadowOffsetX': 2,  # x轴方向阴影偏移
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '初中',
    df['初中'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
            'shadowBlur': 5,  # 阴影大小
            'shadowOffsetY': 2,  # Y轴方向阴影偏移
            'shadowOffsetX': 2,  # x轴方向阴影偏移
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '小学',
    df['小学'].tolist(),
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
            'shadowBlur': 5,  # 阴影大小
            'shadowOffsetY': 2,  # Y轴方向阴影偏移
            'shadowOffsetX': 2,  # x轴方向阴影偏移
            'borderColor': '#fff'
        }
    }
)

bar.add_yaxis(
    '其他',
    [round(x, 2) for x in df['其他'].tolist()],
    stack=1,
    label_opts=opts.LabelOpts(is_show=True, formatter='{c}%', position='insideLeft'),
    itemstyle_opts={
        'normal': {
            'shadowColor': 'rgba(0, 0, 0, .5)',  # 阴影颜色
            'shadowBlur': 5,  # 阴影大小
            'shadowOffsetY': 2,  # Y轴方向阴影偏移
            'shadowOffsetX': 2,  # x轴方向阴影偏移
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
        title="全国各省人口接受教育程度",
        # subtitle='数据来自全国第七次人口普查数据，未包含港澳台地区。',
        pos_left="5%",
        pos_top='1%',
        title_textstyle_opts=opts.TextStyleOpts(color='#00BFFF', font_size=20)
        ),
)

bar.reversal_axis()
bar.set_colors(['blue', '#1E90FF', '#87CEFA', '#FF69B4', 'red'])

bar.render_notebook()


# In[ ]:




