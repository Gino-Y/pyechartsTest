__author__ = 'Gino'
# _*_ coding:utf-8 _*_
# .@FileName :Line_Test_01
# .@Date....:2020-08-30 : 17 :53
# .@Contact:yanjincai@foxmail.com
'''
launch :
        import Line_Test_01 as gn_FileName
        reload(FileName)
        FileName.main()
'''
from pyecharts import options as opts
from pyecharts.charts import Bar, Line


x = ['Python', 'Seaborn', 'Plotly', 'pyecharts']
# 绘制柱状图方法
def bar_charts() -> Bar():
    y1 = [1140, 559, 270, 523]
    y2 = [570, 1358, 1248, 1234]
    bar = Bar(init_opts=opts.InitOpts(width='1920px', height='1080px'))
    bar.add_xaxis(xaxis_data=x)
    bar.add_yaxis(series_name='平台A—销售数量', yaxis_data=y1, label_opts=opts.LabelOpts(is_show=False))
    bar.add_yaxis(series_name='平台B—销售数量', yaxis_data=y2, label_opts=opts.LabelOpts(is_show=False))
    bar.set_global_opts(title_opts=opts.TitleOpts(title='不同平台销售数量'))

    # bar扩展
    bar.extend_axis(
        yaxis=opts.AxisOpts(
            name='价格',
            type_='value',
            min_=0,
            max_=200,
            interval=10,
            axislabel_opts=opts.LabelOpts(formatter='{value} 元')
        )
    )
    return bar

# 绘制Line 方法
def line_charts() -> Line():
    y = [159, 29, 49, 79]
    c = Line()
    c.add_xaxis(xaxis_data=x)
    c.add_yaxis(series_name='当前价格',
                yaxis_index=1,
                y_axis = y,
                label_opts=opts.LabelOpts(is_show=False))
    return c

# Bar + Line
bar = bar_charts()
line = line_charts()
print(bar.overlap(line).render(path='Line_Test_01.html'))
