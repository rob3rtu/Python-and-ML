from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
classifier = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def simple_sentiment_analyzer(text):
    result = classifier(text)

    return result[0]["label"]

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        sentiment = simple_sentiment_analyzer(text)
    
    return render_template("index.html", sentiment=sentiment, text=text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)