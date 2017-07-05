# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
from lib.ajax_aux import *
import lib.tools as tools
import lib.htmlwidgets as htmlwidgets
import lib.model_adder as modeladder
app = Flask(__name__)


history = []
model = modeladder.ModelAdder()

@app.route('/_add_numbers')
def add_numbers():

    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    history.append({'a': a, 'b': b})

    #m._create_db()
    model.add_history_item(a, b)
    model.get_all_history()

    table_html = model.serialise_history()

    return jsonify(
        result=a + b,
        history=[{'a': a, 'b': b}],
        nuses=len(history),
        rgb=tools.val_to_rgb(a+b),
        histtbl=table_html
    )


@app.route('/')
def index():
    meta = {
        'route': '/_add_numbers',
        'id_action': 'a#calculate',
        'id_result': 'result',
        'id_data': ['a', 'b'],
        'id_result_hist': 'history',
        'id_result_uses': 'nuses',
        'id_rgb': 'rgb',
        'id_calc_history_table': 'histtbl'
    }

    return page_head() +\
        get_ajax(meta) + \
        "<h1>jQuery Example</h1><p>" + \
        numeric_boxes(meta['id_data']) + "=" + \
        htmlwidgets.span(meta['id_result'], "?") + "<p>" + \
        link("#", "calculate", "DO IT") + \
        "<h2>N uses: " + htmlwidgets.span(meta['id_result_uses'], "") + "</h2>" +\
        "<div id=\"divtochange\" style=\"height: 50px; width: 50px; background-color:blue;\"></div>" + \
        "<h2>Session history</h2>" + \
        "<table id=\"" + meta['id_result_hist'] + \
        "\"><tr><th>a</th><th>b</th></tr></table>" + \
        "<h2>All history</h2>" + \
        htmlwidgets.span(meta['id_calc_history_table'], "")


if __name__ == '__main__':
    app.run()
