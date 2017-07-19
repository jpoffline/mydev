from flask import Flask, jsonify, render_template, request, url_for, redirect, session
import config as config
import os
import lib.applogic.sales as sales
import lib.applogic.usermanagement.users as users
sales = sales.Sales()
users = users.UsersDB()

app = Flask(__name__)


def get_menuItems():
    """ Get items to be rendered into the LHS-menu """
    return {
        'n': sales.get_nsales(),
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
    print 'All usernames: ', users.get_usernames()
    print 'Logged in users: ', users.get_loggedin_users()
    session['username'] = username
    session['logged_in'] = True
    return redirect('/hello/' + realname)


@app.route('/')
@app.route('/hello/<name>')
def index(name=config.OWNER):
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('screens/index.html',
                           menuItems=get_menuItems(),
                           name=session['username'],
                           appname=config.APPNAME)


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
    app.run()
