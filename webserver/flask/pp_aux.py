def page_head():
    return """
<!doctype html>
<title>jQuery Example</title>
<script type="text/javascript"
  src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<script type="text/javascript">
  var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
</script>
"""


def span(id, text):
    return '<span id=\"' + id + '\">' + text + '</span>'


def input(name, type="text", size="5"):
    return '<input type=\"' + type + '\" size=\"' + size + '\" name=\"' + name + '\">'


def numeric_boxes(names):
    return input(names[0]) + ' + ' + input(names[1])


def serialize_ajax_inputs_base(name):
    return name + ": $('input[name=\"" + name + "\"]').val()"


def serialize_ajax_inputs(names):
    base = []
    for name in names:
        base.append(serialize_ajax_inputs_base(name))
    return ", ".join(base)


def link(href, id, text):
    return "<a href=" + href + " id=\"" + id + "\">" + text + "</a>"


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


def get_ajax(meta):

    route = meta['route']
    id_action = meta['id_action']

    id_data = meta['id_data']

    if not route.startswith('/'):
        route = '/' + route

    return """
<script type="text/javascript">
  $(function() {
    var submit_form = function(e) {
      $.getJSON('""" + route + """', {
        """ + serialize_ajax_inputs(id_data) + """
      }, function(data) {
        """ + \
        ajax_placer(meta['id_result']) + \
        ajax_placer(meta['id_result_uses']) + \
        ajax_placer(meta['id_result_hist'], how='rows', rows_meta={'items': id_data}) + """
      });
      return false;
    };
    $('""" + id_action + """').bind('click', submit_form);
  });
</script>
"""
