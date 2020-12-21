import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route('/')
def hello():
    return "Type your name in the url (e.g. 'https://realpython-wordcount-pro.herokuapp.com/jongmin')"

@app.route('/<name>')
def hello_names(name):
    return f"I love you {name}!"

if __name__ == '__main__':
    print(os.getenv('APP_SETTINGS'))
    app.run()
