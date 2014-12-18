import pygal
import logging
import os 
import sys
from pygal.style import RotateStyle, LightColorizedStyle

def create_graph(kpi_list, chart_name='chart.svg', chart_title='default'):
    labels = []
    for label in kpi_list:
        labels.append(label)
        chart = pygal.Line(fill=True, width=1440, height=500, title=chart_title,
                           legend_at_bottom=True)
        chart.x_labels = map(str, range(0,sample))
        for line, series in kpi_list.items():
            chart.add(line,series)
            chart.render_to_file(os.path.join(os.path.sep, graph_dir, chart_name))


def plot_test_light_theme():
    dark_rotate_style = RotateStyle('#75ff98', base_style=LightColorizedStyle)
    chart = pygal.StackedLine(fill=True, interpolate='cubic', style=dark_rotate_style)
    chart.add('A', [1, 3,  5, 16, 13, 3,  7])
    chart.add('B', [5, 2,  3,  2,  5, 7, 17])
    chart.add('C', [6, 10, 9,  7,  3, 1,  0])
    chart.add('D', [2,  3, 5,  9, 12, 9,  5])
    chart.add('E', [7,  4, 2,  1,  2, 10, 0])
    chart.render_to_file(
        '/home/vectra/projects/servicedeskaid/viewpanel/static/graphs/style.svg'
    )


def plot_bar_chart():
    horizontalbar_chart = pygal.HorizontalBar()
    horizontalbar_chart.title = 'Performance by issues worked (in %)'
    horizontalbar_chart.add('Luiza', 19.5)
    horizontalbar_chart.add('Anna', 36.6)
    horizontalbar_chart.add('John', 36.3)
    horizontalbar_chart.add('Walter', 4.5)
    horizontalbar_chart.add('Jack', 2.3)
    horizontalbar_chart.render_to_file(
        '/home/vectra/projects/servicedeskaid/viewpanel/static/graphs/plot.svg'
    )

plot_bar_chart()
plot_test_light_theme()
