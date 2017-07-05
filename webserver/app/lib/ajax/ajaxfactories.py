""" ajax factories """
import context
import lib.tools as tools


def ajax_placer_rows(id, res, rows_meta):
    """ AJAX-factory: place new items in rows of a table """
    string = []
    for item in rows_meta['items']:
        string.append("""'<td>' + ii.""" + item + """.toString() + '</td>'""")

    joined = ' + '.join(string)
    return """$.each(data.""" + res + """,function(index,ii){
          $('""" + id + """').append('<tr>' + """ + joined + """ + '</tr>');
        }); """


def ajax_placer_css(input_id):
    """ AJAX-factory: change css of an item """
    # HAS_TESTS
    string = placer_id(input_id) + """css('background', data.rgb);"""
    return string


def placer_id(input_id):
    """ AJAX-factory: id """
    # HAS_TESTS
    return """$('""" + input_id + """')."""


def placer_item(item):
    """ AJAX-factory: item """
    # HAS_TESTS
    return """(""" + item + """);"""


def ajax_placer_general(input_id, method, item):
    """ AJAX-factory: general placer """
    # HAS_TESTS
    return placer_id(input_id) + method + placer_item(item)


def ajax_placer(res, options=None):
    """ AJAX-factory: wrapper method """
    if options is None:
        input_id = '#' + res
        return ajax_placer_general(input_id, "text", "data." + res)
    elif options['how'] == 'html':
        input_id = '#' + res
        return ajax_placer_general(input_id, "html", "data." + res)
    elif options['how'] == 'rows':
        input_id = '#' + res
        return ajax_placer_rows(input_id, res, options['rows_meta'])
    elif options['how'] == 'css-background':
        return ajax_placer_css(res)

