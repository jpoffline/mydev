# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
import unittest
from context import app
import app.lib.ajax.ajaxfactories as ajaxfactories


class TestAjaxFactories(unittest.TestCase):

    def test_howText_ajax_placer(self):
        res = 'RES'
        actual = ajaxfactories.ajax_placer(res)
        expected = """$('#RES').text(data.RES);"""
        self.assertEqual(actual, expected)

    def test_howrows_ajax_placer(self):
        res = 'RES'
        opts = {'how': 'rows', 'rows_meta': {'items': ['i1', 'i2']}}
        actual = ajaxfactories.ajax_placer(res, options=opts)
        expected = """$.each(data.RES,function(index,ii){$('#RES').""" + \
            """append('<tr>' + """ + \
            """'<td>' + ii.i1.toString() + '</td>' + """ + \
            """'<td>' + ii.i2.toString() + '</td>' + """ + \
            """'</tr>');});"""
        self.assertEqual(actual, expected)

    def test_howHTML_ajax_placer(self):
        res = 'RES'
        actual = ajaxfactories.ajax_placer(res, options={'how': 'html'})
        expected = """$('#RES').html(data.RES);"""
        self.assertEqual(actual, expected)

    def test_Simple_ajax_placer_css(self):
        id = "div#divtochange"

        actual = ajaxfactories.ajax_placer_css(id)
        expected = """$('div#divtochange').css('background', data.rgb);"""
        self.assertEqual(actual, expected)

    def test_ajax_placer_general(self):
        id = "ID"
        method = "METHOD"
        item = "ITEM"
        actual = ajaxfactories.ajax_placer_general(id, method, item)
        expected = "$('ID').METHOD(ITEM);"
        self.assertEqual(actual, expected)

    def test_placer_id(self):
        id = "ID"
        actual = ajaxfactories.placer_id(id)
        expected = "$('ID')."
        self.assertEqual(actual, expected)

    def test_placer_item(self):
        id = "ITEM"
        actual = ajaxfactories.placer_item(id)
        expected = "(ITEM);"
        self.assertEqual(actual, expected)
