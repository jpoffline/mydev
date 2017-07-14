# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import lib.ajax.ajax_aux as ajax_aux
import lib.tools.tools as tools
import lib.services.hostinfo as hosttools
import lib.widgets.htmlwidgets as htmlwidgets
import lib.model_adder as modeladder
import lib.sqlite.inmemory.database as ims
import flasksite.site as site
app = Flask(__name__)


history = []
model = modeladder.ModelAdder(hosttools)
inmemorydb = modeladder.ModelAdder(hosttools, database=ims.inmemorydb())
inmemorydb._create_db()

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    history.append({'a': a, 'b': b})

    model._create_db()
    model.add_history_item(a, b)
    inmemorydb.add_history_item(a, b)
    print inmemorydb.get_all_history(returnit=True)

    table_html = "<h2>All history</h2>" + model.serialise_history()

    return jsonify(
        result=a + b,
        history=[{'a': a, 'b': b}],
        nuses=len(history),
        rgb=tools.val_to_rgb(a+b),
        histtbl=table_html
    )


@app.route('/')
def index():
    return site.index_page()

if __name__ == '__main__':
    app.run()
