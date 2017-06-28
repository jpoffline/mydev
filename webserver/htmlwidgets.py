""" HTML widgets """

from htmltags import *
import serverhelp as srv


def html(text):
    """ Generate a HTML-html environment """
    # HAS_UNIT_TESTS
    return tag_html() + text + tag_html(open=False)


def body(text):
    """ Generate a HTML-body environment """
    return tag_body() + text + tag_body(open=False)


def h1(text): # pylint: disable=C0103
    """ Generate a HTML-h1 environment """
    return tag_h1() + text + tag_h1(open=False)


def div(text, style=None, styles=None):
    """ Generate a HTML-div environment """
    # HAS_UNIT_TESTS
    if not style and not styles:
        return tag_div() + text + tag_div(open=False)
    elif not styles:
        return tag_div(style=style) + text + tag_div(open=False)
    else:
        return tag_div(styles=styles) + text + tag_div(open=False)


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
