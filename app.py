from flask import Flask, request, jsonify
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)

model_name = "valhalla/t5-base-e2e-qg"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

@app.route('/generate-questions', methods=['POST'])
def generate_questions_endpoint():
    data = request.json
    text = data.get('text', '')
    input_text = f"generate questions: {text}"
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    questions = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'questions': questions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
