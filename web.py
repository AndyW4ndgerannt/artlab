from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def  index():
   if request.method == 'POST':
      index = request.form
      return render_template("index.html",index = index)
    
@app.route('/home', methods = ['POST', 'GET'])
def home():
  if request.method == 'POST':
    home = request.form
    return render_template("home.hmtl",home = home)

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
   app.run(debug = True)
