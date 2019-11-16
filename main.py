import time
from flask import Flask, request
from PIL import Image
import json
from ImageClassification import ImageClassification
app = Flask(__name__)

classification  = ImageClassification()

@app.route('/')
def hello():
    return "Hello"

@app.route('/predict' , methods=["POST"])
def predict():
    print (request.files)
    if request.method == 'POST' and request.files['image']:
        img = request.files['image']
        img.save('./temp/test.png')
        image_data = open('./temp/test.png', "rb")
        result  = classification.get_classified_name_of_image(image_data)
        return json.dumps(result)
    return "Image not found"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)