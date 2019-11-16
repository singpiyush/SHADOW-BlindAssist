#!/bin/python3.6
########### Python 3.6 #############
import requests

class Intent:
    def predict_intent(self,utterance='turn on all lights'):
        try:

            key = '4956773e26f3482f9d075f82924e94f9'
            endpoint = 'westus.api.cognitive.microsoft.com' # such as 'westus2.api.cognitive.microsoft.com' 
            appId = '008f439f-ffb6-4967-9934-248b0c678210'
            # utterance = 'turn on all lights'

            headers = {
            }

            params ={
                'q': utterance,
                'timezoneOffset': '0',
                'verbose': 'true',
                'show-all-intents': 'true',
                'spellCheck': 'false',
                'staging': 'false',
                'subscription-key': key
            }
            r = requests.get(f'https://{endpoint}/luis/v2.0/apps/{appId}', params=params)
            print(r.json())


        except Exception as e:
            print(f'{e}')


if __name__=='__main__':
    import sys
    obj = Intent()
    obj.predict_intent(sys.argv[1])
