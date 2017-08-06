def allowed_strings():
    return ['year', 'month', 'day', 'hour', 'minute']


def to_fmtstring(agglevel):
    if agglevel == 'hour':
        return '%Y-%m-%d %H'
    elif agglevel == 'minute':
        return '%Y-%m-%d %H:%M'
    elif agglevel == 'year':
        return '%Y'
    elif agglevel == 'month':
        return '%Y-%m'
    elif agglevel == 'day':
        return '%Y-%m-%d'
    else:
        return False

def to_fmt(what):
    if what == 'day':
        return '%d'
    elif what == 'month':
        return '%m'
    elif what == 'year':
        return '%Y'
    else:
        return False