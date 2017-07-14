""" Module containing unit tests for the general return module """
# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app

import app.lib.tools.generalreturn as gr

import unittest


class TestGeneralReturn(unittest.TestCase):

    def test_init(self):
        ret = gr.gret()
        self.assertEqual(ret.state(), True)
        self.assertEqual(ret.message(), None)
        self.assertEqual(ret._serialise(), '<generalreturn\\ message:None success:True>')

    def test_equal_compare(self):
        gr1 = gr.gret()
        gr2 = gr.gret()
        self.assertEqual(gr1, gr2)

    def test_unequal_compare(self):
        gr1 = gr.gret()
        gr2 = gr.gret('MSG')
        self.assertNotEqual(gr1, gr2)
        self.assertEqual(gr1._serialise(), '<generalreturn\\ message:None success:True>')
        self.assertEqual(gr2._serialise(), '<generalreturn\\ message:MSG success:False>')


    def test_unequal_diff_msgs_compare(self):
        gr1 = gr.gret('MSG2')
        gr2 = gr.gret('MSG')
        self.assertNotEqual(gr1, gr2)
        self.assertEqual(gr1._serialise(), '<generalreturn\\ message:MSG2 success:False>')
        self.assertEqual(gr2._serialise(), '<generalreturn\\ message:MSG success:False>')
