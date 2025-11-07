from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Discipline is stronger than motivation.",
    "Code, sleep, repeat.",
    "Backend is the brain of the web.",
    "Never stop learning."
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to your first backend!"})

@app.route('/quotes')
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(debug=True)
