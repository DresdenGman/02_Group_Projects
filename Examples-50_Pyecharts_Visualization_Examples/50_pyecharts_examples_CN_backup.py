#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#前言" data-toc-modified-id="前言-1">前言</a></span></li><li><span><a href="#1.-柱状图堆叠" data-toc-modified-id="1.-柱状图堆叠-2">1. 柱状图堆叠</a></span></li><li><span><a href="#2.关闭坐标轴显示" data-toc-modified-id="2.关闭坐标轴显示-3">2.关闭坐标轴显示</a></span></li><li><span><a href="#3.自定义坐标轴标签文本" data-toc-modified-id="3.自定义坐标轴标签文本-4">3.自定义坐标轴标签文本</a></span></li><li><span><a href="#4.更改坐标轴数据类型" data-toc-modified-id="4.更改坐标轴数据类型-5">4.更改坐标轴数据类型</a></span></li><li><span><a href="#5.双Y轴【直方图&amp;折线图】" data-toc-modified-id="5.双Y轴【直方图&amp;折线图】-6">5.双Y轴【直方图&amp;折线图】</a></span></li><li><span><a href="#6.直方图——双Y轴" data-toc-modified-id="6.直方图——双Y轴-7">6.直方图——双Y轴</a></span></li><li><span><a href="#7.折线图——双X轴" data-toc-modified-id="7.折线图——双X轴-8">7.折线图——双X轴</a></span></li><li><span><a href="#8.自定义图例图形" data-toc-modified-id="8.自定义图例图形-9">8.自定义图例图形</a></span></li><li><span><a href="#9.图例选择设置单选" data-toc-modified-id="9.图例选择设置单选-10">9.图例选择设置单选</a></span></li><li><span><a href="#10.设置默认选中系列" data-toc-modified-id="10.设置默认选中系列-11">10.设置默认选中系列</a></span></li><li><span><a href="#11.缩略轴——inside组件" data-toc-modified-id="11.缩略轴——inside组件-12">11.缩略轴——inside组件</a></span></li><li><span><a href="#12.缩略轴——slider组件" data-toc-modified-id="12.缩略轴——slider组件-13">12.缩略轴——slider组件</a></span></li><li><span><a href="#13.缩略轴——slider组件&amp;inside组件" data-toc-modified-id="13.缩略轴——slider组件&amp;inside组件-14">13.缩略轴——slider组件&amp;inside组件</a></span></li><li><span><a href="#14.XY轴翻转" data-toc-modified-id="14.XY轴翻转-15">14.XY轴翻转</a></span></li><li><span><a href="#15.设置动画效果" data-toc-modified-id="15.设置动画效果-16">15.设置动画效果</a></span></li><li><span><a href="#15.直方图带视觉组件" data-toc-modified-id="15.直方图带视觉组件-17">15.直方图带视觉组件</a></span></li><li><span><a href="#16.设置渐变色(线性渐变)" data-toc-modified-id="16.设置渐变色(线性渐变)-18">16.设置渐变色(线性渐变)</a></span></li><li><span><a href="#17.设置渐变色(径向渐变)" data-toc-modified-id="17.设置渐变色(径向渐变)-19">17.设置渐变色(径向渐变)</a></span></li><li><span><a href="#18.设置分割线" data-toc-modified-id="18.设置分割线-20">18.设置分割线</a></span></li><li><span><a href="#19.设置分割区域" data-toc-modified-id="19.设置分割区域-21">19.设置分割区域</a></span></li><li><span><a href="#20.通过字典配置" data-toc-modified-id="20.通过字典配置-22">20.通过字典配置</a></span></li><li><span><a href="#21.面积图" data-toc-modified-id="21.面积图-23">21.面积图</a></span></li><li><span><a href="#22.堆叠面积图" data-toc-modified-id="22.堆叠面积图-24">22.堆叠面积图</a></span></li><li><span><a href="#23.自定义线样式（LineStyleOpts）" data-toc-modified-id="23.自定义线样式（LineStyleOpts）-25">23.自定义线样式（LineStyleOpts）</a></span></li><li><span><a href="#24.-带阴影效果折线图" data-toc-modified-id="24.-带阴影效果折线图-26">24. 带阴影效果折线图</a></span></li><li><span><a href="#25.折线图平滑处理" data-toc-modified-id="25.折线图平滑处理-27">25.折线图平滑处理</a></span></li><li><span><a href="#26.-直方图带标记线(最大值，平均值等)" data-toc-modified-id="26.-直方图带标记线(最大值，平均值等)-28">26. 直方图带标记线(最大值，平均值等)</a></span></li><li><span><a href="#27.折线图带自定义标记点" data-toc-modified-id="27.折线图带自定义标记点-29">27.折线图带自定义标记点</a></span></li><li><span><a href="#28.折线图带标记区域" data-toc-modified-id="28.折线图带标记区域-30">28.折线图带标记区域</a></span></li><li><span><a href="#29.折线图带百分号显示" data-toc-modified-id="29.折线图带百分号显示-31">29.折线图带百分号显示</a></span></li><li><span><a href="#30.象形图自定义图形" data-toc-modified-id="30.象形图自定义图形-32">30.象形图自定义图形</a></span></li><li><span><a href="#31.水球图自定义图形" data-toc-modified-id="31.水球图自定义图形-33">31.水球图自定义图形</a></span></li><li><span><a href="#32.日历图自定义cell" data-toc-modified-id="32.日历图自定义cell-34">32.日历图自定义cell</a></span></li><li><span><a href="#33.日历图显示中文标签" data-toc-modified-id="33.日历图显示中文标签-35">33.日历图显示中文标签</a></span></li><li><span><a href="#34.GEO添加自定义坐标" data-toc-modified-id="34.GEO添加自定义坐标-36">34.GEO添加自定义坐标</a></span></li><li><span><a href="#35.GEO使用国外地图" data-toc-modified-id="35.GEO使用国外地图-37">35.GEO使用国外地图</a></span></li><li><span><a href="#36.GEO-带涟漪效果散点图" data-toc-modified-id="36.GEO-带涟漪效果散点图-38">36.GEO 带涟漪效果散点图</a></span></li><li><span><a href="#37.GEO热力图" data-toc-modified-id="37.GEO热力图-39">37.GEO热力图</a></span></li><li><span><a href="#38.GEO-线图" data-toc-modified-id="38.GEO-线图-40">38.GEO 线图</a></span></li><li><span><a href="#39.饼图自定义图形半径范围" data-toc-modified-id="39.饼图自定义图形半径范围-41">39.饼图自定义图形半径范围</a></span></li><li><span><a href="#40.饼图自定义数据标签" data-toc-modified-id="40.饼图自定义数据标签-42">40.饼图自定义数据标签</a></span></li><li><span><a href="#41.多饼图" data-toc-modified-id="41.多饼图-43">41.多饼图</a></span></li><li><span><a href="#42.散点图添加视觉组件（图形大小）" data-toc-modified-id="42.散点图添加视觉组件（图形大小）-44">42.散点图添加视觉组件（图形大小）</a></span></li><li><span><a href="#43.散点图添加视觉组件（图形大小&amp;颜色）" data-toc-modified-id="43.散点图添加视觉组件（图形大小&amp;颜色）-45">43.散点图添加视觉组件（图形大小&amp;颜色）</a></span></li><li><span><a href="#44.散点图添加视觉组件（图形大小&amp;颜色&amp;透明度）" data-toc-modified-id="44.散点图添加视觉组件（图形大小&amp;颜色&amp;透明度）-46">44.散点图添加视觉组件（图形大小&amp;颜色&amp;透明度）</a></span></li><li><span><a href="#45.自定义背景颜色" data-toc-modified-id="45.自定义背景颜色-47">45.自定义背景颜色</a></span></li><li><span><a href="#46.词云图自定义字体范围" data-toc-modified-id="46.词云图自定义字体范围-48">46.词云图自定义字体范围</a></span></li><li><span><a href="#47.Map带视觉组件" data-toc-modified-id="47.Map带视觉组件-49">47.Map带视觉组件</a></span></li><li><span><a href="#48.Page更改布局" data-toc-modified-id="48.Page更改布局-50">48.Page更改布局</a></span></li><li><span><a href="#49.一个Tab下带多个图表" data-toc-modified-id="49.一个Tab下带多个图表-51">49.一个Tab下带多个图表</a></span></li><li><span><a href="#50.Timeline-自动播放" data-toc-modified-id="50.Timeline-自动播放-52">50.Timeline 自动播放</a></span></li></ul></div>

# #### 前言
# 
# * 总共50个完整pyecharts例子，包含一些常用的配置方法，每个cell都包含完整代码，可独立运行；
# 
# * 为避免混淆，每个例子尽量只包含单一配置的代码；
# 
# * 所有代码均基于`pyecharts V1.7.1`，不同版本间可能存在不兼容，如遇代码报错请优先确认是否版本问题；
# 

# #### 1. 柱状图堆叠
# 
# * 不同系列的数据使用相同的stack值会堆叠在一起；


# In[1]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_stack():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    # stack值一样的系列会堆叠在一起
    bar.add_yaxis('A', Faker.values(), stack='stack1')
    bar.add_yaxis('B', Faker.values(), stack='stack1')
    bar.add_yaxis('C', Faker.values(), stack='stack2')
    return bar



chart = bar_stack()
chart.render_notebook()


# #### 2.关闭坐标轴显示
# 
# * 碰上类目标签过长的时候，可以选择关闭坐标轴，将数据&标签直接显示在图形中；

# In[2]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_axis_off():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('', Faker.values())
    # 碰上类目标签过长的时候，可以选择关闭坐标轴，直接显示在图形中
    bar.set_series_opts(label_opts=opts.LabelOpts(position='insideLeft', formatter='{b}:{c}'))
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=False),
                        yaxis_opts=opts.AxisOpts(is_show=False))
    bar.reversal_axis()
    return bar


chart = bar_with_axis_off()
chart.render_notebook()


# #### 3.自定义坐标轴标签文本
# 

# In[3]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = list(range(2010, 2020))
y_data = [random.randint(20, 200) for _ in range(len(x_data))]


def bar_with_custom_axis_label():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    bar.add_yaxis('', y_data)

    bar.set_global_opts(xaxis_opts=opts.AxisOpts(
        # 自定义坐标轴标签，在年份后加上`年`
        axislabel_opts=opts.LabelOpts(formatter='{value}年')))
    return bar


chart = bar_with_custom_axis_label()
chart.render_notebook()


# #### 4.更改坐标轴数据类型
# 
# * x轴默认数据类型是使用离散型，在使用散点图的时候可调整为数值型；

# In[4]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = [random.randint(0, 20) for _ in range(100)]
y_data = [random.randint(0, 50) for _ in range(100)]


def scatter_with_value_xaxis():
    scatter = Scatter(init_opts=opts.InitOpts(theme='light',
                                              width='1000px',
                                              height='600px'))
    scatter.add_xaxis(x_data)
    scatter.add_yaxis('', y_data)
    # X轴默认数据类型为离散数据，设置为数值型
    scatter.set_global_opts(xaxis_opts=opts.AxisOpts(type_="value"))
    return scatter

chart = scatter_with_value_xaxis()
chart.render_notebook()


# #### 5.双Y轴【直方图&折线图】
# 
# * 实际是Bar和Line两个图表共用同一套坐标体系，将Bar和Line分别指向不同的Y轴；

# In[5]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ['香蕉', '梨子', '水蜜桃', '核桃', '西瓜', '苹果']
y_data_1 = [random.randint(10, 50) for _ in range(len(x_data))]
y_data_2 = [random.randint(100, 500) for _ in range(len(x_data))]


def bar_line_combine_with_two_axis():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    # 添加一个Y轴
    bar.extend_axis(yaxis=opts.AxisOpts())
    bar.add_yaxis('左边Y轴', y_data_1, yaxis_index=0)

    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    # 将line数据通过yaxis_index指向后添加的Y轴
    line.add_yaxis('右边Y轴', y_data_2, yaxis_index=1)

    bar.overlap(line)
    return bar


chart = bar_line_combine_with_two_axis()
chart.render_notebook()


# #### 6.直方图——双Y轴

# In[6]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ['香蕉', '梨子', '水蜜桃', '核桃', '西瓜', '苹果']
y_data_1 = [random.randint(10, 50) for _ in range(len(x_data))]
y_data_2 = [random.randint(100, 500) for _ in range(len(x_data))]


def bar_with_multiple_axis():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    # 添加一个Y轴
    bar.extend_axis(yaxis=opts.AxisOpts())
    # 分别指定使用的Y轴
    bar.add_yaxis('左边Y轴', y_data_1, yaxis_index=0)
    bar.add_yaxis('右边Y轴', y_data_2, yaxis_index=1)
    return bar


chart = bar_with_multiple_axis()
chart.render_notebook()


# #### 7.折线图——双X轴

# In[7]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data_1 = ["2020/10/{}".format(i + 1) for i in range(30)]
x_data_2 = ["2019/10/{}".format(i + 1) for i in range(30)]
y_data_1 = [random.randint(10, 50) for _ in range(30)]
y_data_2 = [random.randint(20, 60) for _ in range(30)]


def line_with_two_xaxis():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data_1)
    # 添加一个x轴
    line.extend_axis(xaxis_data=x_data_2, xaxis=opts.AxisOpts())
    line.add_yaxis('下面X轴', y_data_1)
    line.add_yaxis('上面X轴', y_data_2)
    return line


chart = line_with_two_xaxis()
chart.render_notebook()


# #### 8.自定义图例图形
# 
# * 当前并不支持同一个图表针对不同的系列设置不同的icon
# * 方案是将多个系列的数据拆分到多个图表设置各自的icon，最后通过grid将图表组合起来

# In[8]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

ios_icon = 'path://M24.734 17.003c-0.040-4.053 3.305-5.996 3.454-6.093-1.88-2.751-4.808-3.127-5.851-3.171-2.492-0.252-4.862 1.467-6.127 1.467-1.261 0-3.213-1.43-5.28-1.392-2.716 0.040-5.221 1.579-6.619 4.012-2.822 4.897-0.723 12.151 2.028 16.123 1.344 1.944 2.947 4.127 5.051 4.049 2.026-0.081 2.793-1.311 5.242-1.311s3.138 1.311 5.283 1.271c2.18-0.041 3.562-1.981 4.897-3.931 1.543-2.255 2.179-4.439 2.216-4.551-0.048-0.022-4.252-1.632-4.294-6.473zM20.705 5.11c1.117-1.355 1.871-3.235 1.665-5.11-1.609 0.066-3.559 1.072-4.713 2.423-1.036 1.199-1.942 3.113-1.699 4.951 1.796 0.14 3.629-0.913 4.747-2.264z'
android_icon = 'path://M28 12c-1.1 0-2 0.9-2 2v8c0 1.1 0.9 2 2 2s2-0.9 2-2v-8c0-1.1-0.9-2-2-2zM4 12c-1.1 0-2 0.9-2 2v8c0 1.1 0.9 2 2 2s2-0.9 2-2v-8c0-1.1-0.9-2-2-2zM7 23c0 1.657 1.343 3 3 3v0 4c0 1.1 0.9 2 2 2s2-0.9 2-2v-4h4v4c0 1.1 0.9 2 2 2s2-0.9 2-2v-4c1.657 0 3-1.343 3-3v-11h-18v11zM24.944 10c-0.304-2.746-1.844-5.119-4.051-6.551l1.001-2.001c0.247-0.494 0.047-1.095-0.447-1.342s-1.095-0.047-1.342 0.447l-1.004 2.009-0.261-0.104c-0.893-0.297-1.848-0.458-2.84-0.458s-1.947 0.161-2.84 0.458l-0.261 0.104-1.004-2.009c-0.247-0.494-0.848-0.694-1.342-0.447s-0.694 0.848-0.447 1.342l1.001 2.001c-2.207 1.433-3.747 3.805-4.051 6.551v1h17.944v-1h-0.056zM13 8c-0.552 0-1-0.448-1-1s0.447-0.999 0.998-1c0.001 0 0.002 0 0.003 0s0.001-0 0.002-0c0.551 0.001 0.998 0.448 0.998 1s-0.448 1-1 1zM19 8c-0.552 0-1-0.448-1-1s0.446-0.999 0.998-1c0 0 0.001 0 0.002 0s0.002-0 0.003-0c0.551 0.001 0.998 0.448 0.998 1s-0.448 1-1 1z'

x_data = ["2020/7/{}".format(i + 1) for i in range(10)]

# 随机生成点数据
y_data_1 = [random.randint(10, 20) for i in range(len(x_data))]
y_data_2 = [random.randint(15, 25) for i in range(len(x_data))]


def bar_custom_legend_symbol():
    # 当前并不支持同一个图表针对不同的系列设置不同的icon
    # 方案是将多个系列的数据拆分到多个图表设置各自的icon，最后通过grid将图表组合起来
    ios_bar = Bar()
    ios_bar.add_xaxis(x_data)
    ios_bar.add_yaxis('IOS', y_data_1)
    ios_bar.set_global_opts(legend_opts=opts.LegendOpts(legend_icon=ios_icon,
                                                        pos_right='15%'))

    az_bar = Bar()
    az_bar.add_xaxis(x_data)
    az_bar.add_yaxis('Android', y_data_2)
    az_bar.set_global_opts(legend_opts=opts.LegendOpts(legend_icon=android_icon,
                                                       pos_right='5%'))

    # 将az_bar和ios_bar组合起来
    grid = Grid(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    grid.add(ios_bar, is_control_axis_index=True, grid_opts=opts.GridOpts())
    grid.add(az_bar, is_control_axis_index=True, grid_opts=opts.GridOpts())
    return grid


chart = bar_custom_legend_symbol()
chart.render_notebook()


# #### 9.图例选择设置单选

# In[9]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker

def bar_single_selected():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    # 设置图例选择模式为单选
    bar.set_global_opts(legend_opts=opts.LegendOpts(selected_mode='single'))
    return bar


chart = bar_single_selected()
chart.render_notebook()


# #### 10.设置默认选中系列

# In[10]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_default_selected_series():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    # 默认选中A C
    bar.add_yaxis('A', Faker.values(), is_selected=True)
    bar.add_yaxis('B', Faker.values(), is_selected=False)
    bar.add_yaxis('C', Faker.values(), is_selected=True)
    return bar


chart = bar_with_default_selected_series()
chart.render_notebook()


# #### 11.缩略轴——inside组件

# In[11]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data = [random.randint(10, 20) for i in range(len(x_data))]


def bar_datazoom_inside():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    bar.add_yaxis('', y_data)
    bar.set_global_opts(datazoom_opts=opts.DataZoomOpts(type_='inside',
                                                        range_start=50,   # 设置起止位置，50%-100%
                                                        range_end=100))
    return bar


chart = bar_datazoom_inside()
chart.render_notebook()


# #### 12.缩略轴——slider组件

# In[12]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data = [random.randint(10, 20) for i in range(len(x_data))]


def bar_with_datazoom_slider():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    bar.add_yaxis('', y_data)
    bar.set_global_opts(datazoom_opts=opts.DataZoomOpts(range_start=50,   # 设置起止位置，50%-100%
                                                        range_end=100))
    return bar


chart = bar_with_datazoom_slider()
chart.render_notebook()


# #### 13.缩略轴——slider组件&inside组件

# In[13]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data = [random.randint(10, 20) for i in range(len(x_data))]


def bar_datazoom_both_way():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    bar.add_yaxis('', y_data)
    # 通过list传入两个datazoom_opts
    bar.set_global_opts(datazoom_opts=[opts.DataZoomOpts(),
                                       opts.DataZoomOpts(type_='inside', range_start=50, range_end=100)])
    return bar


chart = bar_datazoom_both_way()
chart.render_notebook()


# #### 14.XY轴翻转

# In[14]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_reverse_axis():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    # x,y轴翻转
    bar.reversal_axis()
    return bar


chart = bar_reverse_axis()
chart.render_notebook()


# #### 15.设置动画效果
# 
# * 在图表加载前会有一段动画效果；
# * 更多动画效果可参见：https://echarts.apache.org/examples/zh/editor.html?c=line-easing

# In[15]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker

"""
更多动画效果可参见：https://echarts.apache.org/examples/zh/editor.html?c=line-easing
"""


def bar_with_animation():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px',
                                      animation_opts=opts.AnimationOpts(animation_delay=1000,   # 动画延时
                                                                        animation_easing='bounceIn')
                                      )
              )
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    return bar


chart = bar_with_animation()
chart.render_notebook()


# #### 15.直方图带视觉组件

# In[16]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_visualmap_color():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    # 设置视觉组件，默认通过颜色映射数据，数值范围为0-100，可通过min_和max_进行自定义
    bar.set_global_opts(visualmap_opts=opts.VisualMapOpts())
    return bar


chart = bar_with_visualmap_color()
chart.render_notebook()


# #### 16.设置渐变色(线性渐变)

# In[17]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode

color_js = """
            new echarts.graphic.LinearGradient(
                                0, 
                                1, 
                                0, 
                                0,
                                [{offset: 0, color: '#008B8B'}, 
                                 {offset: 1, color: '#FF6347'}], 
                                false)
           """


def bar_with_linear_gradient_color():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('', Faker.values(),
                  # 使用JsCode执行渐变色代码
                  itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_js)))

    return bar


chart = bar_with_linear_gradient_color()
chart.render_notebook()


# #### 17.设置渐变色(径向渐变)

# In[18]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode

color_js = """new echarts.graphic.RadialGradient(
                    0.4, 0.3, 1,
                    [{offset: 0,
                      color: '#F8F8FF'},
                     {offset: 1,
                      color: '#00BFFF'}
                      ])"""


def scatter_with_radial_gradient_color():
    scatter = Scatter(init_opts=opts.InitOpts(theme='light',
                                              width='1000px',
                                              height='600px'))
    scatter.add_xaxis(Faker.choose())

    scatter.add_yaxis("", Faker.values(),
                      symbol_size=50,
                      # 渐变配色
                      itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_js)))
    return scatter


chart = scatter_with_radial_gradient_color()
chart.render_notebook()


# #### 18.设置分割线

# In[19]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_custom_splitline():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    # 设置分割线
    bar.set_global_opts(yaxis_opts=opts.AxisOpts(
        splitline_opts=opts.SplitLineOpts(is_show=True,
                                          linestyle_opts=opts.LineStyleOpts(type_='dotted'))))
    return bar


chart = bar_with_custom_splitline()
chart.render_notebook()


# #### 19.设置分割区域

# In[20]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_custom_splitarea():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    # 设置分割区域
    bar.set_global_opts(yaxis_opts=opts.AxisOpts(
        splitarea_opts=opts.SplitAreaOpts(is_show=True,
                                          areastyle_opts=opts.AreaStyleOpts(opacity=1))))
    return bar


chart = bar_with_custom_splitarea()
chart.render_notebook()


# #### 20.通过字典配置

# In[21]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_dict_config():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('', Faker.values())
    # 通过字典配置itemstyle
    bar.set_series_opts(itemstyle_opts=dict(color='#008B8B', opacity=0.8))
    return bar


chart = bar_with_dict_config()
chart.render_notebook()


# #### 21.面积图
# * 实现方式就是在**折线图先填充区域**；

# In[22]:



from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data = [i + random.randint(10, 20) for i in range(len(x_data))]


def line_with_area():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    line.add_yaxis('', y_data)
    # opacity 默认为0，即透明
    line.set_series_opts(areastyle_opts=opts.AreaStyleOpts(opacity=0.5))

    return line


chart = line_with_area()
chart.render_notebook()


# #### 22.堆叠面积图

# In[23]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def line_stack_area():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(Faker.choose())
    line.add_yaxis('A',
                   Faker.values(),
                   stack='stack')
    line.add_yaxis('B',
                   Faker.values(),
                   stack='stack')
    line.add_yaxis('C',
                   Faker.values(),
                   stack='stack')
    # opacity 默认为0，即透明
    line.set_series_opts(areastyle_opts=opts.AreaStyleOpts(opacity=0.5))

    return line


chart = line_stack_area()
chart.render_notebook()


# #### 23.自定义线样式（LineStyleOpts）

# In[24]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def line_with_custom_linestyle():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(Faker.choose())
    line.add_yaxis('样式1',
                   Faker.values(),
                   linestyle_opts=opts.LineStyleOpts(width=5,
                                                     curve=0,
                                                     opacity=0.7,
                                                     type_='solid',
                                                     color='red')
                   )
    line.add_yaxis('样式2',
                   Faker.values(),
                   linestyle_opts=opts.LineStyleOpts(width=3,
                                                     curve=0.5,
                                                     opacity=0.9,
                                                     type_='dashed',
                                                     color='yellow')
                   )
    line.add_yaxis('样式3',
                   Faker.values(),
                   linestyle_opts=opts.LineStyleOpts(width=1,
                                                     curve=1,
                                                     opacity=0.5,
                                                     type_='dotted',
                                                     color='green')
                   )
    return line


chart = line_with_custom_linestyle()
chart.render_notebook()


# #### 24. 带阴影效果折线图
# 
# * `linestyle_opts`在默认参数中并不支持直接配置阴影效果，可选择通过dict传入`shadowOffsetX`等参数来实现；

# In[25]:



from pyecharts.charts import *
from pyecharts import options as opts
import random

line_style = {
    'normal': {
        'width': 4,  # 设置线宽
        'shadowColor': 'rgba(155, 18, 184, .3)',  # 阴影颜色
        'shadowBlur': 10,  # 阴影大小
        'shadowOffsetY': 10,  # Y轴方向阴影偏移
        'shadowOffsetX': 10,  # x轴方向阴影偏移
        'curve': 0.5  # 线弯曲程度，1表示不弯曲
    }
}

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data_1 = [i + random.randint(10, 20) for i in range(len(x_data))]
y_data_2 = [i + random.randint(15, 25) for i in range(len(x_data))]


def line_with_shadow():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    line.add_yaxis("Android",
                   y_data_1,
                   is_symbol_show=False,
                   is_smooth=True,
                   # 传入线风格参数
                   linestyle_opts=line_style)
    line.add_yaxis("IOS",
                   y_data_2,
                   is_symbol_show=False,
                   is_smooth=True,
                   # 传入线风格参数
                   linestyle_opts=line_style)
    line.set_global_opts(title_opts=opts.TitleOpts(title="终端日活趋势"))
    return line


chart = line_with_shadow()
chart.render_notebook()


# #### 25.折线图平滑处理

# In[26]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def line_with_smooth_connect():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(Faker.choose())
    # 设置is_smooth=True来平滑曲线
    line.add_yaxis('平滑曲线', Faker.values(), is_smooth=True)
    line.add_yaxis('直线', Faker.values(), is_smooth=False)

    return line


chart = line_with_smooth_connect()
chart.render_notebook()


# #### 26. 直方图带标记线(最大值，平均值等)

# In[27]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_guide_line():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    # 设置标记线
    bar.set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="min", name="最小值"),
                opts.MarkLineItem(type_="max", name="最大值"),
                opts.MarkLineItem(type_="average", name="平均值"),
            ]
        )
    )

    return bar


chart = bar_with_guide_line()
chart.render_notebook()


# #### 27.折线图带自定义标记点

# In[28]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data = [i + random.randint(10, 20) for i in range(len(x_data))]


def line_with_custom_mark_point():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    line.add_yaxis('', y_data)
    # 自定义标记点
    line.set_series_opts(
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(name="自定义标记点", coord=[x_data[2], y_data[2]], value=y_data[2])]
        )
    )

    return line


chart = line_with_custom_mark_point()
chart.render_notebook()


# #### 28.折线图带标记区域

# In[29]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data = [i + random.randint(10, 20) for i in range(len(x_data))]


def line_with_mark_area():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    line.add_yaxis('', y_data)
    # 设置标记区域
    line.set_series_opts(
        markarea_opts=opts.MarkAreaOpts(
            data=[
                opts.MarkAreaItem(name="黄金周", x=("2020/10/1", "2020/10/8"))
            ]
        )
    )

    return line


chart = line_with_mark_area()
chart.render_notebook()


# #### 29.折线图带百分号显示

# In[30]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode


x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [0.98, 0.89, 0.92, 1.07, 0.81, 1.23]

js = """function (param) {return param.name +':'+ Math.floor(param.value[1])+'%';}"""


def line_with_per_show():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    # 传入数据时先乘以100
    line.add_yaxis('', [round(v * 100, 0) for v in y_data])
    # 执行js代码让%显示
    line.set_series_opts(label_opts=opts.LabelOpts(is_show=True,
                                                   formatter=JsCode(js)))

    return line


chart = line_with_per_show()
chart.render_notebook()


# #### 30.象形图自定义图形

# In[31]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def pictorialbar_with_custom_symbol():
    pictorialbar = PictorialBar(init_opts=opts.InitOpts(theme='light',
                                                        width='1000px',
                                                        height='600px'))
    pictorialbar.add_xaxis(Faker.choose())
    pictorialbar.add_yaxis('A',
                           Faker.values(),
                           symbol_size=20,
                           # 自定义图形
                           symbol='path://M100,0 L41.22,180.90 L195.10,69.09 L4.89,69.09 L158.77,180.90 z',
                           symbol_repeat="fixed",
                           is_symbol_clip=True
                           )

    return pictorialbar


chart = pictorialbar_with_custom_symbol()
chart.render_notebook()


# #### 31.水球图自定义图形

# In[32]:


from pyecharts.charts import *
from pyecharts import options as opts

ios_icon = 'path://M24.734 17.003c-0.040-4.053 3.305-5.996 3.454-6.093-1.88-2.751-4.808-3.127-5.851-3.171-2.492-0.252-4.862 1.467-6.127 1.467-1.261 0-3.213-1.43-5.28-1.392-2.716 0.040-5.221 1.579-6.619 4.012-2.822 4.897-0.723 12.151 2.028 16.123 1.344 1.944 2.947 4.127 5.051 4.049 2.026-0.081 2.793-1.311 5.242-1.311s3.138 1.311 5.283 1.271c2.18-0.041 3.562-1.981 4.897-3.931 1.543-2.255 2.179-4.439 2.216-4.551-0.048-0.022-4.252-1.632-4.294-6.473zM20.705 5.11c1.117-1.355 1.871-3.235 1.665-5.11-1.609 0.066-3.559 1.072-4.713 2.423-1.036 1.199-1.942 3.113-1.699 4.951 1.796 0.14 3.629-0.913 4.747-2.264z'


def liquid_with_custom_shape():
    liquid = Liquid(init_opts=opts.InitOpts(theme='light',
                                            width='1000px',
                                            height='600px'))
    liquid.add('', [0.4, 0.5], shape=ios_icon)

    return liquid


chart = liquid_with_custom_shape()
chart.render_notebook()


# #### 32.日历图自定义cell

# In[33]:


from pyecharts.charts import *
from pyecharts import options as opts
import datetime

# 美国covid确诊数据
data = [(datetime.datetime(2020, 1, 21, 0, 0), 1), (datetime.datetime(2020, 1, 22, 0, 0), 1),
        (datetime.datetime(2020, 1, 23, 0, 0), 1), (datetime.datetime(2020, 1, 24, 0, 0), 2),
        (datetime.datetime(2020, 1, 25, 0, 0), 2), (datetime.datetime(2020, 1, 26, 0, 0), 5),
        (datetime.datetime(2020, 1, 27, 0, 0), 5), (datetime.datetime(2020, 1, 28, 0, 0), 5),
        (datetime.datetime(2020, 1, 29, 0, 0), 5), (datetime.datetime(2020, 1, 30, 0, 0), 5),
        (datetime.datetime(2020, 1, 31, 0, 0), 7), (datetime.datetime(2020, 2, 1, 0, 0), 8),
        (datetime.datetime(2020, 2, 2, 0, 0), 8), (datetime.datetime(2020, 2, 3, 0, 0), 11),
        (datetime.datetime(2020, 2, 4, 0, 0), 11), (datetime.datetime(2020, 2, 5, 0, 0), 11),
        (datetime.datetime(2020, 2, 6, 0, 0), 11), (datetime.datetime(2020, 2, 7, 0, 0), 11),
        (datetime.datetime(2020, 2, 8, 0, 0), 11), (datetime.datetime(2020, 2, 9, 0, 0), 11),
        (datetime.datetime(2020, 2, 10, 0, 0), 11), (datetime.datetime(2020, 2, 11, 0, 0), 12),
        (datetime.datetime(2020, 2, 12, 0, 0), 12), (datetime.datetime(2020, 2, 13, 0, 0), 13),
        (datetime.datetime(2020, 2, 14, 0, 0), 13), (datetime.datetime(2020, 2, 15, 0, 0), 13),
        (datetime.datetime(2020, 2, 16, 0, 0), 13), (datetime.datetime(2020, 2, 17, 0, 0), 13),
        (datetime.datetime(2020, 2, 18, 0, 0), 13), (datetime.datetime(2020, 2, 19, 0, 0), 13),
        (datetime.datetime(2020, 2, 20, 0, 0), 13), (datetime.datetime(2020, 2, 21, 0, 0), 15),
        (datetime.datetime(2020, 2, 22, 0, 0), 15), (datetime.datetime(2020, 2, 23, 0, 0), 15),
        (datetime.datetime(2020, 2, 24, 0, 0), 15), (datetime.datetime(2020, 2, 25, 0, 0), 15),
        (datetime.datetime(2020, 2, 26, 0, 0), 15), (datetime.datetime(2020, 2, 27, 0, 0), 16),
        (datetime.datetime(2020, 2, 28, 0, 0), 16), (datetime.datetime(2020, 2, 29, 0, 0), 24),
        (datetime.datetime(2020, 3, 1, 0, 0), 30), (datetime.datetime(2020, 3, 2, 0, 0), 53),
        (datetime.datetime(2020, 3, 3, 0, 0), 73), (datetime.datetime(2020, 3, 4, 0, 0), 104),
        (datetime.datetime(2020, 3, 5, 0, 0), 174), (datetime.datetime(2020, 3, 6, 0, 0), 222),
        (datetime.datetime(2020, 3, 7, 0, 0), 337), (datetime.datetime(2020, 3, 8, 0, 0), 451),
        (datetime.datetime(2020, 3, 9, 0, 0), 519), (datetime.datetime(2020, 3, 10, 0, 0), 711),
        (datetime.datetime(2020, 3, 11, 0, 0), 1109), (datetime.datetime(2020, 3, 12, 0, 0), 1561),
        (datetime.datetime(2020, 3, 13, 0, 0), 2157), (datetime.datetime(2020, 3, 14, 0, 0), 2870),
        (datetime.datetime(2020, 3, 15, 0, 0), 2968), (datetime.datetime(2020, 3, 16, 0, 0), 4360),
        (datetime.datetime(2020, 3, 17, 0, 0), 6141), (datetime.datetime(2020, 3, 18, 0, 0), 8914),
        (datetime.datetime(2020, 3, 19, 0, 0), 14153), (datetime.datetime(2020, 3, 20, 0, 0), 19479),
        (datetime.datetime(2020, 3, 21, 0, 0), 25818), (datetime.datetime(2020, 3, 22, 0, 0), 33756),
        (datetime.datetime(2020, 3, 23, 0, 0), 43845), (datetime.datetime(2020, 3, 24, 0, 0), 54108),
        (datetime.datetime(2020, 3, 25, 0, 0), 66044), (datetime.datetime(2020, 3, 26, 0, 0), 84080),
        (datetime.datetime(2020, 3, 27, 0, 0), 102254), (datetime.datetime(2020, 3, 28, 0, 0), 122054),
        (datetime.datetime(2020, 3, 29, 0, 0), 141194), (datetime.datetime(2020, 3, 30, 0, 0), 162690),
        (datetime.datetime(2020, 3, 31, 0, 0), 188701), (datetime.datetime(2020, 4, 1, 0, 0), 214194),
        (datetime.datetime(2020, 4, 2, 0, 0), 244593), (datetime.datetime(2020, 4, 3, 0, 0), 276535),
        (datetime.datetime(2020, 4, 4, 0, 0), 309699), (datetime.datetime(2020, 4, 5, 0, 0), 337573),
        (datetime.datetime(2020, 4, 6, 0, 0), 367210), (datetime.datetime(2020, 4, 7, 0, 0), 397992),
        (datetime.datetime(2020, 4, 8, 0, 0), 429686), (datetime.datetime(2020, 4, 9, 0, 0), 464442),
        (datetime.datetime(2020, 4, 10, 0, 0), 497943), (datetime.datetime(2020, 4, 11, 0, 0), 527958),
        (datetime.datetime(2020, 4, 12, 0, 0), 556517), (datetime.datetime(2020, 4, 13, 0, 0), 581810),
        (datetime.datetime(2020, 4, 14, 0, 0), 608845), (datetime.datetime(2020, 4, 15, 0, 0), 637974),
        (datetime.datetime(2020, 4, 16, 0, 0), 669272), (datetime.datetime(2020, 4, 17, 0, 0), 701996),
        (datetime.datetime(2020, 4, 18, 0, 0), 730317), (datetime.datetime(2020, 4, 19, 0, 0), 756375),
        (datetime.datetime(2020, 4, 20, 0, 0), 783716), (datetime.datetime(2020, 4, 21, 0, 0), 809213),
        (datetime.datetime(2020, 4, 22, 0, 0), 837414), (datetime.datetime(2020, 4, 23, 0, 0), 871617),
        (datetime.datetime(2020, 4, 24, 0, 0), 907908), (datetime.datetime(2020, 4, 25, 0, 0), 940829),
        (datetime.datetime(2020, 4, 26, 0, 0), 968517), (datetime.datetime(2020, 4, 27, 0, 0), 990993),
        (datetime.datetime(2020, 4, 28, 0, 0), 1015518), (datetime.datetime(2020, 4, 29, 0, 0), 1042926),
        (datetime.datetime(2020, 4, 30, 0, 0), 1072667)]


def calendar_custom_cell():
    calendar = Calendar(init_opts=opts.InitOpts(theme='light',
                                                width='1000px',
                                                height='600px'))
    calendar.add('确证人数',
                 yaxis_data=data,
                 label_opts=opts.LabelOpts(is_show=True),
                 calendar_opts=opts.CalendarOpts(
                     # 日历位置
                     pos_top='10%',
                     pos_left='10%',
                     # 日期范围
                     range_=['2020-01-21', '2020-04-30'],
                     # 日历单元格尺寸
                     cell_size=50,
                     # 年月日标签样式设置
                     yearlabel_opts=opts.CalendarYearLabelOpts(margin=40,
                                                               label_font_size=20,
                                                               label_color='rgba(130,134,112,0.8)'),
                     daylabel_opts=opts.CalendarDayLabelOpts(label_color='#778633', label_font_weight='bold'),
                     monthlabel_opts=opts.CalendarMonthLabelOpts(label_color='#778633', label_font_weight='bold')
                 )
                 )
    # 设置视觉组件
    calendar.set_global_opts(visualmap_opts=opts.VisualMapOpts(
        max_=1000000,
        is_piecewise=True,
        pieces=[{"min": 1000000},
                {"min": 10000, "max": 1000000},
                {"min": 100, "max": 10000},
                {"max": 100}],
        range_color=["#CCD3D9", "#E6B6C2", "#D4587A", "#DC364C"]
    ))
    return calendar


chart = calendar_custom_cell()
chart.render_notebook()


# #### 33.日历图显示中文标签

# In[34]:


from pyecharts.charts import *
from pyecharts import options as opts
import datetime

# 美国covid确诊数据
data = [(datetime.datetime(2020, 1, 21, 0, 0), 1), (datetime.datetime(2020, 1, 22, 0, 0), 1),
        (datetime.datetime(2020, 1, 23, 0, 0), 1), (datetime.datetime(2020, 1, 24, 0, 0), 2),
        (datetime.datetime(2020, 1, 25, 0, 0), 2), (datetime.datetime(2020, 1, 26, 0, 0), 5),
        (datetime.datetime(2020, 1, 27, 0, 0), 5), (datetime.datetime(2020, 1, 28, 0, 0), 5),
        (datetime.datetime(2020, 1, 29, 0, 0), 5), (datetime.datetime(2020, 1, 30, 0, 0), 5),
        (datetime.datetime(2020, 1, 31, 0, 0), 7), (datetime.datetime(2020, 2, 1, 0, 0), 8),
        (datetime.datetime(2020, 2, 2, 0, 0), 8), (datetime.datetime(2020, 2, 3, 0, 0), 11),
        (datetime.datetime(2020, 2, 4, 0, 0), 11), (datetime.datetime(2020, 2, 5, 0, 0), 11),
        (datetime.datetime(2020, 2, 6, 0, 0), 11), (datetime.datetime(2020, 2, 7, 0, 0), 11),
        (datetime.datetime(2020, 2, 8, 0, 0), 11), (datetime.datetime(2020, 2, 9, 0, 0), 11),
        (datetime.datetime(2020, 2, 10, 0, 0), 11), (datetime.datetime(2020, 2, 11, 0, 0), 12),
        (datetime.datetime(2020, 2, 12, 0, 0), 12), (datetime.datetime(2020, 2, 13, 0, 0), 13),
        (datetime.datetime(2020, 2, 14, 0, 0), 13), (datetime.datetime(2020, 2, 15, 0, 0), 13),
        (datetime.datetime(2020, 2, 16, 0, 0), 13), (datetime.datetime(2020, 2, 17, 0, 0), 13),
        (datetime.datetime(2020, 2, 18, 0, 0), 13), (datetime.datetime(2020, 2, 19, 0, 0), 13),
        (datetime.datetime(2020, 2, 20, 0, 0), 13), (datetime.datetime(2020, 2, 21, 0, 0), 15),
        (datetime.datetime(2020, 2, 22, 0, 0), 15), (datetime.datetime(2020, 2, 23, 0, 0), 15),
        (datetime.datetime(2020, 2, 24, 0, 0), 15), (datetime.datetime(2020, 2, 25, 0, 0), 15),
        (datetime.datetime(2020, 2, 26, 0, 0), 15), (datetime.datetime(2020, 2, 27, 0, 0), 16),
        (datetime.datetime(2020, 2, 28, 0, 0), 16), (datetime.datetime(2020, 2, 29, 0, 0), 24),
        (datetime.datetime(2020, 3, 1, 0, 0), 30), (datetime.datetime(2020, 3, 2, 0, 0), 53),
        (datetime.datetime(2020, 3, 3, 0, 0), 73), (datetime.datetime(2020, 3, 4, 0, 0), 104),
        (datetime.datetime(2020, 3, 5, 0, 0), 174), (datetime.datetime(2020, 3, 6, 0, 0), 222),
        (datetime.datetime(2020, 3, 7, 0, 0), 337), (datetime.datetime(2020, 3, 8, 0, 0), 451),
        (datetime.datetime(2020, 3, 9, 0, 0), 519), (datetime.datetime(2020, 3, 10, 0, 0), 711),
        (datetime.datetime(2020, 3, 11, 0, 0), 1109), (datetime.datetime(2020, 3, 12, 0, 0), 1561),
        (datetime.datetime(2020, 3, 13, 0, 0), 2157), (datetime.datetime(2020, 3, 14, 0, 0), 2870),
        (datetime.datetime(2020, 3, 15, 0, 0), 2968), (datetime.datetime(2020, 3, 16, 0, 0), 4360),
        (datetime.datetime(2020, 3, 17, 0, 0), 6141), (datetime.datetime(2020, 3, 18, 0, 0), 8914),
        (datetime.datetime(2020, 3, 19, 0, 0), 14153), (datetime.datetime(2020, 3, 20, 0, 0), 19479),
        (datetime.datetime(2020, 3, 21, 0, 0), 25818), (datetime.datetime(2020, 3, 22, 0, 0), 33756),
        (datetime.datetime(2020, 3, 23, 0, 0), 43845), (datetime.datetime(2020, 3, 24, 0, 0), 54108),
        (datetime.datetime(2020, 3, 25, 0, 0), 66044), (datetime.datetime(2020, 3, 26, 0, 0), 84080),
        (datetime.datetime(2020, 3, 27, 0, 0), 102254), (datetime.datetime(2020, 3, 28, 0, 0), 122054),
        (datetime.datetime(2020, 3, 29, 0, 0), 141194), (datetime.datetime(2020, 3, 30, 0, 0), 162690),
        (datetime.datetime(2020, 3, 31, 0, 0), 188701), (datetime.datetime(2020, 4, 1, 0, 0), 214194),
        (datetime.datetime(2020, 4, 2, 0, 0), 244593), (datetime.datetime(2020, 4, 3, 0, 0), 276535),
        (datetime.datetime(2020, 4, 4, 0, 0), 309699), (datetime.datetime(2020, 4, 5, 0, 0), 337573),
        (datetime.datetime(2020, 4, 6, 0, 0), 367210), (datetime.datetime(2020, 4, 7, 0, 0), 397992),
        (datetime.datetime(2020, 4, 8, 0, 0), 429686), (datetime.datetime(2020, 4, 9, 0, 0), 464442),
        (datetime.datetime(2020, 4, 10, 0, 0), 497943), (datetime.datetime(2020, 4, 11, 0, 0), 527958),
        (datetime.datetime(2020, 4, 12, 0, 0), 556517), (datetime.datetime(2020, 4, 13, 0, 0), 581810),
        (datetime.datetime(2020, 4, 14, 0, 0), 608845), (datetime.datetime(2020, 4, 15, 0, 0), 637974),
        (datetime.datetime(2020, 4, 16, 0, 0), 669272), (datetime.datetime(2020, 4, 17, 0, 0), 701996),
        (datetime.datetime(2020, 4, 18, 0, 0), 730317), (datetime.datetime(2020, 4, 19, 0, 0), 756375),
        (datetime.datetime(2020, 4, 20, 0, 0), 783716), (datetime.datetime(2020, 4, 21, 0, 0), 809213),
        (datetime.datetime(2020, 4, 22, 0, 0), 837414), (datetime.datetime(2020, 4, 23, 0, 0), 871617),
        (datetime.datetime(2020, 4, 24, 0, 0), 907908), (datetime.datetime(2020, 4, 25, 0, 0), 940829),
        (datetime.datetime(2020, 4, 26, 0, 0), 968517), (datetime.datetime(2020, 4, 27, 0, 0), 990993),
        (datetime.datetime(2020, 4, 28, 0, 0), 1015518), (datetime.datetime(2020, 4, 29, 0, 0), 1042926),
        (datetime.datetime(2020, 4, 30, 0, 0), 1072667)]


def calendar_in_Chinese():
    calendar = Calendar(init_opts=opts.InitOpts(theme='light',
                                                width='1000px',
                                                height='600px'))
    calendar.add('确诊人数',
                 yaxis_data=data,
                 label_opts=opts.LabelOpts(is_show=True),
                 calendar_opts=opts.CalendarOpts(
                     # 日期范围
                     range_=['2020-01-21', '2020-04-30'],
                     # 日历单元格尺寸
                     cell_size=50,
                     # 年月日标签样式设置
                     # 星期和月份设置为中文显示，默认是英文
                     yearlabel_opts=opts.CalendarYearLabelOpts(margin=50),
                     daylabel_opts=opts.CalendarDayLabelOpts(name_map='cn'),
                     monthlabel_opts=opts.CalendarMonthLabelOpts(name_map='cn')
                 )
                 )
    # 设置视觉组件
    calendar.set_global_opts(visualmap_opts=opts.VisualMapOpts(
        max_=1000000,
        is_piecewise=True,
        pieces=[{"min": 1000000},
                {"min": 10000, "max": 1000000},
                {"min": 100, "max": 10000},
                {"max": 100}],
        range_color=["#CCD3D9", "#E6B6C2", "#D4587A", "#DC364C"]
    ))
    return calendar


chart = calendar_in_Chinese()
chart.render_notebook()


# #### 34.GEO添加自定义坐标

# In[35]:


from pyecharts.charts import *
from pyecharts import options as opts


def geo_add_custom_coordinate():
    geo = Geo(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    # 添加自定义坐标点
    geo.add_coordinate('x', 116.397428, 39.90923)
    geo.add_coordinate('y', 112.398615, 29.91659)

    geo.add_schema(maptype="china")
    geo.add("", [('x', 1), ('y', 2)])

    return geo


chart = geo_add_custom_coordinate()
chart.render_notebook()


# #### 35.GEO使用国外地图

# In[36]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.datasets import register_url
import ssl


def geo_foreign_country():
    # 添加其他国家的地图
    # noinspection PyBroadException
    try:
        register_url("https://echarts-maps.github.io/echarts-countries-js/")
    except Exception:
        ssl._create_default_https_context = ssl._create_unverified_context
        register_url("https://echarts-maps.github.io/echarts-countries-js/")

    geo = Geo(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))

    geo.add_schema(maptype="美国")

    return geo


chart = geo_foreign_country()
chart.render_notebook()


# #### 36.GEO 带涟漪效果散点图

# In[37]:


from pyecharts.charts import *
from pyecharts import options as opts


def geo_effect_scatter():
    geo = Geo(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))

    geo.add_schema(maptype="china")

    geo.add("",
            [("广州", 150), ("北京", 70), ("长沙", 64), ("上海", 74),  ("厦门", 63)],
            # 涟漪效果散点图
            type_='effectScatter')

    return geo


chart = geo_effect_scatter()
chart.render_notebook()


# #### 37.GEO热力图

# In[38]:


from pyecharts.charts import *
from pyecharts import options as opts


def geo_heatmap():
    geo = Geo(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))

    geo.add_schema(maptype="china")

    geo.add("",
            [("广州", 150), ("北京", 70), ("深圳", 64), ("上海", 74),  ("杭州", 63)],
            type_='heatmap')
    # 热点图必须配置visualmap_opts
    geo.set_global_opts(visualmap_opts=opts.VisualMapOpts())
    return geo


chart = geo_heatmap()
chart.render_notebook()


# #### 38.GEO 线图

# In[39]:


from pyecharts.charts import *
from pyecharts import options as opts


def geo_lines():
    geo = Geo(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))

    geo.add_schema(maptype="china")

    geo.add("广州出发",
            # 数据格式（from， to）
            [("广州", "上海"), ("广州", "北京"), ("广州", "西宁"), ("广州", "重庆")],
            type_='lines')
    geo.add("成都出发",
            # 数据格式（from， to）
            [("成都", '长沙'), ("成都", "武汉"), ("成都", "长春"), ("成都", "南京")],
            type_='lines')

    return geo


chart = geo_lines()
chart.render_notebook()


# #### 39.饼图自定义图形半径范围

# In[40]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def pie_custom_radius():
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    pie.add("",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            # 设置半径范围，0%-100%
            radius=["40%", "75%"])

    return pie


chart = pie_custom_radius()
chart.render_notebook()


# #### 40.饼图自定义数据标签

# In[41]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def pie_with_custom_label():
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    pie.add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    pie.set_series_opts(
        # 自定义数据标签
        label_opts=opts.LabelOpts(position='top',
                                  color='red',
                                  font_family='Arial',
                                  font_size=12,
                                  font_style='italic',
                                  interval=1,
                                  formatter='{b}:{d}%'
                                  )
    )

    return pie


chart = pie_with_custom_label()
chart.render_notebook()


# #### 41.多饼图

# In[42]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def pie_multiple():
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='800px'))
    pie.add("",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            radius=["20%", "50%"],
            center=["25%", "50%"])
    # 添加多个饼图
    pie.add("",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            radius=["20%", "50%"],
            center=["75%", "50%"])

    return pie


chart = pie_multiple()
chart.render_notebook()


# #### 42.散点图添加视觉组件（图形大小）

# In[43]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def scatter_with_visualmap_size():
    scatter = Scatter(init_opts=opts.InitOpts(theme='light',
                                              width='1000px',
                                              height='600px'))
    scatter.add_xaxis(Faker.choose())
    scatter.add_yaxis('', Faker.values())
    # 设置视觉组件
    scatter.set_global_opts(visualmap_opts=opts.VisualMapOpts(type_='size'))
    return scatter


chart = scatter_with_visualmap_size()
chart.render_notebook()


# #### 43.散点图添加视觉组件（图形大小&颜色）

# In[44]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = [random.randint(0, 100) for _ in range(30)]
y_data = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for _ in range(30)]


def scatter_with_visualmap_color_size():
    scatter = Scatter(init_opts=opts.InitOpts(theme='light',
                                              width='1000px',
                                              height='600px'))
    scatter.add_xaxis(x_data)
    scatter.add_yaxis('', y_data)
    # 多个映射维度通过list形式传入
    # dimension指定数据维度
    scatter.set_global_opts(visualmap_opts=[opts.VisualMapOpts(is_show=True, type_='size', dimension=2, pos_top='20%'),
                                            opts.VisualMapOpts(is_show=True, type_='color', dimension=3,  pos_top='60%')
                                            ],
                            xaxis_opts=opts.AxisOpts(type_="value"))
    return scatter


chart = scatter_with_visualmap_color_size()
chart.render_notebook()


# #### 44.散点图添加视觉组件（图形大小&颜色&透明度）

# In[45]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = [random.randint(0, 100) for _ in range(30)]
y_data = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
          for _ in range(30)]


def scatter_with_visualmap_color_size_opacity():
    scatter = Scatter(init_opts=opts.InitOpts(theme='light',
                                              width='1000px',
                                              height='600px'))
    scatter.add_xaxis(x_data)
    scatter.add_yaxis('', y_data)
    # 多个映射维度通过list形式传入
    # dimension制定数据维度
    scatter.set_global_opts(visualmap_opts=[opts.VisualMapOpts(is_show=True, type_='size', dimension=2, pos_top='10%'),
                                            opts.VisualMapOpts(is_show=True, type_='color', dimension=3, pos_top='40%'),
                                            opts.VisualMapOpts(is_show=True, type_='opacity', dimension=4,
                                                               # VisualMapOpt中对于range_opacity没给默认值，需要自行设定
                                                               range_opacity=[0.2, 1], pos_top='70%')],
                            xaxis_opts=opts.AxisOpts(type_="value"))
    return scatter


chart = scatter_with_visualmap_color_size_opacity()
chart.render_notebook()


# #### 45.自定义背景颜色

# In[46]:


from pyecharts.charts import *
from pyecharts import options as opts
import random


x_data = [random.randint(0, 100) for _ in range(30)]
y_data = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for _ in range(30)]


def scatter_with_custom_bgColor():
    scatter = Scatter(
        init_opts=opts.InitOpts(theme='light',
                                width='1000px',
                                height='600px',
                                # 自定义背景颜色
                                bg_color='#008B8B'))
    scatter.add_xaxis(x_data)
    scatter.add_yaxis('', y_data)
    # 多个映射维度通过list形式传入
    # dimension制定数据维度
    scatter.set_global_opts(visualmap_opts=[opts.VisualMapOpts(is_show=True, type_='size', dimension=2),
                                            opts.VisualMapOpts(is_show=True, type_='color', dimension=3)],
                            xaxis_opts=opts.AxisOpts(type_="value"))
    return scatter


chart = scatter_with_custom_bgColor()
chart.render_notebook()


# #### 46.词云图自定义字体范围

# In[47]:


from pyecharts.charts import *
from pyecharts import options as opts
import random

text = """
I used to rule the world
Seas would rise when I gave the word
Now in the morning I sleep alone
Sweep the streets I used to own
I used to roll the dice
Feel the fear in my enemy eyes
Listen as the crowd would sing
Now the old king is dead
Long live the king
One minute I held the key
Next the walls were closed on me
And I discovered that my castles stand
Upon pillars of salt and pillars of sand
I hear Jerusalem bells are ringing
Roman Cavalry choirs are singing
Be my mirror my sword and shield
My missionaries in a foreign field
For some reason I can't explain
Once you go there was never
Never an honest word
That was when I ruled the world
"""

word_list = set(text.split(' '))

words = [(word, random.randint(1, 100)) for word in word_list]


def wordcloud_custom_word_size():
    wordcloud = WordCloud(init_opts=opts.InitOpts(theme='light',
                                                  width='1000px',
                                                  height='600px'))
    wordcloud.add('',
                  words,
                  # 设置字体大小范围
                  word_size_range=[10, 50])

    return wordcloud


chart = wordcloud_custom_word_size()
chart.render_notebook()


# #### 47.Map带视觉组件

# In[48]:


from pyecharts.charts import *
from pyecharts import options as opts

data = [('广东', 10430),
        ('山东', 9579),
        ('河南', 9402),
        ('四川', 8041),
        ('江苏', 7866),
        ('河北', 7185),
        ('湖南', 6568),
        ('安徽', 5950),
        ('湖北', 5724),
        ('浙江', 5442),
        ('广西', 4603),
        ('云南', 4597),
        ('江西', 4457),
        ('辽宁', 4375),
        ('黑龙江', 3831),
        ('陕西', 3733),
        ('山西', 3571),
        ('福建', 3552),
        ('贵州', 3477),
        ('重庆', 2884),
        ('吉林', 2746),
        ('甘肃省', 2557),
        ('内蒙古', 2471),
        ('台湾', 2316),
        ('上海', 2301),
        ('新疆', 2181),
        ('北京', 1961),
        ('天津', 1294),
        ('海南', 867),
        ('香港', 710),
        ('宁夏', 630),
        ('青海', 562),
        ('西藏', 300),
        ('澳门', 55)]


def map_with_viusalmap():
    map_chart = Map(init_opts=opts.InitOpts(theme='light',
                                            width='1000px',
                                            height='600px'))
    map_chart.add('人口（万人）',
                  data_pair=data,
                  maptype='china',
                  # 关闭symbol的显示
                  is_map_symbol_show=False)

    map_chart.set_global_opts(visualmap_opts=opts.VisualMapOpts(
        max_=10430,  # visualmap默认映射数据范围是【0，100】，需调整
        is_piecewise=True,
        range_color=["#CCD3D9", "#E6B6C2", "#D4587A", "#DC364C"]
    ))
    return map_chart


chart = map_with_viusalmap()
chart.render_notebook()


# #### 48.Page更改布局

# In[49]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def page_simple_layout():
    # 图表1
    bar_1 = Bar(init_opts=opts.InitOpts(theme='light',
                                        width='500px',
                                        height='300px'))
    bar_1.add_xaxis(Faker.choose())
    bar_1.add_yaxis('A', Faker.values())
    bar_1.add_yaxis('B', Faker.values())

    # 图表2
    bar_2 = Bar(init_opts=opts.InitOpts(theme='light',
                                        width='500px',
                                        height='300px'))
    bar_2.add_xaxis(Faker.choose())
    bar_2.add_yaxis('A', Faker.values())
    # x,y轴翻转
    bar_2.reversal_axis()

    # 图表3
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='500px',
                                        height='300px'))
    line.add_xaxis(Faker.choose())
    line.add_yaxis('A', Faker.values())
    line.add_yaxis('B', Faker.values())

    # 图表4
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='500px',
                                      height='300px'))
    pie.add("",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            radius=["40%", "75%"])

    page = Page(layout=Page.SimplePageLayout)
    # 需要自行调整每个 chart 的 height/width，布局会因为页面大小而不同
    page.add(bar_1, bar_2, line, pie)

    return page


chart = page_simple_layout()
chart.render_notebook()


# #### 49.一个Tab下带多个图表
# 
# * 通过Grid将多个图表组合，然后再将Grid添加到Tab中；

# In[50]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def tab_with_multiple_chart():
    # 图表1
    bar = Bar()
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis("商家A", Faker.values())
    bar.add_yaxis("商家B", Faker.values())

    # 图表2
    line = Line()
    line.add_xaxis(Faker.choose())
    line.add_yaxis("商家A", Faker.values())
    line.add_yaxis("商家B", Faker.values())

    # 先通过Grid将图表1和图表2组合起来
    grid = Grid()
    grid.add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
    grid.add(line, grid_opts=opts.GridOpts(pos_top="60%"))

    # 再将Grid添加到Tab
    tab = Tab()
    tab.add(grid, '示例')

    return tab


chart = tab_with_multiple_chart()
chart.render_notebook()


# #### 50.Timeline 自动播放

# In[51]:


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def timeline_auto_play():
    timeline = Timeline(init_opts=opts.InitOpts(theme='light',
                                                width='1000px',
                                                height='600px'))
    timeline.add_schema(is_auto_play=True,  # 自动播放
                        is_loop_play=True  # 循环播放
                        )
    for year in range(2000, 2020):
        bar = Bar()
        bar.add_xaxis(['香蕉', '梨子', '水蜜桃', '核桃', '西瓜', '苹果', '菠萝'])
        bar.add_yaxis('A', Faker.values())
        bar.add_yaxis('B', Faker.values())
        timeline.add(bar, '{}年'.format(year))
    return timeline


chart = timeline_auto_play()
chart.render_notebook()

