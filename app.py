from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

RUNWAY_API_KEY = os.environ.get("RUNWAY_API_KEY")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    headers = {
        "Authorization": f"Bearer {RUNWAY_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "duration": 4,
        "ratio": "1:1"
    }

    response = requests.post(
        "https://api.runwayml.com/v1/generate/video",
        headers=headers,
        json=payload
    )

    return jsonify(response.json())

if __name__ == "__main__":
    app.run()
