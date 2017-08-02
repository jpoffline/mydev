""" Module for plotting stuff for sales """

from plotly import tools as plytools
import plotly
import plotly.graph_objs as go
import datetime

def plot_box(data, meta):
    """ Put a plot into a bootstrap well """
    trace = go.Scatter(
        x=data['x'],
        y=data['y'],
        text=data['text']
    )

    div = plotly.offline.plot({
        "data": [trace],
        "layout": go.Layout(
            title=meta.get('title', 'data')
        )
    },
        show_link=False,
        output_type="div",
        include_plotlyjs=False)

    return div

def agg_sales_stats(data):
    """ Generate a text string per
    item for the sales data """
    mean = sum(data['sales']) / len(data['sales'])
    maxdata = max(data['sales'])
    meta = []
    for idx, point in enumerate(data['sales']):
        dev = round(point - mean, 2)
        frc = round(point / mean * 100, 2)
        fmx = round(point / maxdata * 100, 2)
        text = data['times'][idx] + "<br>" + \
            'Number of sales: ' + str(data['counts'][idx]) + '<br>' + \
            'Deviation from average: ' + str(dev) + '<br>' +\
            'Fraction of average: ' + str(frc) + '%' + '<br>' +\
            'Fraction of maximum: ' + str(fmx) + '%'
        meta.append(text)
    return meta

def comparisons_point_label(data):
    meta = []
    date = datetime.datetime.strptime(
                data['date'], '%Y-%m').strftime('%B %Y')

    maxamt = max(data['sales']['amounts'])
    for idx, point in enumerate(data['sales']['amounts']):
        frcmx = round(point / maxamt * 100, 2)
        text = data['sales']['dates'][idx] + \
        ' ' + date + "<br>" + \
        'Number of sales: ' + str(data['sales']['counts'][idx]) + '<br>' + \
        'Fraction of maximum: ' + str(frcmx) + '%'
        meta.append(text)
    return meta

def plot_comparisons(comparison_data, meta):
    traces = []
    for data in comparison_data:
        date = data['date']
        amounts = data['sales']['amounts']
        counts = data['sales']['counts']
        days = data['sales']['dates']
        trace = go.Scatter(
            x=days,
            y=amounts,
            name=date,
            text=comparisons_point_label(data)
        )
        traces.append(trace)
    div = plotly.offline.plot({
        "data": traces,
        "layout": go.Layout(title=meta.get('title', 'data'),
                            xaxis=dict(
            title=meta.get('xlabel', 'x')
        ),
            yaxis=dict(
                title=meta.get('ylabel', 'y')
        ))

    },
        show_link=False,
        output_type="div",
        include_plotlyjs=False)

    return div


def plot_sales(sales_data, meta=None):
    """ Plot the sales data """
    return plot_box({'x': sales_data['times'], 'y': sales_data['sales']}, None)
    aggplot_label = 'By ' + meta['agglevel']
    # Construct the aggregated-sales plot
    trace0 = go.Scatter(
        x=sales_data['times'],
        y=sales_data['sales'],
        text=sales_data['counts'],
        name=aggplot_label)

    # Construct the raw sales plot
    trace1 = go.Scatter(
        x=sales_data['id'],
        y=sales_data['amount'],
        xaxis='x2',
        yaxis='y2',
        name='Raw',
        text=sales_data['date'])

    trace2 = go.Scatter(
        x=sales_data['times'],
        y=sales_data['cumulative'],
        name='Cumulative',
        text=sales_data['date'])

    graph = plytools.make_subplots(rows=2,
                                   cols=2,
                                   subplot_titles=(
                                       aggplot_label, 'Raw', 'Cumulative'),
                                   print_grid=False)

    graph.append_trace(trace0, 1, 1)
    graph.append_trace(trace1, 1, 2)
    graph.append_trace(trace2, 2, 1)

    graph['layout']['xaxis1'].update(title='Time')
    graph['layout']['xaxis2'].update(title='Transaction ID')
    graph['layout']['yaxis1'].update(title='Amount')
    graph['layout']['yaxis2'].update(title='Amount')
    graph['layout'].update(showlegend=False, title='Sales summary')

    div = plotly.offline.plot(graph,
                              show_link=False,
                              output_type="div",
                              include_plotlyjs=False)

    return div
