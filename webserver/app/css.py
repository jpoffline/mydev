""" Holder for app css """


def get_simple_css():
    """ Create an return a simple css object """
    return {
        'body': {
            'background-color': 'lightblue'
        },
        '#half_width': {
            'background-color': 'lightblue',
            'width': '50%'
        },
        '#response':
        {
            'color': 'white'
        },
        'input[type=submit]:hover': {
            'background-color': '#45a049'
        },
        'input[type=text], select': {
            'width': '100%',
            'padding': '12px 20px',
            'margin': '8px 0',
            'display': 'inline-block',
            'border': '1px solid #ccc',
            'border-radius': '4px',
            'box-sizing': 'border-box'
        },
        'input[type=submit]': {
            'width': '100%',
            'background-color': '#4CAF50',
            'color': 'white',
            'padding': '14px 20px',
            'margin': '8px 0',
            'border': 'none',
            'border-radius': '4px',
            'cursor': 'pointer'
        }
    }
