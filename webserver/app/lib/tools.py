""" General helper tools """
import time
import datetime

def collapse_dict(in_dict, sep_pair=' ', link='=', val_surround='\"', key_surround=''):
    """ Collapse a dict """
    fmt = key_surround + '{}' + key_surround + \
        link + val_surround + '{}' + val_surround
    return sep_pair.join([fmt.format(k, v) for k, v in sorted(in_dict.iteritems())])


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


def val_to_rgb(value):
    """ Convert a value to an RGB-string """
    return 'rgb(' + str(value) + ',127,127)'


def get_username():
    """ Get the current user name """
    import getpass
    return getpass.getuser()


def get_hostname():
    """ Get the current host machine name """
    import socket
    return socket.gethostname()


def get_datetime():
    """ Get the current datetime stamp in YYYYMMDDHHMMSS-form """
    today = datetime.datetime.today()
    return today.strftime('%Y%m%d%H%M%S')
