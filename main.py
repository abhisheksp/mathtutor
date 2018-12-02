from flask import Flask, request, jsonify

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
    latex_string = ocr.parse_images(image_urls)
    feedback = wolfram.solve(latex_string)
    return jsonify(feedback)


if __name__ == '__main__':
    app.run()
