from flask import Flask, request, jsonify

from services.ai_engine import AIEngine
from services.response_formatter import format_response
app = Flask(__name__)

print("Starting SmartAssist AI Service...")

# Load AI Engine once
engine = AIEngine()

print("SmartAssist AI Service Ready!")


@app.route("/")
def home():
    return {
        "message": "SmartAssist AI Service Running"
    }


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is missing."
        }), 400

    ticket = data.get("ticket")

    if not ticket:
        return jsonify({
            "error": "Ticket is required."
        }), 400

    result = engine.analyze_ticket(ticket)

    return jsonify(format_response(result))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )