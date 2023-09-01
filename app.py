from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
application = app
CORS(app)


@app.route('/')
def hello():
    return 'home page!'


@app.route('/api')
def index():
    return 'index page!'


if __name__ == '__main__':
    app.run(debug=True)
