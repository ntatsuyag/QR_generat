from datetime import date
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    data = None
    return render_template("index.html",data=data)

@app.route("/index",methods=["post"])
def post():
    data = request.form["data"]
    format = request.form["format"]
    return render_template("index.html",data=data,format=format)


if __name__ == "__main__":
    app.run(debug=True)