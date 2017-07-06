""" Unit tests for htmltags """
# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test


import app.lib.htmltags as htmltags



def test_tag_html():
    actual = htmltags.tag_html()
    expected = '<html>'
    return test.exe_test(actual, expected)


def test_withmeta_tag():
    actual = htmltags.tag('html', meta='thing')
    expected = '<html thing>'
    return test.exe_test(actual, expected)


def test_withoutmeta_tag():
    actual = htmltags.tag('html')
    expected = '<html>'
    return test.exe_test(actual, expected)


def test_empty_tag_form():
    actual = htmltags.tag_form()
    expected = '<form action="" method="">'
    return test.exe_test(actual, expected)


def test_full_tag_form():
    actual = htmltags.tag_form('METHOD', 'ACTION')
    expected = '<form action="ACTION" method="METHOD">'
    return test.exe_test(actual, expected)


def test_close_tag_form():
    actual = htmltags.tag_form(open=False)
    expected = '</form>'
    return test.exe_test(actual, expected)


def test_tag_h1():
    actual = htmltags.tag_h1()
    expected = '<h1>'
    return test.exe_test(actual, expected)


def test_h2_tag_h_general():
    actual = htmltags.tag_h_general(2)
    expected = '<h2>'
    return test.exe_test(actual, expected)


def test_h5_tag_h_general():
    actual = htmltags.tag_h_general(5)
    expected = '<h5>'
    return test.exe_test(actual, expected)


def test_tag_div():
    actual = htmltags.tag_div()
    expected = '<div>'
    return test.exe_test(actual, expected)


def test_close_tag_div():
    actual = htmltags.tag_div(open=False)
    expected = '</div>'
    return test.exe_test(actual, expected)


def test_style_tag_div():
    actual = htmltags.tag_div(style={'thing': 'value'})
    expected = '<div style=\"thing: value;\">'
    return test.exe_test(actual, expected)


def test_styleOnly_options_to_str():
    style = {
        'color': 'blue',
        'weight': 'bold'
    }
    actual = htmltags.options_to_str(style=style)
    expected = 'style=\"color: blue; weight: bold;\"'
    return test.exe_test(actual, expected)


def test_optionsOnly_options_to_str():
    opts = {
        'id': '1',
        'name': 'jp'
    }
    actual = htmltags.options_to_str(options=opts)
    expected = 'id=\"1\" name=\"jp\"'
    return test.exe_test(actual, expected)


def test_optionsAndStyle_options_to_str():
    style = {
        'color': 'blue',
        'weight': 'bold'
    }
    opts = {
        'id': '1',
        'name': 'jp'
    }
    actual = htmltags.options_to_str(style=style, options=opts)
    expected = 'style=\"color: blue; weight: bold;\" id=\"1\" name=\"jp\"'
    return test.exe_test(actual, expected)


def test_tag_input():
    actual = htmltags.tag_input('T', 'N')
    expected = '<input name=\"N\" type=\"T\">'
    return test.exe_test(actual, expected)

def test_withOptions_tag_div():
    opts = {
        'id': '1',
        'name': 'jp'
    }
    actual = htmltags.tag_div(options=opts)
    expected = '<div id=\"1\" name=\"jp\">'
    return test.exe_test(actual, expected)

def test_withOptionsAndStyle_tag_div():
    opts = {
        'id': '1',
        'name': 'jp'
    }
    style = {
        'color': 'blue',
        'weight': 'bold'
    }
    actual = htmltags.tag_div(options=opts, style=style)
    expected = '<div style="color: blue; weight: bold;" id=\"1\" name=\"jp\">'
    return test.exe_test(actual, expected)

def test_with_value_tag_input():
    actual = htmltags.tag_input('checkbox', 'ID', options={'value': 'THE_VALUE'})
    expected = '<input name="ID" type="checkbox" value="THE_VALUE">'
    return test.exe_test(actual, expected)


def test_openOnly_tag_style_options():
    expected = '<TAG_TYPE>'
    actual = htmltags.tag_style_options('TAG_TYPE')
    return test.exe_test(actual, expected)

def test_closeOnly_tag_style_options():
    expected = '</TAG_TYPE>'
    actual = htmltags.tag_style_options('TAG_TYPE', open=False)
    return test.exe_test(actual, expected)


def test_optionsOnly_tag_style_options():
    expected = '<TAG_TYPE id="1" name="jp">'
    opts = {
        'id': '1',
        'name': 'jp'
    }
    actual = htmltags.tag_style_options('TAG_TYPE', options=opts)
    return test.exe_test(actual, expected)


def test_styleOnly_tag_style_options():
    expected = '<TAG_TYPE style="color: blue; weight: bold;">'
    style = {
        'color': 'blue',
        'weight': 'bold'
    }
    actual = htmltags.tag_style_options('TAG_TYPE', style=style)
    return test.exe_test(actual, expected)


def test_styleAndOpts_tag_style_options():
    expected = '<TAG_TYPE style="color: blue; weight: bold;" id="1" name="jp">'
    style = {
        'color': 'blue',
        'weight': 'bold'
    }
    opts = {
        'id': '1',
        'name': 'jp'
    }
    actual = htmltags.tag_style_options('TAG_TYPE', style=style, options=opts)
    return test.exe_test(actual, expected)

def test_TextAndStyleAndOpts_tag_style_options():
    expected = '<TAG_TYPE style="color: blue; weight: bold;" id="1" name="jp">TEXT</TAG_TYPE>'
    style = {
        'color': 'blue',
        'weight': 'bold'
    }
    opts = {
        'id': '1',
        'name': 'jp'
    }
    actual = htmltags.tag_style_options('TAG_TYPE', style=style, options=opts, text='TEXT')
    return test.exe_test(actual, expected)
