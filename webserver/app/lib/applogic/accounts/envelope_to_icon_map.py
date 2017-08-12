
def to_icon(text):
    return '<i class="fa fa-'+text+'" aria-hidden="true"></i>'

def env_to_icon_mapper(text):
    if text == 'giving':
        text = to_icon('recycle') + ' ' + text
    if text == 'bills':
        text = to_icon('shopping-basket') + ' ' + text
    if text == 'commute':
        text = to_icon('train') + ' ' + text
    if text == 'wages':
        text = to_icon('industry') + ' ' + text
    if text == 'house':
        text = to_icon('home') + ' ' + text
    if text == 'petrol':
        text = to_icon('car') + ' ' + text
    if text == 'saving':
        text = to_icon('life-buoy') + ' ' + text
    return text