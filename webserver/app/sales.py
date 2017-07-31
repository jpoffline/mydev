from flask import Flask, jsonify, render_template, request, url_for, redirect, session
import config as config
import os
import lib.applogic.sales as sales
import lib.tools.tools as tools
import lib.applogic.usermanagement.users as users
sales = sales.Sales()
users = users.UsersDB()
import lib.widgets.bswidgets as bswidgets
app = Flask(__name__)


def get_menuItems():
    """ Get items to be rendered into the LHS-menu """
    return {
        'nsales': sales.get_nsales(),
        'username': session.get('username', 'anon')
    }


@app.route('/login')
def login():
    return render_template('screens/login.html',
                           existingusers=users.get_usernames())


@app.route('/submituserlogin', methods=['POST'])
def submituserlogin():
    if request.form['username-select-existing'] != '-':
        meta = users.get_usersmeta_for_username(
            request.form['username-select-existing'].encode('ascii', 'ignore')
        )
        users.log_user_in(
            meta
        )
        realname = meta['realname']
        username = meta['username']
    else:
        username = request.form['username'].encode('ascii', 'ignore')
        realname = request.form['realname'].encode('ascii', 'ignore')
        users.log_user_in({
            'username': username,
            'realname': realname})
    session['username'] = username
    session['logged_in'] = True
    sales.log_user_in(username)
    return redirect('/welcome/' + username)


@app.route('/')
@app.route('/welcome/<name>')
def index(name=config.OWNER):
    if not session.get('logged_in'):
        return redirect('/login')

    vbmeta = {
        'boxtype' : 'primary',
        'icon' : 'gbp',
        'boxtext': 'Total sales',
        'boxvalue': sales.get_totalsales()
    }

    vbmeta2 = {
        'boxtype' : 'info',
        'icon' : 'pencil',
        'boxtext': 'Number of sales',
        'boxvalue': sales.get_nsales()
    }

    bmeta3 = {
        'boxtype' : 'danger',
        'icon' : 'gbp',
        'boxtext': 'Average per sale',
        'boxvalue': sales.get_average_sale()
    }

    salessummary = bswidgets.bsValueBox_collection([vbmeta,vbmeta2, bmeta3])
    
    return render_template('screens/index.html',
                           menuItems=get_menuItems(),
                           name=session['username'],
                           appname=config.APPNAME,
                           args={'salessummary': salessummary})


@app.route('/logsale', methods=['POST'])
def logsale():
    sale_info = {
        'user': session['username'],
        'title': request.form['sale-title'],
        'description': request.form['sale-description'],
        'amount': request.form['sale-amount']
    }
    sales.add_sale(sale_info)
    return render_template('screens/index.html',
                           menuItems=get_menuItems(),
                           name=session['username'],
                           logsale=sales.get_sales(),
                           appname=config.APPNAME)


@app.route('/about')
def about():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('screens/about.html',
                           menuItems=get_menuItems())


@app.route('/contact')
def contact():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('screens/contact.html',
                           menuItems=get_menuItems())


@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect('/login')

    users_html_tbl = users.user_to_table()

    return render_template('screens/admin.html',
                           menuItems=get_menuItems(),
                           args={
                               'userinfo': users_html_tbl,
                               'salesinfo': sales._sales.all_to_bstable()
                           })


@app.route('/analytics')
def analytics():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('screens/analytics.html',
                           menuItems=get_menuItems(),
                           logsale=sales.get_sales(),
                           plotamts=sales.plot_sales())


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0')
