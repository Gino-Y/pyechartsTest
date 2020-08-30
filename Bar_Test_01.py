__author__ = 'Gino'
# _*_ coding:utf-8 _*_
# .@FileName :Bar_Test_01
# .@Date....:2020-08-30 : 17 :17
# .@Contact:yanjincai@foxmail.com
'''
launch :
        import Bar_Test_01 as gn_FileName
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
    y1 = [1234, 2329, 2134]
    y2 = [464, 789, 744]

    c = Bar(init_opts=opts.InitOpts(width='1000px', height='600px'))
    c.add_xaxis(xaxis_data=x)
    c.add_yaxis(series_name='平台1 销售数据', yaxis_data=y1)
    c.add_yaxis(series_name='平台2 销售数据', yaxis_data=y2)

    c.set_global_opts(

        title_opts=opts.TitleOpts(title='不同平台销售统计'),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=60)),
        legend_opts = opts.LegendOpts(is_show=True),
        datazoom_opts=opts.DataZoomOpts(type_='slider', range_start=0, range_end=1500)


    )
    return c


if __name__ == "__main__":
    c = bar_charts()
    print(c.render(path='Bar_Test_01.html'))
