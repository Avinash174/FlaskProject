from flask import Flask, render_template, request, url_for, redirect,jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Hello Avinash, Welcome to Flask"

@app.route("/index", methods=["GET"])
def index():
    return "<h1>Welcome to Index Page</h1>"

# Variable rule 
@app.route("/success/<int:score>")
def success(score):
    return f"<h2>Congratulations! Your Score: {score}</h2>"

@app.route('/fail/<int:score>')
def fail(score):
    return f"<h1>Try again next year, you failed. Score: {score}</h1>"

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Retrieve input values
        history = float(request.form['history'])
        math = float(request.form['math'])
        science = float(request.form['science'])

        # Calculate average marks
        avg_marks = (history + math + science) / 3
        
        # Determine success or failure
        res = "success" if avg_marks >= 50 else "fail"
        
        # Redirect to appropriate page with integer score
        return redirect(url_for(res, score=int(avg_marks)))  

    # Handle GET request
    return render_template('form.html', score=None)

@app.route('/api', methods=["POST"])
def calculate_sum():
    data=request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val+b_val)
    
    

if __name__ == '__main__':
    app.run(debug=True)
