# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    data = request.json
    topic = data.get('topic')
    grade = data.get('grade')
    difficulty = data.get('difficulty')

    # Mock question generation logic (Replace with your AI model)
    questions = generate_mock_questions(topic, grade, difficulty)

    return jsonify({'questions': questions})

def generate_mock_questions(topic, grade, difficulty):
    # This is a placeholder for the actual AI-based question generation logic
    return [
        f"Question 1 about {topic} for grade {grade} at {difficulty} level.",
        f"Question 2 about {topic} for grade {grade} at {difficulty} level.",
        f"Question 3 about {topic} for grade {grade} at {difficulty} level.",
    ]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
