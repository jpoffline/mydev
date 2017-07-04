""" General helper tools """
import time


def collapse_dict(input_dict, sep_pair=' ', link='=', val_surround='\"', key_surround=''):
    """ Collapse a dict """
    fmt = key_surround + '{}' + key_surround + \
        link + val_surround + '{}' + val_surround
    return sep_pair.join([fmt.format(k, v) for k, v in sorted(input_dict.iteritems())])


def collapse_dict_css(input_css):
    """
    Collapse a dict of css type
    """
    return collapse_dict(input_css, sep_pair='; ', link=': ', val_surround='')


def collapse_css_ajax(input_css):
    """ Return a css string suitable for use in AJAX. """
    return collapse_dict(input_css, sep_pair=', ', link=': ', val_surround='\"', key_surround='\"')


def collapse_css(input_css):
    """
    Collapse a full css doc to string.

    Example input:

    input_css = {
        'body': {
            'background-color': 'lightblue'
        },
        'div' :{
            'background-color': 'green'
        }
    }

    """
    if input_css is None:
        return ''
    string = ''
    for key, val in input_css.iteritems():
        string += key + ' {' + collapse_dict_css(val) + ';} '
    return string
