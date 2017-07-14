""" Module containing unit tests for the mock time module """
# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app


from tests.mocks.mock_time import *

from app.lib.tools.timer import Timer, pretty_time

import unittest


class TestPrettyPrint(unittest.TestCase):

    def test_seconds_prettyprint(self):
        self.assertEqual(pretty_time(1), '1.0 secs')

    def test_60seconds_prettyprint(self):
        self.assertEqual(pretty_time(60), '1.0 mins')

    def test_mins_prettyprint(self):
        self.assertEqual(pretty_time(120), '2.0 mins')
    
    def test_small_secs_prettyprint(self):
        self.assertEqual(pretty_time(0.001), '1.0 ms')

    def test_ms_prettyprint(self):
        self.assertEqual(pretty_time(0.0001), '0.1 ms')

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

    def test_Timersig(self):
        timer = Timer(self.time)
        timer.sig(2)
        self.assertEqual(timer._sig, 2)

    def test_elapsed(self):
        timer = Timer(self.time)
        timer.start()
        timer._time.cycle(2)
        timer.end()
        actual = timer.elapsed_seconds()
        self.assertEqual(actual, 3)
        self.assertEqual(timer.elapsed(), '3.0 secs')

    def test_minselapsed(self):
        timer = Timer(self.time)
        timer.start()
        timer._time.cycle(119)
        timer.end()
        actual = timer.elapsed_seconds()
        self.assertEqual(actual, 120)
        self.assertEqual(timer.elapsed(), '2.0 mins')



