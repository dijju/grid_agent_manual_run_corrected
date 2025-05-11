from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/charge", methods=["POST"])
def charge():
    data = request.json
    print("🔌 Battery received charge request:", data)
    return jsonify({"status": "charging", "received": data})

if __name__ == "__main__":
    app.run(port=6001)