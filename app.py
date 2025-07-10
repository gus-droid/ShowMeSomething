from flask import Flask, redirect, url_for, render_template

#render_template renders html pages
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/media")
def media():
    return render_template("media.html")

@app.route("/recommend")
def recommend():
    return render_template("recommend.html")

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")
