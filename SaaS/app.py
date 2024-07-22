from flask import Flask, request, jsonify
from ai_humanizer import ai_humanizer
from ai_detector import ai_detector
from ai_generator import ai_generator

app = Flask(__name__)

@app.route('/humanize', methods=['POST'])
def humanize():
    data = request.get_json()
    text = data['text']
    humanized_text = ai_humanizer(text)
    return jsonify({'humanized_text': humanized_text})

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    text = data['text']
    detection_result = ai_detector(text)
    return jsonify({'detection_result': detection_result})

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data['prompt']
    generated_text = ai_generator(prompt)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
