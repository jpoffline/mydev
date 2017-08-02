from flask import Flask, jsonify, render_template, request, url_for, redirect, session
import config as config
import os
import lib.applogic.sales as sales
import lib.tools.tools as tools
import lib.applogic.usermanagement.users as users
import lib.services.hostinfo as hostinfo
import lib.sqlite.qy_factories as qyfacs
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

    box_total_sales = {
        'boxtype': 'primary',
        'icon': 'gbp',
        'boxtext': 'Total sales',
        'boxvalue': sales.get_totalsales()
    }

    box_nsales = {
        'boxtype': 'info',
        'icon': 'pencil',
        'boxtext': 'Number of sales',
        'boxvalue': sales.get_nsales()
    }

    box_average = {
        'boxtype': 'danger',
        'icon': 'gbp',
        'boxtext': 'Average per sale',
        'boxvalue': sales.get_average_sale()
    }

    salessummary = bswidgets.bsValueBox([box_total_sales, box_nsales, box_average])

    return render_template('screens/index.html',
                           menuItems=get_menuItems(),
                           name=session['username'],
                           appname=config.APPNAME,
                           args={'salessummary': salessummary.get(),
                                 'datetime': hostinfo.get_datetime(pretty=True)})


@app.route('/logsale', methods=['POST'])
def logsale():
    pulled_date = request.form['sale-time']
    if hostinfo.is_string_a_datetime(pulled_date) is not True:
        print "ERROR: invalid datetime"
        return False
    sale_info = {
        'user': session['username'],
        'title': request.form['sale-title'],
        'description': request.form['sale-description'],
        'amount': request.form['sale-amount'],
        'datetime': pulled_date
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
                           menuItems=get_menuItems(),
                           args={
                               'codeversion': config.VERSION
                           })


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


@app.route('/submitagglevelchange', methods=['POST'])
def submitagglevelchange():
    agglevel = request.form['sales-agg-level-selection']
    return redirect('/analytics/agglevel/' + agglevel)


@app.route('/analytics/agglevel/<agglevel>')
@app.route('/analytics')
def analytics(agglevel=None):
    if not session.get('logged_in'):
        return redirect('/login')
    
    if agglevel is None:
        agglevel = 'day'

    return render_template('screens/analytics.html',
                           menuItems=get_menuItems(),
                           logsale=sales.get_sales(),
                           args={
                               'agglevels': qyfacs.allowed_agg_levels(),
                               'selectedagglevel': agglevel,
                               'plots': {
                                   'aggregate': sales.plot_sales(agglevel=agglevel),
                                   'compare': sales.plot_compare_sales()
                               }
                           })


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0')
