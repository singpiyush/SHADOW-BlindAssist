from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
from io import BytesIO

class ImageClassification:
    def __init__(self):
        self.threshold = 0.7
        # Add your Computer Vision subscription key to your environment variables.
        if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
            self.subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
        else:
            print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
            sys.exit()
        # Add your Computer Vision endpoint to your environment variables.
        if 'COMPUTER_VISION_ENDPOINT' in os.environ:
            self.endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
        else:
            print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
            sys.exit()
        self.computervision_client = ComputerVisionClient(self.endpoint, CognitiveServicesCredentials(self.subscription_key))

    def get_classification_result(self,image):
        return self.computervision_client.detect_objects_in_stream(image )
    
    def get_classified_name_of_image(self,image):
        name = []
        result = self.get_classification_result(image)
        if result != None:
            for obj in result.objects:
                print (obj)
                if obj.confidence > self.threshold:
                    name.append(obj.object_property)
        return name

    def get_classified_color_of_image(self,image):
        pass
if __name__=="__main__":
    a = ImageClassification()
    image_path = "./temp/test.jpeg"
    image_data = open(image_path, "rb")
    print(a.get_classified_name_of_image(image_data))
