from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/elliot')
def wc():
    s1 = 'Elliot: FUBAR'
    return s1

@app.route('/')
def t_test():
    return render_template('home-page.html')