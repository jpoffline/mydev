import plotly

def traces_layout_to_div(traces, layout):
    """ Return a plotly div for an inputted
    set of traces and the layout.
    """
    return graph_to_div({
        "data": traces,
        "layout": layout
    })

def graph_to_div(graph):
    """ Return a plotly plot for an inputted graph-object;

    Parameters
    ----------
    graph : Dict containing data and layout keys.
     {
        "data": TRACES,
        "layout": LAYOUT
    }
    """
    return plotly.offline.plot(graph,
                               show_link=False,
                               output_type="div",
                               include_plotlyjs=False)