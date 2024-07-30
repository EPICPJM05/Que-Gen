import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")

app = Flask(__name__)

@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    topic = data.get('topic')
    grade = data.get('grade')
    difficulty = data.get('difficulty')

    questions = generate_ai_questions(topic, grade, difficulty)
    return jsonify({"questions": questions})

def generate_ai_questions(topic, grade, difficulty):
    url = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3.1-8B-Instruct"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    payload = {
        "inputs": f"Generate 10 questions for a {difficulty}, {grade} grade student on the topic of {topic}.",
        "parameters": {
            "max_length": 100,
            "num_return_sequences": 5
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    
    # Debugging: Print response status and text
    print("Response status:", response.status_code)
    print("Response text:", response.text)

    if response.status_code == 200:
        result = response.json()
        return [item["generated_text"] for item in result]
    else:
        return ["Error generating questions"]

if __name__ == '__main__':
    app.run(debug=True)
