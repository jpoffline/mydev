""" HTML tags module """
import context
import lib.tools as tools


def tag(item, open=True, meta=''):
    """ Generate a general HTML tag """
    # HAS_UNIT_TESTS
    the_tag = '<'
    if open:
        the_tag += item
        if len(meta) > 0:
            the_tag += ' ' + meta
        return the_tag + '>'
    else:
        the_tag += '/' + item
    return the_tag + '>'


def tag_style_options(type, open=True, style=None, options=None):
    """ Generate a div tag """
    # Check for the unstyled case
    if style is None and options is None:
        return tag(type, open)
    meta = options_to_str(style=style, options=options)
    return tag(type, meta=meta)


def tag_table(options=None, style=None, open=True):
    """ Generate a general HTML-table-tag """
    return tag_style_options('table', options=options, style=style, open=open)


def tag_style(open=True):
    """ Generate a general HTML-style-tag """
    return tag('style', open)


def tag_html(open=True):
    """ Generate a general HTML-html-tag """
    return tag('html', open)


def tag_head(open=True):
    """ Generate a general HTML-head-tag """
    return tag('head', open)


def tag_title(open=True):
    """ Generate a general HTML-title-tag """
    return tag('title', open)


def tag_body(open=True):
    """ Generate a general HTML-body-tag """
    return tag('body', open)


def tag_h_general(which, open=True):
    """ Generate a general HTML-h-tag """
    # HAS_UNIT_TESTS
    return tag("h" + str(which), open)


def tag_h1(open=True):
    """ Generate a HTML-h1-tag """
    # HAS_UNIT_TESTS
    return tag_h_general(1, open)


def tag_img(src, open=True):
    """ Generate a HTML-img-tag """
    src = 'src = \"' + src + '\"'
    return tag('img', open, src)


def tag_form(method='', action='', open=True):
    """ Generate and return a HTML-form tag """
    # HAS_UNIT_TESTS
    if open:
        return tag('form ' + tools.collapse_dict({'method': method, 'action': action}))
    else:
        return tag('form', open)


def tag_label(open=True):
    """ Generate a HTML-label-tag """
    return tag('label', open)


def tag_input(in_type, name, place_holder=None, options=None):
    """ Generate a HTML-input-tag """
    # HAS_UNIT_TESTS
    opts_dict = {'type': in_type, 'name': name}
    if place_holder is not None:
        opts_dict.update({'placeholder': place_holder})
    if options is not None:
        opts_dict.update(options)
    return tag('input ' + tools.collapse_dict(opts_dict))


def tag_div(open=True, style=None, options=None):
    """ Generate a div tag """
    # HAS_UNIT_TESTS
    return tag_style_options('div', style=style, options=options, open=open)


def options_to_str(options=None, style=None):
    """ options and style to string """
    # HAS_UNIT_TESTS

    string = ''
    if style is not None:
        bit = tools.collapse_dict_css(style) + ';'
        string += 'style=\"' + bit + '\"'
    if options is not None:
        if style is not None:
            string += ' '
        string += tools.collapse_dict(options)
    return string
