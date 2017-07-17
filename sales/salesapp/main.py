from flask import Flask, jsonify, render_template, request, url_for, redirect
import config as config

import lib.sales as sales

sales = sales.Sales()

app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def index(name=config.OWNER):
    return render_template('index.html', name=name)


@app.route('/logsale', methods=['POST'])
def logsale():
    title = request.form['sale-title']
    text = request.form['sale-description']
    amount = request.form['sale-amount']
    sales.add_sale(title, text, amount)
    return render_template('index.html', logsale=sales.get_sales())


@app.route('/add', methods=['POST'])
def add_entry():
    title = request.form['sale-title']
    text = request.form['sale-description']
    print title, text
    return redirect('/')




if __name__ == '__main__':
    app.run()
