import cv2
from ImageClassification import ImageClassification
from Intent import Intent
import azure.cognitiveservices.speech as speechsdk
import json
from Tts import TextToSpeech
def convert_speech_to_text():
    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    speech_key, service_region = "c3694571998049e3878a0dd7c5ba70ec", "eastus"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Say something...")


    # Starts speech recognition, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed.  The task returns the recognition text as result.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    result = speech_recognizer.recognize_once()

    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))



intent =  Intent()
classification  = ImageClassification()
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
out = cv2.imwrite('capture.jpg', frame)
cap.release()
image_data = open('capture.jpg', "rb")

text  = convert_speech_to_text()

intents = intent.predict_intent(text)

print(intents['topScoringIntent']['intent'])

result  = classification.get_classified_name_of_image(image_data , intent)
print (result)
voiceText  = "This image consist of ";
for ob in result:
    voiceText += ob+","
app = TextToSpeech(voiceText)
app.get_token()
app.save_audio()