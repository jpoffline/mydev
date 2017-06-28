""" html generator """

import serverhelp as srv
from htmlwidgets import *


def hello_world_text():
    """ Return the hello, world text """
    return 'Hello, World!'


def hello_world():
    """ Return the hello-world page """
    return hello_person(' World!')


def hello_person(text):
    """ Return a hello-person page, with a picture of a cat """
    return html(
        body(
            h1('Hello, ' + text)
            + img("https://s-media-cache-ak0.pinimg.com/736x/60/9f/39/609f392284fd9e5d787ee190ca1bbc40--animal-quotes-animal-humor.jpg")
        )
    )


def get_response_page(code):
    decon = srv.deconstruct_response_string(code)
    event_id = decon[0]
    return pick_response_page(event_id, decon)


def pick_response_page(eventid, replies):
    if eventid == '/send_name_and_age':
        return page_form('jonathan', replies)
    elif eventid == 'TEST_ERROR':
        return page_error()
    return page_error()


def page_error():
    return html(
        body(
            h1(
                "PAGE NOT FOUND"
            )
        )
    )


def page_form(reply=None):
    """ Form page """
    return html(
        body(
            h1("my form")
            + input_submit_form(
                'send_name_and_age',
                ['Insert your name:', 'Insert your age:'],
                ['your_name', 'your_age']
            )
            + pagePut('send_name_and_age', reply,
                      div(
                          '<b>Name</b>: ?your_name<br /><b>Age</b>: ?your_age',
                          style='color:blue'
                      ))
        )
    )


def page_index():
    """ Generate an index page """
    return page_form()
