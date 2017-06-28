from htmlwidgets import *
import test_framework as test


def test_html():
    actual = html('test')
    expected = '<html>test</html>'
    return test.exe_test(actual, expected)


def test_input_submit_form():

    id = 'send'
    labels = ['label_1', 'label_2']
    vars = ['var1', 'var2']
    expected = '<form action="/send?var1&var2" method="POST">'\
        + '<label>label_1</label><input type="text" name="var1">'\
        + '<input type="submit" name="Send">'\
        + '<label>label_2</label>'\
        + '<input type="text" name="var2">'\
        + '<input type="submit" name="Send"></form>'
    actual = input_submit_form(id, labels, vars)
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
    actual = div("TEXT", style={'color':'blue', 'weight':'bold'})
    return test.exe_test(actual, expected)
