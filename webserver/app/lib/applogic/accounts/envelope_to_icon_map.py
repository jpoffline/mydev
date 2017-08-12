
def to_icon(text):
    return '<i class="fa fa-'+text+'" aria-hidden="true"></i>'

def env_to_icon_mapper(text):
    if text == 'giving':
        text = to_icon('recycle') + ' ' + text
    if text == 'bills':
        text = to_icon('shopping-basket') + ' ' + text
    return text