from flask import Flask, request, jsonify

import latex
import ocr
import wolfram

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1>Works!</h1>'


@app.route('/feedback', methods=['POSt'])
def feedback_handler():
    request_body = request.get_json()
    image_urls = request_body['images']
    latex_responses = ocr.parse_images(image_urls)
    formatted_responses = latex.format_response(latex_responses)
    feedback = wolfram.solve(formatted_responses)
    return jsonify(feedback)


if __name__ == '__main__':
    app.run()
