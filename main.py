import time
from flask import Flask, request
from PIL import Image
import json
from ImageClassification import ImageClassification
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
app = Flask(__name__)

classification  = ImageClassification()

@app.route('/')
def hello():
    return "Hello"

@app.route('/predict' , methods=["POST"])
def predict():
    print (request.files['image'])
    if request.method == 'POST' and request.files['image']:
        img = request.files['image']
        blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=piyush1diag;AccountKey=YlsPLuQK0k2+rybGuZUI2ddM3327PIGdeRh+KE9mFo0s8e0Zmem4HMsBvr6vqRet/cku7erI7tI7bHqoPtMPNg==;EndpointSuffix=core.windows.net")
        blob_client = blob_service_client.get_blob_client(container="quickstartblobs", blob="temp.jpg")
        with open("temp1", "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

        Image.open("temp1").save("temp2" + '.jpg', 'JPEG')

        image_data = open('temp2.jpg', "rb")
        result  = classification.get_classified_name_of_image(image_data)
        return json.dumps(result)
    return "Image not found"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)