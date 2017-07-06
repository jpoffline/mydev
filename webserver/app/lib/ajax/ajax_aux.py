""" Aux functions for pyflask implementation """
import context
import app.lib.widgets.htmltags as htmltags
import app.lib.ajax.ajaxfactories as ajaxtools
import app.lib.widgets.htmlwidgets as htmlwidgets
import app.lib.widgets.default_css as widgetcss



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


def get_ajax_index(meta):

    route = meta['route']
    id_action = meta['id_action']

    id_data = meta['id_data']

    if not route.startswith('/'):
        route = '/' + route

    new_css = {'how': 'css', 'new_css': {"background-color": "#FF0000"}}

    return """
<script type="text/javascript">
  $(function() {
    var submit_form = function(e) {
      $.getJSON('""" + route + """', {
        """ + serialize_ajax_inputs(id_data) + """
      }, function(data) {
        """ + \
        ajaxtools.ajax_placer('div#divtochange', options={'how': 'css-background'}) + \
        ajaxtools.ajax_placer(meta['id_result']) + \
        ajaxtools.ajax_placer(meta['id_calc_history_table'], options={'how': 'html'}) + \
        ajaxtools.ajax_placer(meta['id_result_uses']) + \
        ajaxtools.ajax_placer(meta['id_result_hist'], options={'how': 'rows', 'rows_meta': {'items': id_data}}) + """
      });
      return false;
    };
    $('""" + id_action + """').bind('click', submit_form);
  });
</script>
"""
