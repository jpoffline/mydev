from flask import Flask, jsonify, render_template, request, url_for, redirect
import config as config

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
    print 'LOG', title, text
    return render_template('index.html', logsale_title=title, logsale_text=text, logsale_amount=amount)


@app.route('/add', methods=['POST'])
def add_entry():
    title = request.form['sale-title']
    text = request.form['sale-description']
    print title, text
    return redirect('/')




if __name__ == '__main__':
    app.run()