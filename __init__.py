from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from sqlite3 import sql

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
    
@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
   user = request.form['nm']
   
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = cookies.get('userID')
   return ()

@app.route('/canvas',methods = ['POST', 'GET'])
def canvas():
   if request.method == 'POST':
      canvas = request.form
      return render_template("canvas.html",canvas = canvas)  

@app.route('/images',methods = ['POST', 'GET'])
def  images():
   if request.method == 'POST':
      images = request.form
      return render_template("images.html",images = images)
  

if __name__ == '__main__':
   app.run(host = '0.0.0.0', debug = True)
