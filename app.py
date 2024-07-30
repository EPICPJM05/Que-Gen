from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    
    topic = data.get('topic')
    grade = data.get('grade')
    difficulty = data.get('difficulty')
    
    # Dummy questions for demonstration
    questions = [
        "What is 2 + 2?",
        "Solve for x in the equation x + 5 = 10."
    ]
    
    return jsonify({"questions": questions})

if __name__ == '__main__':
    app.run(debug=True)
