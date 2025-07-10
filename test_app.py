# test_app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Sastry — Flask is working!"

if __name__ == "__main__":
    print(">>> Flask is about to run")
    app.run(host="0.0.0.0", port=5050)
