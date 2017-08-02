# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app



import app.lib.tools.tools as tools


import unittest

class TestTools(unittest.TestCase):

    def test_collapse_dict(self):
    
        input_dict = {
            'key': 'value',
            'key2': 'val'
        }
    
        actual = tools.collapse_dict(input_dict)
        expected = "key=\"value\" key2=\"val\""
        self.assertEqual(actual, expected)    
    
    def test_Emptycollapse_css(self):
        input_css = None
        actual = tools.collapse_css(input_css)
        expected = ''
        self.assertEqual(actual, expected)    
    
    def test_collapse_css_ajax(self):
        input_css = {
            'h1': {
                'color': 'blue',
                'weight': 'bold'
            },
            'p': {
                'color': 'red',
                'weight': 'italic'
            }
        }
        actual = tools.collapse_css_ajax(input_css)
        expected = '"h1": "{\'color\': \'blue\', \'weight\': \'bold\'}", ' + \
        '"p": "{\'color\': \'red\', \'weight\': \'italic\'}"'
        self.assertEqual(actual, expected)   



    def test_collapse_css(self):
        input_css = {
            'h1': {
                'color': 'blue',
                'weight': 'bold'
            },
            'p': {
                'color': 'red',
                'weight': 'italic'
            }
        }
        actual = tools.collapse_css(input_css)
        expected = "p {color: red; weight: italic;} h1 {color: blue; weight: bold;} "
        self.assertEqual(actual, expected)    
    
    def test_NoDiff_diff_dict(self):
        dict1 = {'one': 1, 'two': 2}
        dict2 = {'one': 1, 'two': 2}
        actual = tools.diff_dict(dict1, dict2)
        expected = {
            'keys': True,
            'vals': True
        }
        self.assertEqual(actual, expected)    
    
    def test_SimpleDiff_diff_dict(self):
        dict1 = {'one': 1, 'two': 2}
        dict2 = {'one': 1, 'two': 3}
        actual = tools.diff_dict(dict1, dict2)
        expected = {
            'keys': True,
            'vals': False,
            'val_diffs': [{'two': (2, 3)}]
        }
        self.assertEqual(actual, expected)    
    
    def test_ChangeOrder_diff_dict(self):
        dict1 = {'one': 1, 'two': 2}
        dict2 = {'two': 3, 'one': 1}
        actual = tools.diff_dict(dict1, dict2)
        expected = {
            'keys': True,
            'vals': False,
            'val_diffs': [{'two': (2, 3)}]
        }
        self.assertEqual(actual, expected)    
    
    def test_DiffKeys_diff_dict(self):
        dict1 = {'three': 1, 'two': 2}
        dict2 = {'two': 3, 'one': 1}
        actual = tools.diff_dict(dict1, dict2)
        expected = {
            'keys': False,
            'vals': False,
            'val_diffs': [{'two': (2, 3)}],
            'diff_keys': set(['three', 'one'])
        }
        self.assertEqual(actual, expected)    
    
    def test_WithListMatch_diff_dict(self):
        dict1 = {'one': 1, 'two': [1, 2]}
        dict2 = {'one': 1, 'two': [1, 2]}
        actual = tools.diff_dict(dict1, dict2)
        expected = {
            'keys': True,
            'vals': True
        }
        self.assertEqual(actual, expected)    
    
    def test_WithListNoMatch_diff_dict(self):
        dict1 = {'one': 1, 'two': [1, 2]}
        dict2 = {'one': 1, 'two': [1, 3]}
        actual = tools.diff_dict(dict1, dict2)
        expected = {
            'keys': True,
            'vals': False,
            'val_diffs': [{'two': ([1, 2], [1, 3])}]
        }
        self.assertEqual(actual, expected)    
    
    def test_WithListAndStringsNoMatch_diff_dict(self):
        dict1 = {'one': 1, 'two': [1, 2], 'three': 'hello'}
        dict2 = {'one': 1, 'two': [1, 3], 'three': 'World'}
        actual = tools.diff_dict(dict1, dict2)
        expected = {
            'keys': True,
            'vals': False,
            'val_diffs': [
                {'three': ('hello', 'World')},
                {'two': ([1, 2], [1, 3])}
            ]
        }
        self.assertEqual(actual, expected)

    def test_val_to_rgb(self):
        actual = tools.val_to_rgb(123)
        expected = 'rgb(123,127,127)'
        self.assertEqual(actual, expected)

    def test_NOChange_truncate_string(self):
        string = 'hello'
        actual = tools.truncate_string(string)
        expected = 'hello'
        self.assertEqual(actual, expected)

    def test_withChange_truncate_string(self):
        string = 'hello'
        actual = tools.truncate_string(string, mlen=2)
        expected = 'he...'
        self.assertEqual(actual, expected)

    def test_longerChange_truncate_string(self):
        string = 'hello'
        actual = tools.truncate_string(string, mlen=5)
        expected = 'hello'
        self.assertEqual(actual, expected)

    def test_append_gbp(self):
        input = 5
        expected = u"\xA3" + '5.00'
        self.assertEqual(tools.append_gbp(input), expected)

        input = None
        expected = u"\xA3" + '0.00'
        self.assertEqual(tools.append_gbp(input), expected)

        input = -5
        expected = "-" + u"\xA3" + '5.00'
        
        self.assertEqual(tools.append_gbp(input), expected)


    def test_to_pctg(self):
        self.assertEqual(tools.to_pctg(1,1),100)
        self.assertEqual(tools.to_pctg(1,0.5),200)
        self.assertEqual(tools.to_pctg(1,0),False)