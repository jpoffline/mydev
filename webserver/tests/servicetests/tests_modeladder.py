# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test

import app.lib.model_adder as modeladder
import tests.mocks.mock_tools as tools_mock
import app.lib.sqlite.inmemorysqlite as ims


def service_inMemory_init():

    model = modeladder.ModelAdder(tools_mock.mockTools(),database=ims.inmemorydb())
    actual = ''
    expected = ''
    return test.exe_test(actual, expected)
