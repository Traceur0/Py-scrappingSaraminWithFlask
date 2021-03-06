from flask import Flask, render_template, request

app = Flask("superscrapper")


@app.route("/")
def home():
    return render_template("scrapper.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template("report.html", searchingBy = word)

app.run(host="0.0.0.0") # initializing, releasing own website