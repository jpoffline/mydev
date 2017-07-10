# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app
import test_framework as test

import app.lib.model_adder as modeladder


class toolsMock(object):
    def __init__(self):
        pass
    def get_username(self):
        return 'JONNY'
    def get_hostname(self):
        return 'MKBK'
    def get_datetime(self):
        return 'NOW'

def service_inMemory_init():

    model = modeladder.ModelAdder(toolsMock(),inmemory=True)
    actual = model.check_store_type()
    actual.update({'user' : model._user})
    expected = { 'user' : 'JONNY', 'store': 'memory'}
    return test.exe_test(actual, expected)


def service_insertInMemory():

    

    model = modeladder.ModelAdder(toolsMock(),inmemory=True)
    model.add_history_item(1,2)
    actual = model.get_all_history(returnit=True)
    expected = ''
    return test.exe_test(actual, expected)
