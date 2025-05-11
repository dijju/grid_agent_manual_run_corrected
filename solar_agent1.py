from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/inverter")
def inverter():
    return jsonify({"kWh": 20})

@app.route("/meter")
def meter():
    return jsonify({"kWh": 5})

@app.route("/curtail", methods=["POST"])
def curtail():
    data = request.json
    print("📩 SA1 received curtailment request:", data)
    return jsonify({"status": "shutting down", "received": data})

if __name__ == "__main__":
    app.run(port=5001)