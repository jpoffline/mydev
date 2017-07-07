""" Unit test framework """
import inspect

def some_magic(mod):
    """ Collect together the test functions in the loaded modules """
    all_functions = inspect.getmembers(mod, inspect.isfunction)
    results = []
    for key, _ in all_functions:
        if key.startswith("test_"):

            var = eval(key + '()')  # pylint: disable=W0123

            results.append(var)
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


def exe_test(actual, expected):
    """ Execute a particular unit test """
    calling_function = inspect.stack()[1][3]

    if actual == expected:
        return throw_pass(calling_function)
    else:
        print '================================='
        print 'FAILED TEST : ' + calling_function
        print '  ACTUAL:'
        print actual
        print '  EXPECTED:'
        print expected
        print '================================='
        return throw_fail(calling_function, actual, expected)


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

