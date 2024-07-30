import os
import time
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
    url = "https://api-inference.huggingface.co/models/google/flan-t5-small"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    prompt = (
        f"Generate diverse and educational questions on the topic of {topic}. "
        f"The questions should be suitable for a {difficulty} level, {grade} grade student. "
        f"Ensure the questions are relevant and clear. The questions should be based on {grade} grade textbooks for Advanced Physics, Chemistry, Maths, Biology."
    )

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 300,
            "num_return_sequences": 1,
            "temperature": 0.7,
            "top_p": 0.9
        }
    }

    while True:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            generated_text = result[0].get("generated_text", "")
            questions = parse_questions(generated_text)
            return questions
        elif response.status_code == 503:
            time.sleep(10)  # Wait for 10 seconds if the model is loading
        else:
            return [f"Error generating questions: {response.text}"]

def parse_questions(generated_text):
    # Split the text into potential questions by newlines and filter out non-questions
    lines = generated_text.split('\n')
    questions = [line.strip() for line in lines if line.strip().endswith('?')]
    return questions if questions else ["No valid questions generated"]


if __name__ == '__main__':
    app.run(debug=True)
