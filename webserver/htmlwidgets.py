""" HTML widgets """

from htmltags import *
import serverhelp as srv
import tools as tools

def head(text, css=None):
    """ Generate a HTML-body environment """
    # HAS_UNIT_TESTS
    return tag_head() + title(text) + style(css) + tag_head(open=False)


def style(css):
    """ Generate a HTML-style environment """
    # HAS_UNIT_TESTS
    if css is None:
        return ''
    return tag_style() + tools.collapse_css(css) + tag_style(open=False)


def title(text):
    """ Generate a HTML-title environment """
    # HAS_UNIT_TESTS
    return tag_title() + text + tag_title(open=False)


def html(text, title=None, css=None):
    """ Generate a HTML-html environment """
    # HAS_UNIT_TESTS
    if title is None:
        title = 'Blank'
    return tag_html() + head(title, css=css) + text + tag_html(open=False)


def body(text):
    """ Generate a HTML-body environment """
    return tag_body() + text + tag_body(open=False)


def h1(text):  # pylint: disable=C0103
    """ Generate a HTML-h1 environment """
    return tag_h1() + text + tag_h1(open=False)


def div(text, style=None, options=None):
    """
    Generate a HTML-div environment

    Optionally pass in css-style or options dict.

    Example inputs:

    options = {
        'id': '1',
        'name': 'this_div'
    }

    style = {
        'color': 'blue',
        'weight': 'bold'
    }
    """
    # HAS_UNIT_TESTS
    if style is None and options is None:
        return tag_div() + text + tag_div(open=False)
    return tag_div(style=style, options=options) + text + tag_div(open=False)


def label(text):
    """ Generate a HTML-label environment """
    # HAS_UNIT_TESTS
    return tag_label() + text + tag_label(open=False)


def form(method, action, text):
    """ Generate a HTML-form environment """
    return tag_form(method, action) + text + tag_form(open=False)


def img(src):
    """
    Generate a HTML-img environment.

    src: The image URL.

    """
    return tag_img(src)


def pagePut(anchor, replies, what):
    """ Generate a HTML-page-put environment """
    if not replies:
        return ''
    elif not '/' + anchor == replies[0]:
        return ''

    for rep in replies[1:]:
        what = what.replace('?' + rep['key'], rep['val'])

    return what

# Compound widgets


def input_submit(text, submit_id, input_type='text', add_button=True, place_holder=None):
    """ Generate an input-submit form HTML-environment """
    html_input_submit = label(text)
    if place_holder is not None:
        html_input_submit += tag_input(input_type, submit_id, place_holder=place_holder)
    else:
        html_input_submit += tag_input(input_type, submit_id)
    if add_button:
        html_input_submit += tag_input('submit', 'send')
    return html_input_submit


def input_submit_form(form_id, labels, ids):
    """
    Generate an input form HTML-environment.

    Many input fields, with one button at the end.
    """
    # HAS_UNIT_TESTS
    form_text = ''
    for i in xrange(0, len(labels)-1):
        form_text += input_submit(labels[i], ids[i], add_button=False, place_holder=labels[i])
    last_idx = len(labels)-1
    form_text += input_submit(labels[last_idx], ids[last_idx], place_holder=labels[last_idx])
    return form('POST', srv.gen_post_string(form_id, ids), form_text)
