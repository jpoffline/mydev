# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test

import app.lib.widgets.htmlwidgets as htmlwidgets


def test_html():
    actual = htmlwidgets.html('test')
    expected = '<html><head><title>Blank</title></head>test</html>'
    return test.exe_test(actual, expected)


def test_withTitle_html():
    actual = htmlwidgets.html('test', title='my title')
    expected = '<html><head><title>my title</title></head>test</html>'
    return test.exe_test(actual, expected)


def test_linebreak():
    actual = htmlwidgets.linebreak()
    expected = '<br />'
    return test.exe_test(actual, expected)


def test_withCSS_html():
    css = {
        'body': {
            'background-color': 'lightblue'
        }
    }
    actual = htmlwidgets.html('test', css=css)
    expected = '<html><head><title>Blank</title>'\
        + '<style>body {background-color: lightblue;} </style></head>test</html>'
    return test.exe_test(actual, expected)


def test_withTitleAndCSS_html():
    css = {
        'body': {
            'background-color': 'lightblue'
        }
    }
    actual = htmlwidgets.html('test', css=css, title="TITLE")
    expected = '<html><head><title>TITLE</title><style>body {background-color: lightblue;} </style></head>test</html>'
    return test.exe_test(actual, expected)


def test_label():
    expected = '<label>text</label>'
    actual = htmlwidgets.label('text')
    return test.exe_test(actual, expected)


def test_noReplies_pagePut():
    reply = None

    expected = ''
    actual = htmlwidgets.pagePut('send', reply, '')
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
    actual = htmlwidgets.pagePut('send2', reply, '')
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
    actual = htmlwidgets.pagePut(
        'send', reply, '<div>Your name: ?your_name, Your age: ?your_age</div>')
    return test.exe_test(actual, expected)


def test_plain_div():
    expected = "<div>TEXT</div>"
    actual = htmlwidgets.div("TEXT")
    return test.exe_test(actual, expected)


def test_style_div():
    expected = "<div style=\"color: blue;\">TEXT</div>"
    actual = htmlwidgets.div("TEXT", style={'color': 'blue'})
    return test.exe_test(actual, expected)


def test_stylesList_div():
    expected = "<div style=\"color: blue; weight: bold;\">TEXT</div>"
    actual = htmlwidgets.div("TEXT", style={'color': 'blue', 'weight': 'bold'})
    return test.exe_test(actual, expected)


def test_title():
    expected = '<title>TEXT</title>'
    actual = htmlwidgets.title("TEXT")
    return test.exe_test(actual, expected)


def test_head():
    expected = '<head><title>TEXT</title></head>'
    actual = htmlwidgets.head("TEXT")
    return test.exe_test(actual, expected)


def test_None_style():
    expected = ''
    actual = htmlwidgets.style(None)
    return test.exe_test(actual, expected)


def test_withCss_style():
    expected = '<style>body {background-color: lightblue;} </style>'
    css = {
        'body': {
            'background-color': 'lightblue'
        }
    }
    actual = htmlwidgets.style(css)
    return test.exe_test(actual, expected)


def test_withOptions_div():
    opts = {
        'id': '1',
        'name': 'jp'
    }
    expected = '<div id="1" name="jp">TEXT</div>'
    actual = htmlwidgets.div("TEXT", options=opts)
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
    actual = htmlwidgets.div("TEXT", options=opts, style=sty)
    return test.exe_test(actual, expected)


def test_input_submit():
    expected = '<label>TEXT</label><input name="ID" type="text"><input name="send" type="submit" value="BTN TEXT">'
    actual = htmlwidgets.input_submit("TEXT", "ID", add_button='BTN TEXT')
    return test.exe_test(actual, expected)


def test_checkbox_group():
    expected = '<form action="/send_buttons_12?btn1&btn2" method="POST">'\
        + '<input name="btn1" type="checkbox" value="val1"> CHK 1<br />'\
        + '<input name="btn2" type="checkbox" value="val2"> CHK 2<br />'\
        + '<input name="send" type="submit" value="YO">'\
        + '</form>'
    meta = {
        'form_id': 'send_buttons_12',
        'button_label': 'YO',
        'inputs': [
            {
                'id': 'btn1',
                'value': 'val1',
                'text': 'CHK 1'
            },
            {
                'id': 'btn2',
                'value': 'val2',
                'text': 'CHK 2'
            }
        ]
    }
    actual = htmlwidgets.checkbox_group(meta)
    return test.exe_test(actual, expected)


def test_serialise_cols_to_row():
    cols = ['id', 'a']
    actual = htmlwidgets.serialise_cols_to_row(cols)
    expected = '<tr><td>id</td><td>a</td></tr>'
    return test.exe_test(actual, expected)


def test_customParent_serialise_cols_to_row():
    cols = ['id', 'a']
    actual = htmlwidgets.serialise_cols_to_row(cols, parent='TT')
    expected = '<TT><td>id</td><td>a</td></TT>'
    return test.exe_test(actual, expected)


def test_customItem_serialise_cols_to_row():
    cols = ['id', 'a']
    actual = htmlwidgets.serialise_cols_to_row(cols, item='th')
    expected = '<tr><th>id</th><th>a</th></tr>'
    return test.exe_test(actual, expected)


def test_customItemAndParent_serialise_cols_to_row():
    cols = ['id', 'a']
    actual = htmlwidgets.serialise_cols_to_row(cols, item='th', parent='TT')
    expected = '<TT><th>id</th><th>a</th></TT>'
    return test.exe_test(actual, expected)


def test_sql_to_html():
    cols = ['id', 'a']
    data = [(0, 0), (1, 1)]
    expected = '<table class="jp-table">' + \
        '<tr><th>id</th><th>a</th></tr>' + \
        '<tr><td>0</td><td>0</td></tr>' + \
        '<tr><td>1</td><td>1</td></tr>' + \
        '</table>'
    actual = htmlwidgets.sql_to_html(cols, data)
    return test.exe_test(actual, expected)


def test_unequalCols_sql_to_html():
    cols = ['id', 'a', 'b']
    data = [(0, 0), (1, 1)]
    expected = None
    actual = htmlwidgets.sql_to_html(cols, data)
    return test.exe_test(actual, expected)


def test_unequalData_sql_to_html():
    cols = ['id', 'a']
    data = [(0, 0, 1), (1, 1)]
    expected = None
    actual = htmlwidgets.sql_to_html(cols, data)
    return test.exe_test(actual, expected)


def test_span():
    expected = '<span id="ID">TEXT</span>'
    actual = htmlwidgets.span("ID", "TEXT")
    return test.exe_test(actual, expected)


def test_withStyle_span():
    expected = '<span style="color: blue;" id="ID">TEXT</span>'
    span_style = {
        'color': 'blue'
    }
    actual = htmlwidgets.span("ID", "TEXT", style=span_style)
    return test.exe_test(actual, expected)


def test_emptyID_span():
    expected = '<span>TEXT</span>'
    actual = htmlwidgets.span('', "TEXT")
    return test.exe_test(actual, expected)


def test_htmloutput():
    expected = '<span id="ID"></span>'
    actual = htmlwidgets.htmloutput("ID")
    return test.exe_test(actual, expected)