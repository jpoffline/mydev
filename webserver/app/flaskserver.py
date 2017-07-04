# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
from lib.ajax_aux import *
app = Flask(__name__)


history = []


@app.route('/_add_numbers')
def add_numbers():

    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    history.append({'a': a, 'b': b})
    print history
    return jsonify(result=a + b, history=[{'a': a, 'b': b}], nuses=len(history))


@app.route('/')
def index():
    meta = {
        'route': '/_add_numbers',
        'id_action': 'a#calculate',
        'id_result': 'result',
        'id_data': ['a', 'b'],
        'id_result_hist': 'history',
        'id_result_uses': 'nuses'
    }

    return page_head() +\
        get_ajax(meta) + \
        "<h1>jQuery Example</h1><p>" + \
        numeric_boxes(meta['id_data']) + "=" + \
        span(meta['id_result'], "?") + "<p>" + \
        link("#", "calculate", "DO IT") + \
        "<h2>N uses: " + span(meta['id_result_uses'], "") + "</h2>" +\
        "<h2>calc history</h2>" + \
        "<table id=\"" + meta['id_result_hist'] + \
        "\"><tr><th>a</th><th>b</th></tr></table>"


if __name__ == '__main__':
    app.run()
