# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test

import app.lib.model_adder as modeladder
import tests.mocks.mock_tools as tools_mock



def service_inMemory_init():

    model = modeladder.ModelAdder(tools_mock.mockTools(),inmemory=True)
    actual = model.check_store_type()
    actual.update({'user' : model._user})
    expected = { 'user' : 'CURRENT_USERNAME', 'store': 'memory'}
    return test.exe_test(actual, expected)
