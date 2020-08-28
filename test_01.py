__author__ = 'Gino'
# _*_ coding:utf-8 _*_
# .@FileName :test_01
# .@Date....:2020-08-28 : 10 :17
# .@Contact:yanjincai@foxmail.com
'''
launch :
        import test_01 as gn_FileName
        reload(FileName)
        FileName.main()
'''
from pyecharts.charts import Bar
from pyecharts import options as opts

# Bar 参数数据格式
x = ['python数据可视化库 seaborn', 'python数据可视化库 plotly', 'python数据可视化库 matplotlib']
y1 = [1140, 550, 270]
y2 = [2324, 546, 789]

bar = Bar()  # 实例对象
bar.add_xaxis(xaxis_data=x)  # 轴坐标的数据
bar.add_yaxis(series_name='平台A', yaxis_data=y1)  # 图例并称+y轴数据
bar.add_yaxis(series_name='平台B', yaxis_data=y2)  # 图例并称+y轴数据

# 标题
bar.set_global_opts(title_opts=opts.TitleOpts(title='不同销售平台销售数量'))

# 坐标轴转换
bar.reversal_axis()

# 生成HTML文件
print(bar.render(path='first_bar.html'))
