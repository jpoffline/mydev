from context import app
from tests.mock_time import * 
import test_framework as test
from app.lib.tools.timer import Timer, pretty_time

def service_timer_start():
    time = mock_time()
    return test.exe_test(time.time(), 0)


def service_twice_timer_start():
    time = mock_time()
    time.cycle(2)
    return test.exe_test(time.time(), 2)

def service_Timer_simple():
    timer = Timer(mock_time())
    timer.start()
    timer._time.cycle(2)
    timer.end()
    return test.exe_test(timer.elapsed_seconds(), 3)

def service_TimerMS_simple():
    timer = Timer(mock_time())
    timer._time.set_increment(0.001)
    timer.start()
    timer._time.cycle(2)
    timer.end()
    return test.exe_test(timer._time.time(), 0.004)