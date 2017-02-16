from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'December 2 1982'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name

@app.route('/add/<int:param1>/<int:param2>')
def add(param1, param2):
    return str(param1 + param2)

@app.route('/multiply/<int:param1>/<int:param2>')
def multiply(param1, param2):
    return str(param1 * param2)

@app.route('/subtract/<int:param1>/<int:param2>')
def subtract(param1, param2):
    return str(param1 - param2)

@app.route('/favoritefoods')
def favoritefoods():
    myList = ['football', 'basketball', 'rugby']
    return jsonify(myList)
