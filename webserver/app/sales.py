from flask import Flask, jsonify, render_template, request, url_for, redirect
import config as config

import lib.applogic.sales as sales

sales = sales.Sales()

app = Flask(__name__)

def get_menuItems():
    menuItems = {'n': sales.get_nsales()}
    return menuItems


@app.route('/')
@app.route('/hello/<name>')
def index(name=config.OWNER):
    return render_template('screens/index.html', menuItems=get_menuItems(), name=name, appname=config.APPNAME)


@app.route('/logsale', methods=['POST'])
def logsale():
    sale_info = {
        'title': request.form['sale-title'],
        'description': request.form['sale-description'],
        'amount': request.form['sale-amount']
    }
    sales.add_sale(sale_info)
    return render_template('screens/index.html', menuItems=get_menuItems(),logsale=sales.get_sales(), appname=config.APPNAME)


@app.route('/about')
def about():
    return render_template('screens/about.html', menuItems=get_menuItems())


@app.route('/contact')
def contact():
    return render_template('screens/contact.html', menuItems=get_menuItems())


@app.route('/analytics')
def analytics():
    return render_template('screens/analytics.html', menuItems=get_menuItems(), logsale=sales.get_sales())





if __name__ == '__main__':
    app.run()
