""" my app code """
from context import app
from app.lib.htmlwidgets import *
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


def form_meta(get_id=False):
    options = {
        'form_id': 'send_name_and_age',
        'inputs': [
            {
                'id': 'your_name',
                'label': 'Insert your name:',
                'placeholder': 'your name...'
            },
            {
                'id': 'your_age',
                'label': 'Insert your age',
                'placeholder': 'your age...',
                'type': 'number',
                'button': 'Submit my data; yo'
            }
        ]
    }
    if get_id:
        return options['form_id']
    return options

def chkbx_meta():
    return{
        'form_id': 'send_buttons_12',
        'button_label' : 'YO',
        'inputs' : [
            {
                'id' : 'btn1',
                'value' : 'val1',
                'text' : 'CHK 1'
            },
            {
                'id' : 'btn2',
                'value' : 'val2',
                'text' : 'CHK 2'
            }
        ]
    }


def page_form(reply=None):
    """ Form page """
    return html(
        body(
            h1("my form")
            + div(
                input_submit_form(form_meta())
                + checkbox_group(chkbx_meta())
                + pagePut('send_name_and_age', reply,
                          div(
                              '<b>Name</b>: ?your_name<br /><b>Age</b>: ?your_age',
                              options={'id': 'response'}
                          ))
                + pagePut('send_buttons_12', reply,
                          div(
                              '<b>YO</b>: ?btn1<br /><b>WORD</b>: ?btn2',
                              options={'id': 'response'}
                          )),
                options={'id': 'half_width'})
        ),
        title='My page',
        css=get_simple_css()
    )


def page_index():
    """ Generate an index page """
    return page_form()
