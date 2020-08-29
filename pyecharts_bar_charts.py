__author__ = 'Gino'
# _*_ coding:utf-8 _*_
# .@FileName :pyecharts_bar_charts
# .@Date....:2020-08-29 : 17 :32
# .@Contact:yanjincai@foxmail.com
'''
launch :
        import pyecharts_bar_charts as gn_FileName
        reload(FileName)
        FileName.main()
'''
from pyecharts import options as opts
from pyecharts.charts import Bar


def bar_charts() -> Bar():
    """
    定义一个返回pyecharts Bar 的函数
    :return:
    """
    x = ['Python 数据可视化 seaborn', 'Python 数据可视化 plotly', 'Python 数据可视化 pyecharts']
    y1 = [1234, 232, 2134]

    c = Bar(init_opts=opts.InitOpts(width='1000px', height='600px'))
    c.add_xaxis(xaxis_data=x)
    c.add_yaxis(series_name='', yaxis_data=y1)

    c.set_global_opts(


        title_opts=opts.TitleOpts(title='不同平台销售统计'),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=60))
    )
    return c


if __name__ == "__main__":
    c = bar_charts()
    c.render(path='pyecharts_bar_charts.html')
