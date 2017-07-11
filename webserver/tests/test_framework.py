""" General test framework """
import inspect
import context
from app.lib.tools.timer import Timer
import app.lib.tools as tools
import time
import sys

from services import *
from units import *


def run_tests(args, test_type):
    """ Interface method to run the tests.

    Test functions will be looked for which
    have the <test_type>_X prefix.

    Args
    ---
    args: List of options for the execution of this set of tests.
            -quiet : suppress screen info if pass

    test_type: The test type.

    """
    if '-quiet' in args:
        verbose = False
    else:
        verbose = True
    timer = Timer(time)
    if verbose:
        print unit_tests_banner(testtype=test_type)
    timer.start()
    timer.sig(4)
    results = execute_tests(verbose=verbose, prefix=test_type)
    timer.end()
    if analyse_tests(results, verbose=verbose) is False:
        print 'FAIL'

    if verbose:
        print elapsed(timer.elapsed())
        print unit_tests_banner(empty=True)


def execute_tests(verbose=True, prefix='test'):
    """ Collect together the test functions in the loaded modules """

    results = []
    all_functions = inspect.getmembers(sys.modules[__name__], inspect.isfunction)

    timer = Timer(time)
    timer.sig(5)
    for key, _ in all_functions:
        if key.startswith(prefix+"_"):
            timer.start()
            function_to_exe = key + '()'
            var = eval(function_to_exe)  # pylint: disable=W0123
            timer.end()
            timer.save(key, reset=True)
            results.append(var)
    timer.sort_laps()
    if verbose:
        timer.print_stats()
    return results


def if_any_fail(input_list):
    """ Helper function to detect if any unit tests failed """
    count_pass = 0
    count_fail = 0
    for item in input_list:
        if not item['result']:
            count_fail += 1
        else:
            count_pass += 1
    return {
        'pass': (count_fail == 0),
        'count_pass': count_pass,
        'count_fail': count_fail
    }


def general_test_result(name, result, actual, expected):
    """ Return a general unit test return """
    if result:
        return {
            'name': name,
            'result': result
        }
    else:
        return {
            'name': name,
            'result': result,
            'actual': actual,
            'expected': expected
        }


def throw_pass(name):
    """ Throw a unit test pass """
    return general_test_result(name, True, None, None)


def throw_fail(name, actual, expected):
    """ Throw a unit test fail """
    return general_test_result(name, False, actual, expected)


def exe_test(actual, expected, many=False):
    """ Execute a particular unit test """
    calling_function = inspect.stack()[1][3]

    if actual == expected:
        return throw_pass(calling_function)
    else:
        print '================================='
        print 'FAILED TEST : ' + calling_function
        if many:
            report_failed_many_comparison(actual, expected)
        else:
            report_simple_fail(actual, expected)
        print '================================='
        return throw_fail(calling_function, actual, expected)


def report_simple_fail(actual, expected):
    print '  ACTUAL:'
    print '    ', actual
    print '  EXPECTED'
    print '    ', expected


def report_failed_many_comparison(actual, expected):
    dict_diffs = tools.diff_dict(actual, expected)
    if dict_diffs['keys'] is False:
        print 'issue with keys'
    if dict_diffs['vals'] is False:
        print '* Issue with values'
        for diff in dict_diffs['val_diffs']:
            for key, v in diff.iteritems():
                print '*', key
                report_simple_fail(v[0], v[1])

def analyse_tests(results, verbose=True):
    """ Analyse the unit test results """
    
    print '* ran ' + str(len(results)) + ' tests'
    analysis = if_any_fail(results)
    if analysis['pass']:
        if verbose:
            print '* tests passed'
            return True
    else:
        print '* tests failed: ' + str(analysis['count_fail']) + '/' + str(analysis['count_pass'])
        return False

def unit_tests_banner(testtype='unit',empty=False):
    """ Return a banner for the start of the unit tests """
    if not empty:
        return '\n========== '+testtype +' tests =========='
    return '================================\n'

def elapsed(time):
    return '* elapsed: ' + time

