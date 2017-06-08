from flask import Flask
from flask import render_template
import os


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/gegevens')
def gegevens():
    return render_template('gegevens.html')

@app.route('/profiel')
def profiel():
    return render_template('profiel.html')

@app.route('/instellingen')
def instellingen():
    return render_template('instellingen.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=80, debug=True)
