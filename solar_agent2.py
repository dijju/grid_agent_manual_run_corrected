from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/inverter")
def inverter():
    return jsonify({"kWh": 15})

@app.route("/meter")
def meter():
    return jsonify({"kWh": 3})

@app.route("/curtail", methods=["POST"])
def curtail():
    data = request.json
    print("📩 SA2 received curtailment request:", data)
    return jsonify({"status": "shutting down", "received": data})

if __name__ == "__main__":
    app.run(port=5002)