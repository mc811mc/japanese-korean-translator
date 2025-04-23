from flask import Flask, request, jsonify, render_template
from converter import JapaneseToKoreanConverter

app = Flask(__name__)
converter = JapaneseToKoreanConverter()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        # Process the Japanese text and get results
        results = converter.process_japanese_text(text)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)