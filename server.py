from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/steal-data', methods=['POST'])
def steal_data():
    data = request.json
    print("Received data:", data)  # Log the data
    return jsonify({"status": "success", "message": "Data received"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
