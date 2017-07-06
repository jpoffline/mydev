""" Default css for the widgets """


def valuebox():
    """ Value box body css """
    return {
        'width': '90px',
        'background-color': 'red',
        'margin': '10px',
        'padding': '10px',
        'border': '2px solid black',
        'border-radius': '5px'
    }


def valuebox_title():
    """ Value box title css """
    return {
        'font-weight': 'bold'
    }


def global_valuebox():
    """ The full value box css """
    return {
        'div.jp-valuebox': valuebox(),
        'span.jp-valuebox-title': valuebox_title()
    }


def global_table():
    """ Table css """
    return {
        'table.jp-table': {
            'padding': '5px'
        },
        'table.jp-table tr:nth-child(even)': {
            'background': '#FFF8DC'
        },
        'table.jp-table tr:nth-child(odd)': {
            'background': '#FFF'
        },
        'table.jp-table td': {
            'padding': '5px'
        }
    }


def global_headers():
    return {
        'h1.jp': {
            'background': 'white'
        }
    }

def global_jp_widgets():
    """ Assemble and return the css for all widgets """
    css = {}
    css.update(global_valuebox())
    css.update(global_table())
    css.update(global_headers())
    return css



