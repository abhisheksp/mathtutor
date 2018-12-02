import json
import requests

with open('mathpix.json') as f:
    data = json.load(f)
    app_id = data['app_id']
    app_key = data['app_key']


def parse_images(image_urls):
    responses = []
    for image_url in image_urls:
        request = requests.post(
            "https://api.mathpix.com/v3/latex",
            data=json.dumps({'src': image_url}),
            headers={
                "app_id": app_id,
                "app_key": app_key,
                "Content-type": "application/json"}
        )
        response = json.loads(request.text)
        responses.append(response['latex'])
    return responses
