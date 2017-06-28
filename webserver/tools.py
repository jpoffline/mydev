""" General helper tools """

def collapse_dict(input_dict, sep_pair=' ', link='=', val_surround='\"'):
    """ Collapse a dict """
    fmt = '{}' + link + val_surround + '{}' + val_surround
    return sep_pair.join([fmt.format(k, v) for k, v in sorted(input_dict.iteritems())])

def collapse_dict_css(input_css):
    """ Collapse a dict of css type """
    return collapse_dict(input_css, sep_pair='; ', link=': ', val_surround='')

def collapse_css(input_css):
    """ Collapse a full css doc to string """
    if input_css is None:
        return ''
        
    string = ''
    for k,v in input_css.iteritems():
        string += k + ' {' + collapse_dict_css(v) + ';} '
    return string