""" ajax factories """
from tools import *


def ajax_placer_rows(id, res, rows_meta):
    """ AJAX-factory: place new items in rows of a table """
    string = []
    for item in rows_meta['items']:
        string.append("""'<td>' + ii.""" + item + """.toString() + '</td>'""")

    joined = ' + '.join(string)
    return """$.each(data.""" + res + """,function(index,ii){
          $('""" + id + """').append('<tr>' + """ + joined + """ + '</tr>');
        }); """


def ajax_placer_css(input_id, new_css):
    """ AJAX-factory: change css of an item """
    # HAS_TESTS
    css = collapse_css_ajax(new_css)
    string = """$(\"""" + input_id + """\").css({""" + css + """});"""
    return string


def ajax_placer(res, options=None):
    """ AJAX-factory: wrapper method """
    if options is None:
        input_id = '#' + res
        return """$('""" + input_id + """').text(data.""" + res + """);"""
    elif options['how'] == 'rows':
        input_id = '#' + res
        return ajax_placer_rows(input_id, res, options['rows_meta'])
    elif options['how'] == 'css':
        return ajax_placer_css(res, options['new_css'])

