""" html generator """

import serverhelp as srv
from htmlwidgets import html, body, h1, img, input_submit_form, pagePut, div


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
            + img(".jpg")
        )
    )


def get_response_page(code):
    """ Get the response page for a given code """
    decon = srv.deconstruct_response_string(code)
    event_id = decon[0]
    return pick_response_page(event_id, decon)


def pick_response_page(eventid, replies):
    """ Pick a response page, based on the eventid """
    if eventid == '/send_name_and_age':
        return page_form(replies)
    elif eventid == 'TEST_ERROR':
        return page_error()
    return page_error()


def page_error():
    """ Return an error page """
    return html(
        body(
            h1(
                "PAGE NOT FOUND"
            )
        )
    )


def get_simple_css():
    """ Create an return a simple css object """
    return {
        'body': {
            'background-color': 'lightblue'
        },
        'div' :{
            'background-color': 'green'
        }
    }


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
                          style={'color': 'blue'}
                      ))
        ),
        title='My page',
        css=get_simple_css()
    )


def page_index():
    """ Generate an index page """
    return page_form()
