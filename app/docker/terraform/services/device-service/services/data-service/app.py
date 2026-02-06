from flask import Flask

app = Flask(__name__)

@app.route("/process")
def process_data():
    return "IoT Data Processed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
