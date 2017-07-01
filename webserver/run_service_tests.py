

import inspect
import sys
from tests.servicetests.test_timer import *



from lib.timer import Timer
import time


def some_magic(mod):
    """ Collect together the test functions in the loaded modules """
    all_functions = inspect.getmembers(mod, inspect.isfunction)
    results = []
    for key, _ in all_functions:
        if key.startswith("test_"):

            var = eval(key + '()')  # pylint: disable=W0123

            results.append(var)
    return results


def run_service_tests():
    """ Run the unit tests """
    timer = Timer(time)
    print test.unit_tests_banner()
    timer.start()
    timer.sig(4)
    results = some_magic(sys.modules[__name__])
    timer.end()
    test.analyse_tests(results)
    print test.elapsed(timer.elapsed())
    print test.unit_tests_banner(True)


if __name__ == '__main__':
    run_service_tests()
