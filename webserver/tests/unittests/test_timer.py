""" Module containing unit tests for the serverHelp module """
# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app


from tests.mocks.mock_time import *

from app.lib.tools.timer import Timer, pretty_time

import unittest


class TestTimer(unittest.TestCase):

    def setUp(self):
        self.time = mock_time()

    def test_timer_start(self):
        time = self.time
        actual = time.time()
        expected = 0
        self.assertEqual(actual, expected)

    def test_twice_timer_start(self):
        time = self.time
        time.cycle(2)
        actual = time.time()
        expected = 2
        self.assertEqual(actual, expected)

    def test_Timer_simple(self):
        timer = Timer(self.time)
        timer.start()
        timer._time.cycle(2)
        timer.end()
        actual = timer.elapsed_seconds()
        expected = 3
        self.assertEqual(actual, expected)

    def test_TimerMS_simple(self):
        timer = Timer(self.time)
        timer._time.set_increment(0.001)
        timer.start()
        timer._time.cycle(2)
        timer.end()
        actual = timer._time.time()
        expected = 0.004
        self.assertEqual(actual, expected)
