from flask import Flask, jsonify
import time
import threading

app = Flask(__name__)
current_high = False

def toggle_frequency():
    global current_high
    while True:
        current_high = not current_high
        print(f"Toggling grid frequency to {'HIGH (55.0 Hz)' if current_high else 'LOW (48.5 Hz)'}")
        time.sleep(10)

@app.route("/fgrid")
def get_fgrid():
    return jsonify({"fgrid": 55.0 if current_high else 48.5})

if __name__ == "__main__":
    threading.Thread(target=toggle_frequency, daemon=True).start()
    app.run(port=7000)