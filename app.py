from flask import Flask, request, jsonify
import uuid
from utils import calculate_total_points

app = Flask(__name__)

receipts = {}

@app.route("/receipts/process", methods=["POST"])
def process_receipt():
    data = request.get_json()

    receipt_id = str(uuid.uuid4())
    receipts[receipt_id] = data

    return jsonify({"id": receipt_id})

@app.route("/receipts/<id>/points", methods=["GET"])
def get_points(id):
    if id not in receipts:
        return jsonify({"error": "No receipt found for that ID"}), 404

    receipt = receipts[id]
    points = calculate_total_points(receipt)

    return jsonify({"points": points})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
