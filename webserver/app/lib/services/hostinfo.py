""" General host info services """
import time
import datetime


def get_username():
    """ Get the current user name """
    import getpass
    return getpass.getuser()


def get_hostname():
    """ Get the current host machine name """
    import socket
    return socket.gethostname()


def get_datetime(pretty=False):
    """ Get the current datetime stamp in YYYYMMDDHHMMSS-form """
    today = datetime.datetime.today()
    if pretty is False:
        chosen_format = '%Y%m%d%H%M%S'
    else:
        chosen_format = '%d/%m/%Y %H:%M:%S'
    return today.strftime(chosen_format)
