from flask import Flask, render_template
from flask.helpers import url_for
from werkzeug.utils import redirect

dog = Flask(__name__)


@dog.route('/')
def main():
    return render_template('index.html')
@dog.route('/home')
def hello():
    return render_template('test.html')

if __name__=='__main__':
    dog.run()
    
