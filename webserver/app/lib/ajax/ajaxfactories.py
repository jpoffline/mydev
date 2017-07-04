""" ajax factories """


def ajax_placer_rows(id, res, rows_meta):
    string = []
    for item in rows_meta['items']:
        string.append("""'<td>' + ii.""" + item + """.toString() + '</td>'""")

    joined = ' + '.join(string)
    return """$.each(data.""" + res + """,function(index,ii){
          $('""" + id + """').append('<tr>' + """ + joined + """ + '</tr>');
        }); """


def ajax_placer(res, how='text', rows_meta=None):
    id = '#' + res
    if(how == 'text'):
        return """$('""" + id + """').text(data.""" + res + """);"""
    elif(how == 'rows'):
        return ajax_placer_rows(id, res, rows_meta)
