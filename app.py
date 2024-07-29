from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    data = request.json
    topic = data.get('topic')
    grade = data.get('grade')
    difficulty = data.get('difficulty')
    
    # Dummy questions for demonstration
    questions = [f"{topic} question {i} for grade {grade} at {difficulty} difficulty" for i in range(1, 10)]
    return jsonify({"questions": questions})

if __name__ == '__main__':
    app.run(debug=True)
