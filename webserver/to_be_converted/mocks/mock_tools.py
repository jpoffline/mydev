""" Mock version of the tools module

Useful for dependency injections.
"""

class mockTools(object):
    def __init__(self):
        pass
    def get_username(self):
        return 'CURRENT_USERNAME'
    def get_hostname(self):
        return 'CURRENT_HOSTNAME'
    def get_datetime(self):
        return 'YYYYMMDDHHMMSS'