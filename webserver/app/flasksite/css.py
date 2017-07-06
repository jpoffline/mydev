""" Site css """
import context
import lib.widgets.default_css as widgetcss


def global_body():
    """ The page body css """
    return {
        'body': {
            'background-color': 'LightBlue'
        }
    }


def global_css():
    """ Return the global css """
    css = {}
    css.update(global_body())
    css.update(widgetcss.global_jp_widgets())
    return css
