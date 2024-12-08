from flask import Flask, render_template, request, jsonify
from converter import JapaneseToKoreanConverter

app = Flask(__name__)
converter = JapaneseToKoreanConverter()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    try:
        results = converter.process_japanese_text(text)
        if results:
            return jsonify(results[0])
        else:
            return jsonify({'error': 'No results found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
