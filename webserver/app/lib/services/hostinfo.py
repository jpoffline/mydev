""" General host info services """
import time
import datetime
import os


def get_username():
    """ Get the current user name """
    import getpass
    return getpass.getuser()


def get_hostname():
    """ Get the current host machine name """
    import socket
    return socket.gethostname()


def pretty_datetime_format():
    """ Get the datetime format
    string for a pretty looking date:
    YYY-MM-DD HH:MM:SS
    """
    return '%Y-%m-%d %H:%M:%S'

def compact_datetime_format():
    """ Get the datetime format
    string for a compact looking date:
    YYYYMMDDHHMMSS
    """
    return '%Y%m%d%H%M%S'

def get_datetime(pretty=False):
    """ Get the current datetime stamp in YYYYMMDDHHMMSS-form """
    today = datetime.datetime.today()
    if pretty is False:
        chosen_format = compact_datetime_format()
    else:
        chosen_format = pretty_datetime_format()
    return today.strftime(chosen_format)


def check_and_create_path(path):
    """ Check the existence of a path,
    and create if not exists """
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise


def is_string_a_datetime(date_text, fmt=pretty_datetime_format()):
    """ Check to see if a given
    string is of the date-time format
    that python recognises """
    try:
        if date_text != datetime.datetime.strptime(date_text, fmt).strftime(fmt):
            raise ValueError
        return True
    except ValueError:
        return False
