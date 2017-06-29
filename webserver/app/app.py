""" my app code """

from htmlwidgets import html, body, h1, img, input_submit_form, pagePut, div
from css import get_simple_css


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


def page_form(reply=None):
    """ Form page """
    return html(
        body(
            h1("my form")
            + div(
                input_submit_form(
                    'send_name_and_age',
                    ['Insert your name:', 'Insert your age:'],
                    ['your_name', 'your_age']
                )
                + pagePut('send_name_and_age', reply,
                          div(
                              '<b>Name</b>: ?your_name<br /><b>Age</b>: ?your_age',
                              options={'id': 'response'}
                          )), options={'id': 'half_width'})),
        title='My page',
        css=get_simple_css()
    )


def page_index():
    """ Generate an index page """
    return page_form()
