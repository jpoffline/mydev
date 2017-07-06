""" Default css for the widgets """

def valuebox():
    return {
        'width': '90px',
        'background-color': 'red',
        'margin': '10px',
        'padding': '10px'
    }


def valuebox_title():
    return {
        'font-weight': 'bold'
    }


def global_valuebox():
    return {
        'div.jp-valuebox': valuebox(),
        'span.jp-valuebox-title': valuebox_title()
    }


def global_body():
    """ The body css """
    return {
        'body': {
            'background-color': 'LightBlue'
        }
    }

def global_table():
    return {
        'table.jp-table' : {
            'background-color': 'LightCyan',
            'padding': '5px'
        },
        'table.jp-table tr:nth-child(even)': {
            'background': '#CCC'
        },
        'table.jp-table tr:nth-child(odd)': {
            'background': '#FFF'
        }
    }

def global_css():
    """ Return the global css """
    css = {}
    css.update(global_valuebox())
    css.update(global_body())
    css.update(global_table())
    return css
