from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Type your name in the url (e.g. 'https://realpython-wordcount-pro.herokuapp.com/jongmin')"

@app.route('/<name>')
def hello_names(name):
    return f"I love you {name}!"

if __name__ == '__main__':
    app.run()