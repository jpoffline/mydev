""" General helper tools """


def collapse_dict(input_dict, sep_pair=' ', link='=', val_surround='\"'):
    """ Collapse a dict """
    fmt = '{}' + link + val_surround + '{}' + val_surround
    return sep_pair.join([fmt.format(k, v) for k, v in sorted(input_dict.iteritems())])


def collapse_dict_css(input_css):
    """
    Collapse a dict of css type
    """
    return collapse_dict(input_css, sep_pair='; ', link=': ', val_surround='')


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

def pretty_time(time):
    """
    Return a pretty-string version of
    an inputted time in seconds
    """
    units = 'secs'
    if time > 60:
        time = time / 60
        units = 'mins'
    return str(round(time, 2)) + ' ' + units
