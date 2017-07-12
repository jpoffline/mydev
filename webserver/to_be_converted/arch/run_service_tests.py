""" service test driver """

import sys
import test_framework as test


if __name__ == '__main__':
    test.run_tests(sys.argv[1:], 'service')
