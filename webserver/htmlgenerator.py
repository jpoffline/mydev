""" html generator """

import serverhelp as srv
from htmlwidgets import html, body, h1
from app.app import page_form

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

