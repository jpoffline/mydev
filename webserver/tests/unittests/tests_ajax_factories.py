# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test


import app.lib.ajax.ajaxfactories as ajaxfactories


def test_ajax_placer_rows():
    id = 'ID'
    res = 'RES'
    meta = {'items': ['one', 'two']}
    actual = ""#ajax_placer_rows(id, res, meta)
    expected = ""
    return test.exe_test(actual, expected)

def test_howText_ajax_placer():
    res = 'RES'
    actual = ajaxfactories.ajax_placer(res)
    expected = """$('#RES').text(data.RES);"""
    return test.exe_test(actual, expected)


def test_Simple_ajax_placer_css():
    id = "div#divtochange"

    actual = ajaxfactories.ajax_placer_css(id)
    expected = """$('div#divtochange').css('background', data.rgb);"""
    return test.exe_test(actual, expected)
