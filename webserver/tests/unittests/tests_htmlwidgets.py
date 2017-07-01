# pylint: disable=C0111
# pylint: disable=C0103

from htmlwidgets import *
import tests.test_framework as test


def test_html():
    actual = html('test')
    expected = '<html><head><title>Blank</title></head>test</html>'
    return test.exe_test(actual, expected)


def test_withTitle_html():
    actual = html('test', title='my title')
    expected = '<html><head><title>my title</title></head>test</html>'
    return test.exe_test(actual, expected)


def test_withCSS_html():
    css = {
        'body': {
            'background-color': 'lightblue'
        }
    }
    actual = html('test', css=css)
    expected = '<html><head><title>Blank</title>'\
    + '<style>body {background-color: lightblue;} </style></head>test</html>'
    return test.exe_test(actual, expected)


def test_withTitleAndCSS_html():
    css = {
        'body': {
            'background-color': 'lightblue'
        }
    }
    actual = html('test', css=css, title="TITLE")
    expected = '<html><head><title>TITLE</title><style>body {background-color: lightblue;} </style></head>test</html>'
    return test.exe_test(actual, expected)


def test_label():
    expected = '<label>text</label>'
    actual = label('text')
    return test.exe_test(actual, expected)


def test_noReplies_pagePut():
    reply = None

    expected = ''
    actual = pagePut('send', reply, '')
    return test.exe_test(actual, expected)


def test_wrongAnchor_pagePut():
    reply = [
        'send',
        {
            'key': 'your_name',
            'val': 'jonny'
        },
        {
            'key': 'your_age',
            'val': '29'
        }
    ]

    expected = ''
    actual = pagePut('send2', reply, '')
    return test.exe_test(actual, expected)


def test_pagePut():
    reply = [
        '/send',
        {
            'key': 'your_name',
            'val': 'jonny'
        },
        {
            'key': 'your_age',
            'val': '29'
        }
    ]

    expected = '<div>Your name: jonny, Your age: 29</div>'
    actual = pagePut(
        'send', reply, '<div>Your name: ?your_name, Your age: ?your_age</div>')
    return test.exe_test(actual, expected)


def test_plain_div():
    expected = "<div>TEXT</div>"
    actual = div("TEXT")
    return test.exe_test(actual, expected)


def test_style_div():
    expected = "<div style=\"color: blue;\">TEXT</div>"
    actual = div("TEXT", style={'color': 'blue'})
    return test.exe_test(actual, expected)


def test_stylesList_div():
    expected = "<div style=\"color: blue; weight: bold;\">TEXT</div>"
    actual = div("TEXT", style={'color': 'blue', 'weight': 'bold'})
    return test.exe_test(actual, expected)


def test_title():
    expected = '<title>TEXT</title>'
    actual = title("TEXT")
    return test.exe_test(actual, expected)


def test_head():
    expected = '<head><title>TEXT</title></head>'
    actual = head("TEXT")
    return test.exe_test(actual, expected)


def test_None_style():
    expected = ''
    actual = style(None)
    return test.exe_test(actual, expected)


def test_withCss_style():
    expected = '<style>body {background-color: lightblue;} </style>'
    css = {
        'body': {
            'background-color': 'lightblue'
        }
    }
    actual = style(css)
    return test.exe_test(actual, expected)

def test_withOptions_div():
    opts = {
        'id': '1',
        'name': 'jp'
    }
    expected = '<div id="1" name="jp">TEXT</div>'
    actual = div("TEXT", options=opts)
    return test.exe_test(actual, expected)


def test_withOptionsAndStyle_div():
    opts = {
        'id': '1',
        'name': 'jp'
    }
    sty = {
        'color': 'blue',
        'weight': 'bold'
    }
    expected = '<div style="color: blue; weight: bold;" id="1" name="jp">TEXT</div>'
    actual = div("TEXT", options=opts, style=sty)
    return test.exe_test(actual, expected)

def test_input_submit():
    expected = '<label>TEXT</label><input name="ID" type="text"><input name="send" type="submit" value="BTN TEXT">'
    actual = input_submit("TEXT", "ID", add_button='BTN TEXT')
    return test.exe_test(actual, expected)


def test_checkbox_group():
    expected = '<form action="/send_buttons_12?btn1&btn2" method="POST">'\
    + '<input name="btn1" type="checkbox" value="val1"> CHK 1<br />'\
    + '<input name="btn2" type="checkbox" value="val2"> CHK 2<br />'\
    + '<input name="send" type="submit" value="YO">'\
    + '</form>'
    meta = {
        'form_id': 'send_buttons_12',
        'button_label' : 'YO',
        'inputs' : [
            {
                'id' : 'btn1',
                'value' : 'val1',
                'text' : 'CHK 1'
            },
            {
                'id' : 'btn2',
                'value' : 'val2',
                'text' : 'CHK 2'
            }
        ]
    }
    actual = checkbox_group(meta)
    return test.exe_test(actual, expected)