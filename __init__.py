import os
from flask import Flask, session, redirect, url_for, escape, request, g
from flask import render_template
from sqlite3 import sql
from flask_sijax import sijax


app = Flask(__name__)

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app.config['SIJAX_STATIC_PATH'] = path

app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)

@app.route('/')
def index():
   return render_template('index.html')
    
@app.route('/home', methods = ['POST', 'GET'])
def home():
   return render_template('home.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
   user = request.form['nm']
   
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie', methods = ['POST', 'GET'])
def getcookie():
   name = cookies.get('userID')
   return ()

@app.route('/canvas', methods = ['POST', 'GET'])
def canvas():
   return render_template('canvas.html')


@app.route('/images', methods = ['POST', 'GET'])
def images():
   return render_template('images.html')

  

if __name__ == '__main__':
   app.run(host = '0.0.0.0', debug = True)
