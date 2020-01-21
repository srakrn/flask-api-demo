from flask import Flask, escape, request, render_template
import classifier.bts_classifier as classifier

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analyse', methods=['POST'])
def analyse():
    print(request.form)
    result = classifier.classify(request.form["tweetText"])
    if result is None:
        result = "(no information extracted)"
    else:
        result = "Train service status: " + result
    return render_template("result.html", data={
        "tweet_text": request.form["tweetText"],
        "result": result
    })