import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

HUGGING_FACE_API_KEY = os.getenv('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')
HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/valhalla/t5-base-e2e-qg"  # Replace <model_name> with your model name

headers = {
    "Authorization": f"Bearer {HUGGING_FACE_API_KEY}"
}

@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    data = request.json
    topic = data.get('topic')
    grade = data.get('grade')
    difficulty = data.get('difficulty')

    prompt = f"Generate 15 questions for {topic} for grade {grade} at {difficulty} difficulty level."

    response = requests.post(HUGGING_FACE_API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        questions = response.json()  # Assuming the API response is a list of questions
        return jsonify({"questions": questions})
    else:
        return jsonify({"error": "Failed to generate questions"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
