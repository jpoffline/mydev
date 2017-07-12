""" Unit tests for htmltags """
# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
import unittest
from context import app
import app.lib.widgets.htmltags as htmltags


class TestHtmltags(unittest.TestCase):

    def test_tag_html(self):
        actual = htmltags.tag_html()
        expected = '<html>'
        self.assertEqual(actual, expected)

    def test_withmeta_tag(self):
        actual = htmltags.tag('html', meta='thing')
        expected = '<html thing>'
        self.assertEqual(actual, expected)

    def test_withoutmeta_tag(self):
        actual = htmltags.tag('html')
        expected = '<html>'
        self.assertEqual(actual, expected)

    def test_empty_tag_form(self):
        actual = htmltags.tag_form()
        expected = '<form action="" method="">'
        self.assertEqual(actual, expected)

    def test_full_tag_form(self):
        actual = htmltags.tag_form('METHOD', 'ACTION')
        expected = '<form action="ACTION" method="METHOD">'
        self.assertEqual(actual, expected)

    def test_close_tag_form(self):
        actual = htmltags.tag_form(open=False)
        expected = '</form>'
        self.assertEqual(actual, expected)

    def test_tag_h1(self):
        actual = htmltags.tag_h1()
        expected = '<h1>'
        self.assertEqual(actual, expected)

    def test_h2_tag_h_general(self):
        actual = htmltags.tag_h_general(2)
        expected = '<h2>'
        self.assertEqual(actual, expected)

    def test_h5_tag_h_general(self):
        actual = htmltags.tag_h_general(5)
        expected = '<h5>'
        self.assertEqual(actual, expected)

    def test_tag_div(self):
        actual = htmltags.tag_div()
        expected = '<div>'
        self.assertEqual(actual, expected)

    def test_close_tag_div(self):
        actual = htmltags.tag_div(open=False)
        expected = '</div>'
        self.assertEqual(actual, expected)

    def test_style_tag_div(self):
        actual = htmltags.tag_div(style={'thing': 'value'})
        expected = '<div style=\"thing: value;\">'
        self.assertEqual(actual, expected)

    def test_styleOnly_options_to_str(self):
        style = {
            'color': 'blue',
            'weight': 'bold'
        }
        actual = htmltags.options_to_str(style=style)
        expected = 'style=\"color: blue; weight: bold;\"'
        self.assertEqual(actual, expected)

    def test_optionsOnly_options_to_str(self):
        opts = {
            'id': '1',
            'name': 'jp'
        }
        actual = htmltags.options_to_str(options=opts)
        expected = 'id=\"1\" name=\"jp\"'
        self.assertEqual(actual, expected)

    def test_optionsAndStyle_options_to_str(self):
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
        self.assertEqual(actual, expected)

    def test_tag_input(self):
        actual = htmltags.tag_input('T', 'N')
        expected = '<input name=\"N\" type=\"T\">'
        self.assertEqual(actual, expected)

    def test_withOptions_tag_div(self):
        opts = {
            'id': '1',
            'name': 'jp'
        }
        actual = htmltags.tag_div(options=opts)
        expected = '<div id=\"1\" name=\"jp\">'
        self.assertEqual(actual, expected)

    def test_withOptionsAndStyle_tag_div(self):
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
        self.assertEqual(actual, expected)

    def test_with_value_tag_input(self):
        actual = htmltags.tag_input(
            'checkbox', 'ID', options={'value': 'THE_VALUE'})
        expected = '<input name="ID" type="checkbox" value="THE_VALUE">'
        self.assertEqual(actual, expected)

    def test_openOnly_tag_style_options(self):
        expected = '<TAG_TYPE>'
        actual = htmltags.tag_style_options('TAG_TYPE')
        self.assertEqual(actual, expected)

    def test_closeOnly_tag_style_options(self):
        expected = '</TAG_TYPE>'
        actual = htmltags.tag_style_options('TAG_TYPE', open=False)
        self.assertEqual(actual, expected)

    def test_optionsOnly_tag_style_options(self):
        expected = '<TAG_TYPE id="1" name="jp">'
        opts = {
            'id': '1',
            'name': 'jp'
        }
        actual = htmltags.tag_style_options('TAG_TYPE', options=opts)
        self.assertEqual(actual, expected)

    def test_styleOnly_tag_style_options(self):
        expected = '<TAG_TYPE style="color: blue; weight: bold;">'
        style = {
            'color': 'blue',
            'weight': 'bold'
        }
        actual = htmltags.tag_style_options('TAG_TYPE', style=style)
        self.assertEqual(actual, expected)

    def test_styleAndOpts_tag_style_options(self):
        expected = '<TAG_TYPE style="color: blue; weight: bold;" id="1" name="jp">'
        style = {
            'color': 'blue',
            'weight': 'bold'
        }
        opts = {
            'id': '1',
            'name': 'jp'
        }
        actual = htmltags.tag_style_options(
            'TAG_TYPE', style=style, options=opts)
        self.assertEqual(actual, expected)

    def test_TextAndStyleAndOpts_tag_style_options(self):
        expected = '<TAG_TYPE style="color: blue; weight: bold;" id="1" name="jp">TEXT</TAG_TYPE>'
        style = {
            'color': 'blue',
            'weight': 'bold'
        }
        opts = {
            'id': '1',
            'name': 'jp'
        }
        actual = htmltags.tag_style_options(
            'TAG_TYPE', style=style, options=opts, text='TEXT')
        self.assertEqual(actual, expected)
