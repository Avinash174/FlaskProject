# Flask App Routing
#function name never should same

from flask import Flask,render_template,request

## create a simple flask application

app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Hello Avinash Welcome In Flask"

@app.route("/index",methods=["Get"])
def index():
    return "<h1>Welcom to Index Page<h1>"

# varible rule 

@app.route("/success/<int:score>")
def success(score):
    return "<h2>this is the<h2>"+str(score) 

@app.route('/fail/<int:score>')
def fail(score):
    return "<h1>try again next year your failed<h1>"+str(score)

if __name__=='__main__':
    app.run(debug=True)
    