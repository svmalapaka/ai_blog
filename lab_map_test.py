from flask import Flask, render_template

app = Flask(__name__)

@app.route('/lab-map')
def lab_map():
    return "<h1>✅ Lab Map Test Works</h1>"

if __name__ == "__main__":
    app.run()
