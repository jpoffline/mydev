""" General helper tools """

def collapse_dict(input_dict, sep_pair=' ', link='=', val_surround='\"'):
    """ Collapse a dict """
    fmt = '{}' + link + val_surround + '{}' + val_surround
    return sep_pair.join([fmt.format(k, v) for k, v in input_dict.iteritems()])
