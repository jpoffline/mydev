""" General helper tools """


def collapse_dict(in_dict, sep_pair=' ', link='=', val_surround='\"',
                  key_surround=''):
    """ Collapse a dict """
    fmt = key_surround + '{}' + key_surround + \
        link + val_surround + '{}' + val_surround
    return sep_pair.join([fmt.format(k, v)
                          for k, v in sorted(in_dict.iteritems())])


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


def get_dict_keys(input_dict):
    """ Get the keys in a dict """
    return set(input_dict.keys())


def diff_dict(dict1, dict2):
    """ Get the difference between two dicts """
    # HAS_UNIT_TESTS

    # Check keys are identical
    keys_dict1 = get_dict_keys(dict1)
    keys_dict2 = get_dict_keys(dict2)
    keys_same = keys_dict1 ^ keys_dict2

    if keys_same == set([]):
        is_ks = True
    else:
        is_ks = False

    returns = {}

    returns['keys'] = is_ks
    if is_ks is False:
        returns['diff_keys'] = keys_same

    # Check content is identical
    diffs = []
    for key_dict1, val_dict1 in dict1.iteritems():
        if key_dict1 in keys_dict2 and not val_dict1 == dict2[key_dict1]:
            diffs.append({key_dict1: (
                val_dict1, dict2[key_dict1]
            )})

    if len(diffs) > 0:
        returns['val_diffs'] = diffs
        returns['vals'] = False
    else:
        returns['vals'] = True
    return returns


def truncate_string(in_str, mlen=25):
    """ Truncate a string; append longer with dots """
    return (in_str[:mlen] + '...') if len(in_str) > mlen else in_str


def append_gbp(in_str):
    """ Append a number with the GBP-symbol """
    if in_str is None:
        in_str = 0
    return u"\xA3" + "%.2f" % in_str

def digit_to_time(digit):
    if digit > 9:
        return str(digit)
    return '0' + str(digit)