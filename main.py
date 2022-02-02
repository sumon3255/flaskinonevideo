from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    name = "sumon"
    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        result = int(num1) + int(num2)
        return render_template("index.html",result=result,name=name)
  
    return render_template("index.html",name=name)
    
    


if __name__ == "__main__":
    app.run(debug=True)