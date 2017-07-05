# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test


import app.lib.ajax.ajaxfactories as ajaxfactories


def test_howText_ajax_placer():
    res = 'RES'
    actual = ajaxfactories.ajax_placer(res)
    expected = """$('#RES').text(data.RES);"""
    return test.exe_test(actual, expected)


def test_howHTML_ajax_placer():
    res = 'RES'
    actual = ajaxfactories.ajax_placer(res, options={'how': 'html'})
    expected = """$('#RES').html(data.RES);"""
    return test.exe_test(actual, expected)


def test_Simple_ajax_placer_css():
    id = "div#divtochange"

    actual = ajaxfactories.ajax_placer_css(id)
    expected = """$('div#divtochange').css('background', data.rgb);"""
    return test.exe_test(actual, expected)


def test_ajax_placer_general():
    id = "ID"
    method = "METHOD"
    item = "ITEM"
    actual = ajaxfactories.ajax_placer_general(id, method, item)
    expected = "$('ID').METHOD(ITEM);"
    return test.exe_test(actual, expected)


def test_placer_id():
    id = "ID"
    actual = ajaxfactories.placer_id(id)
    expected = "$('ID')."
    return test.exe_test(actual, expected)


def test_placer_item():
    id = "ITEM"
    actual = ajaxfactories.placer_item(id)
    expected = "(ITEM);"
    return test.exe_test(actual, expected)