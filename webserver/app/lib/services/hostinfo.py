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


def get_datetime():
    """ Get the current datetime stamp in YYYYMMDDHHMMSS-form """
    today = datetime.datetime.today()
    return today.strftime('%Y%m%d%H%M%S')