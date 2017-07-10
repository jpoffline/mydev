import context
import lib.widgets.htmlwidgets as htmlwidgets
import css as css
import lib.ajax.ajax_aux as ajax_aux

def page_head():
    return """
<!doctype html><html>""" + \
 htmlwidgets.head("jQuery Example", css=css.global_css()) + \
"""<script type="text/javascript"
  src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<script type="text/javascript">
  var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
</script>
"""

def index_ajax_meta():
    return {
        'route': '/_add_numbers',
        'id_action': 'a#calculate',
        'id_result': 'result',
        'id_data': ['a', 'b'],
        'id_result_hist': 'history',
        'id_result_uses': 'nuses',
        'id_rgb': 'rgb',
        'id_calc_history_table': 'histtbl'
    }

def index_page():
    meta = index_ajax_meta()
    return page_head() +\
        ajax_aux.get_ajax_index(meta) + \
        "<body>"+\
        htmlwidgets.h1("jQuery Example") + \
        ajax_aux.numeric_boxes(meta['id_data']) + " = " + \
        htmlwidgets.htmloutput(meta['id_result']) + \
        ajax_aux.link("#", "calculate", "DO IT") + \
        htmlwidgets.htmlvaluebox("N uses", meta['id_result_uses']) + \
        htmlwidgets.div('', options={'id':'divtochange'},style={'height': '50px', 'width': '50px', 'background-color':'blue'})+\
        htmlwidgets.h1("Session history") + \
        htmlwidgets.datatable(['a','b'],[],options={'id':meta['id_result_hist']})+\
        htmlwidgets.htmloutput(meta['id_calc_history_table']) + \
        "</body></html>"
