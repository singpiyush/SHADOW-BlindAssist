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


class ImageClassification:
    def __init__(self):
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

    def get_classification_result(self,image_url):
        return self.computervision_client.describe_image(image_url )
    
    def get_classified_name_of_image(self,image_url):
        result = self.get_classification_result(image_url)
        print (result)

if __name__=="__main__":
    a = ImageClassification()
    a.get_classified_name_of_image("https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg")
