from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/fgrid")
def get_fgrid():
    # Simulate a high grid frequency to trigger curtailment and battery charge
    return jsonify({"fgrid": 55.0})

if __name__ == "__main__":
    app.run(port=7000)