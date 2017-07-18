""" Module for plotting stuff for sales """

from plotly import tools as plytools
import plotly
import plotly.graph_objs as go


def plot_sales(sales_data):
    """ Plot the sales data """
    # Construct the aggregated-sales plot
    trace0 = go.Scatter(
        x=sales_data['times'],
        y=sales_data['sales'],
        text=sales_data['counts'],
        name='By hour')

    # Construct the raw sales plot
    trace1 = go.Scatter(
        x=sales_data['id'],
        y=sales_data['amount'],
        xaxis='x2',
        yaxis='y2',
        name='Raw',
        text=sales_data['date'])

    graph = plytools.make_subplots(rows=1,
                                   cols=2,
                                   subplot_titles=('By hour', 'Raw'),
                                   print_grid=False)

    graph.append_trace(trace0, 1, 1)
    graph.append_trace(trace1, 1, 2)

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
