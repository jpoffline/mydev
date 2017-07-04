from lib.ajax.ajaxfactories import *
import tests.test_framework as test

def test_ajax_placer_rows():
    id = 'ID'
    res = 'RES'
    meta = {'items': ['one', 'two']}
    actual = ajax_placer_rows(id, res, meta)
    expected = ""
    return test.exe_test(actual, expected)

def test_howText_ajax_placer():
    res = 'RES'
    actual = ajax_placer(res)
    expected = """$('#RES').text(data.RES);"""
    return test.exe_test(actual, expected)