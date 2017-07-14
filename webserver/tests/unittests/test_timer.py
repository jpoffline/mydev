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
        self.assertEqual(timer.elapsed_seconds(), 3)
        self.assertEqual(timer.elapsed(), '3.0 secs')

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



class TestLapTimer(unittest.TestCase):

    def setUp(self):
        self.time = mock_time()

    def test_simpleLap(self):
        timer = Timer(self.time)
        timer.start()
        timer._time.cycle(2)
        timer.end()
        timer.save('first lap')

        expected_lap_data = [{'id': 'first lap', 'elapsed': 3.0}]

        self.assertEqual(timer.elapsed_seconds(), 3.0)
        self.assertEqual(timer.laps(sort=False), expected_lap_data)
        timer.sort_laps()
        self.assertEqual(timer.slowest(last_n=1), [{'id': 'first lap', 'elapsed': 3.0}])

    def test_two_laps(self):
        timer = Timer(self.time)
        timer.start()
        timer._time.cycle(2)
        timer.end()
        timer.save('first lap')
        self.assertEqual(timer.elapsed_seconds(), 3.0)
        timer.start()
        timer._time.cycle(3)
        timer.end()
        timer.save('second lap')

        expected_lap_data = [
            {'id': 'first lap', 'elapsed': 3.0},
            {'id': 'second lap', 'elapsed': 4.0}]

        self.assertEqual(timer.elapsed_seconds(), 4.0)
        self.assertEqual(timer.laps(sort=False), expected_lap_data)

    def test_two_sorted_laps(self):
        timer = Timer(self.time)

        timer.start()
        timer._time.cycle(5)
        timer.end()
        timer.save('first lap')
        self.assertEqual(timer.elapsed_seconds(), 6.0)

        timer.start()
        timer._time.cycle(3)
        timer.end()
        timer.save('second lap')
        self.assertEqual(timer.elapsed_seconds(), 4.0)

        expected_lap_data = [
            {'id': 'second lap', 'elapsed': 4.0},
            {'id': 'first lap', 'elapsed': 6.0}]

        
        self.assertEqual(timer.laps(sort=True), expected_lap_data)


    def test_twoLaps_getSlowest_laps(self):
        timer = Timer(self.time)

        timer.start()
        timer._time.cycle(5)
        timer.end()
        timer.save('first lap')
        self.assertEqual(timer.elapsed_seconds(), 6.0)

        timer.start()
        timer._time.cycle(3)
        timer.end()
        timer.save('second lap')
        self.assertEqual(timer.elapsed_seconds(), 4.0)
        
        expected_lap_data = [
            {'id': 'second lap', 'elapsed': 4.0},
            {'id': 'first lap', 'elapsed': 6.0}]

        
        self.assertEqual(timer.laps(sort=True), expected_lap_data)
        self.assertEqual(timer.slowest(last_n=1), [{'id': 'first lap', 'elapsed': 6.0}])
        
