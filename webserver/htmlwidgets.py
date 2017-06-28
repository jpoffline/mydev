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


def div(text, style=None):
    """ Generate a HTML-div environment """
    # HAS_UNIT_TESTS
    if style is None:
        return tag_div() + text + tag_div(open=False)
    return tag_div(style=style) + text + tag_div(open=False)


def label(text):
    # HAS_UNIT_TESTS
    return tag_label() + text + tag_label(open=False)


def form(method, action, text):
    return tag_form(method, action) + text + tag_form(open=False)


def img(src):
    return tag_img(src)


def pagePut(anchor, replies, what):
    if not replies:
        return ''
    elif not '/' + anchor == replies[0]:
        return ''

    for rep in replies[1:]:
        what = what.replace('?' + rep['key'], rep['val'])

    return what

# Compound widgets


def input_submit(text, id, type='text'):
    return label(text) + tag_input(type, id) + tag_input('submit', 'Send')


def input_submit_form(id, labels, vars):
    # HAS_UNIT_TESTS
    ii = ''
    n = len(labels)
    for i in xrange(0, n):
        ii += input_submit(labels[i], vars[i])
    return form('POST', srv.gen_post_string(id, vars), ii)
