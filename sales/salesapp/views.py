from main import app


@app.route('/next')
def index():
    return 'Hello World!'