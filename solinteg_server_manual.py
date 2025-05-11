from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/fgrid")
def get_fgrid():
    # Set to a high value to simulate overgeneration
    return jsonify({"fgrid": 55.0})  # Change to 48.5 to simulate normal case

if __name__ == "__main__":
    app.run(port=7000)