from flask import Flask, redirect, url_for, request, render_template
import webbrowser

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        with open("main.py") as file:
            exec(file.read())
        webbrowser.open(r"templates\map.html")
        return redirect(url_for("index"))

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/report")
def report():
    return render_template("report.html")


app.run()
