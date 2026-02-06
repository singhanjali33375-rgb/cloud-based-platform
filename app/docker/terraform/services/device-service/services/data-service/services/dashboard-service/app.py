from flask import Flask

app = Flask(__name__)

@app.route("/")
def dashboard():
    return "IoT Cloud Dashboard Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
