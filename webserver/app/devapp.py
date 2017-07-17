# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import lib.ajax.ajax_aux as ajax_aux
import lib.tools.tools as tools
import lib.services.hostinfo as hosttools
import lib.widgets.htmlwidgets as htmlwidgets
import lib.models.model_adder as modeladder
import lib.sqlite.inmemory.database as ims
import lib.sqlite.sqlite_api as sql
import flasksite.site as site
app = Flask(__name__)


history = []
model = modeladder.ModelAdder(hosttools, sql)
inmemorydb = modeladder.ModelAdder(hosttools, ims.inmemorydb())
inmemorydb._create_db()

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    history.append({'a': a, 'b': b})

    model.create_db()
    model.add_history_item(a, b)
    inmemorydb.add_history_item(a, b)
    print inmemorydb.get_all_history(returnit=True)[0]
    hist = model.serialise_history()
    hist_dt = htmlwidgets.datatable(hist[1], hist[0])
    table_html = "<h2>All history</h2>" + hist_dt

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
