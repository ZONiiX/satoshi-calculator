from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"SAT/USD": satoshiUSD})

if __name__ == '__main__':
    app.run(debug=True);
