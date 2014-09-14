import pygal
import logging
import os 
import sys


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
