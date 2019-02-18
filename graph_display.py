import pandas as pd
from bokeh.io import show, curdoc
from bokeh.models import ColumnDataSource, HoverTool, Select, Axis, CustomJS
from bokeh.plotting import figure, output_file
from bokeh.layouts import column

df = pd.read_csv('path file to...HighestGrossingFilms.csv')


name = df.loc[:, 'Name']
year = df.loc[:, 'Year']
revenue = df.loc[:, 'Revenue']
name2014 = df.loc[:, 'Name2014']
revenue2014 = df.loc[:, 'Revenue2014']
name2015 = df.loc[:, 'Name2015']
revenue2015 = df.loc[:, 'Revenue2015']
name2016 = df.loc[:, 'Name2016']
revenue2016 = df.loc[:, 'Revenue2016']
name2017 = df.loc[:, 'Name2017']
revenue2017 = df.loc[:, 'Revenue2017']


source = ColumnDataSource(data=dict(revenue=revenue, year=year, name=name,
                                    name2014=name2014, revenue2014=revenue2014,
                                    name2015=name2015, revenue2015=revenue2015,
                                    name2016=name2016, revenue2016=revenue2016,
                                    name2017=name2017, revenue2017=revenue2017))


p = figure(title="Highest Grossing Films of All Time vs. The Past Five Years")
p.scatter(x='year', y='revenue', size=10, source=source, legend="All Time")
p.legend.click_policy = "hide"
yaxis = p.select(dict(type=Axis, layout="left"))[0]
yaxis.formatter.use_scientific = False


menu = Select(options=['All Time', '2014', '2015', '2016', '2017'],
              value='uniform', title='Distribution')


def callback(attr, old, new):
    if menu.value == 'All Time':
        r1 = p.scatter(x='year', y='revenue', size=10, source=source,
                       legend="All Time")
        p.add_tools(HoverTool(renderers=[r1], tooltips=[('name', '@name')]))

    if menu.value == '2014':
        r2 = p.scatter(x='year', y='revenue2014', size=8,
                       color='green', source=source, legend="2014")
        p.add_tools(HoverTool(renderers=[r2], tooltips=[('name2014', '@name2014')]))

    if menu.value == '2015':
        r3 = p.scatter(x='year', y='revenue2015', size=8, color='red', source=source,
                       legend="2015")
        p.add_tools(HoverTool(renderers=[r3], tooltips=[('name2015', '@name2015')]))

    if menu.value == '2016':
        r4 = p.scatter(x='year', y='revenue2016', size=8, color='orange', source=source,
                       legend="2016")
        p.add_tools(HoverTool(renderers=[r4], tooltips=[('name2016', '@name2016')]))

    if menu.value == '2017':
        r5 = p.scatter(x='year', y='revenue2017', size=8, color='purple',
                       source=source, legend="2017")
        p.add_tools(HoverTool(renderers=[r5], tooltips=[('name2017', '@name2017')]))


menu.on_change('value', callback)
layout = column(menu, p)
curdoc().add_root(layout)
