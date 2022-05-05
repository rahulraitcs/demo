from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello_world():
    return 'Hello world!'


@app.route('/demo/<name>/<int:age>')
def demo(name, age):
    print(age)
    return 'Hello '+name+', Welcome to TCS demo'

#app.add_url_rule('/demo/<name>/<int:age>', 'demo', demo)

