
""" Server helper functions """


def read_form(form, key):
    """ Read a form """
    if key in form:
        var = form[key].value

        if var == '':
            return 'empty'
        else:
            return var
    else:
        return 'False'

def gen_post_string(send, vars):
    """ Generate a POST string """
    # HAS_UNIT_TESTS
    return '/' + send + '?' + '&'.join(vars)


def gen_response_string(send, keys, values):
    """ Generate a reponse string """
    # HAS_UNIT_TESTS

    zipped = [m + '=' + n for m, n in zip(keys, values)]
    zipped = '&'.join(zipped)
    return send + '?' + zipped


def gen_pkt_item(key, value):
    """ Generate a packet item """
    return dict({
        'key': key,
        'val': value
    })


def deconstruct_response_string(string):
    """ 
    Deconstruct a response string 

    Parameters
    ----------
    string: string

    Returns
    -------
    List of packet items
    """
    # HAS_UNIT_TESTS

    first = string.split('?')
    items = first[1].split('&')
    pkts = [first[0]]

    for item in items:
        data = item.split('=')

        pkts.append(
            gen_pkt_item(
                data[0],
                data[1]
            )
        )

    return pkts
