from flask import Flask, render_template, request

app = Flask("superscrapper")

#that's new!

@app.route("/")
def home():
    return render_template("scrapper.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template("report.html", searchingBy = word)

app.run(host="0.0.0.0") # initializing, releasing own website


@app.route("/contact") # @ is decorator
def contact(): # With sign '@', connected to the function below
    return "Contact me!"

@app.route("/<username>") # dynamic URL
def name(username):
    return f"Hello {username}, how are you doing?"