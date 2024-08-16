import base64
from flask import Flask, request
from src.service.read_text_captcha_service import read_text_captcha_image_service

app = Flask(__name__)

@app.post("/text/base64", )
def resolve_by_base64():
    image_base64: str = request.json['image']
    
    image_bytes =base64.b64decode(image_base64)

    text = read_text_captcha_image_service(image_bytes)

    return text

@app.post("/text/file")
def resolve_by_file():
    file = request.files['image']

    teste = file.read()

    text = read_text_captcha_image_service(teste)

    return text