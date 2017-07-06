""" html generator """

import app.lib.serverhelp as srv
import app.lib.widgets.htmlwidgets as htmlwidgets
from app import app

def get_response_page(code):
    """ Get the response page for a given code """
    decon = srv.deconstruct_response_string(code)
    event_id = decon[0]
    return pick_response_page(event_id, decon)


def pick_response_page(eventid, replies):
    """ Pick a response page, based on the eventid """
    if eventid == 'TEST_ERROR':
        return page_error()
    return app.page_form(replies)


def page_error(eventid='404'):
    """ Return an error page """
    return htmlwidgets.html(
        htmlwidgets.body(
            htmlwidgets.h1(
                "PAGE NOT FOUND" + eventid
            )
        )
    )

