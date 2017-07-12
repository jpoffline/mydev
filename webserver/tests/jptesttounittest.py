import os
from glob import glob
files = [y for x in os.walk('unittests') for y in glob(os.path.join(x[0], 'tests_*.py'))]
test_fns = []
test_files = []
for file in files:
    orig_test_file_name = file.split('\\')[1][6:][:-3]
    test_files.append(orig_test_file_name)
    ff = orig_test_file_name.split('_')
    fff = [f.title() for f in ff]
    fff = ''.join(fff)
    test_fns.append(fff)
    print orig_test_file_name
    new_file = open('unittests/converts/test_' + orig_test_file_name + '.py', 'w')

    newContent = """import unittest\n\nclass Test""" + fff + """(unittest.TestCase):\n\n"""

    test_case = False
    with open(file) as f:
        for line in f:
            if line.startswith('def test'):
                if test_case is False:
                    new_file.write(newContent)
                test_case = True
                line = '    ' + line.replace('()', '(self)')
            elif line.startswith('    return test.'):
                line = '        self.assertEqual(actual, expected)'
            else:
                if test_case is not False:
                    line = '    ' + line
                else:
                    line = line
            new_file.write(line)
    new_file.close()
