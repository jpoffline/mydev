""" Aux functions for pyflask implementation """

import htmltags as htmltags
import lib.ajax.ajaxfactories as ajaxtools
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




def numeric_boxes(names):
    options = {'size': '5'}
    bxs = []
    for name in names:
        bxs.append(htmltags.tag_input('text', name, options=options))
    numboxes = ' + '.join(bxs)
    return numboxes
    


def serialize_ajax_inputs_base(name):
    return name + ": $('input[name=\"" + name + "\"]').val()"


def serialize_ajax_inputs(names):
    base = []
    for name in names:
        base.append(serialize_ajax_inputs_base(name))
    return ", ".join(base)


def link(href, id, text):
    return "<a href=" + href + " id=\"" + id + "\">" + text + "</a>"




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
        ajaxtools.ajax_placer(meta['id_result']) + \
        ajaxtools.ajax_placer(meta['id_result_uses']) + \
        ajaxtools.ajax_placer(meta['id_result_hist'], how='rows', rows_meta={'items': id_data}) + """
      });
      return false;
    };
    $('""" + id_action + """').bind('click', submit_form);
  });
</script>
"""
