from flask import Flask

app = Flask(__name__)

@app.route("/", method=['GET'])
def home():
    return "<h1> Hi kiran </h1>"

if __name__ == "__main__":
    app.run()