#!/usr/bin/env python

"""Google Cloud Speech API sample application using the REST API for batch
processing."""

# Reference from Google Speech Recognition API
# https://cloud.google.com/speech/docs/common/auth
# https://cloud.google.com/speech/docs/rest-tutorial

import argparse
import base64
import json
from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')


# Application default credentials provided by env variable
# GOOGLE_APPLICATION_CREDENTIALS
def get_speech_service():
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    return discovery.build(
        'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)
# [END authenticating]


def main(speech_file):

    with open(speech_file, 'rb') as speech:
        # Base64 encode the binary audio file for inclusion in the JSON
        # request.
        speech_content = base64.b64encode(speech.read())

		service = get_speech_service()
		service_request = service.speech().syncrecognize(
        body={
            'config': {
                'encoding': 'LINEAR16',  
                'sampleRate': 16000, 
                'languageCode': 'en-US',
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })
    # [END construct_request]
    # [START send_request]
    response = service_request.execute()
    try:
    	#print(json.dumps(response))
		data = json.loads(json.dumps(response))
		if data is not None:
			#print("inside 1 {}".format(str(data["results"])))
			for result in data["results"]:
			#	print(result["alternatives"])
				for response in result["alternatives"]:
					confidence = response["confidence"]
					transcript = response["transcript"]
					print(transcript)
					#print("confidence= {}, result= {}".format(confidence,transcript))
    except BaseException as e:
		print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'speech_file', help='Full path of audio file to be recognized')
    args = parser.parse_args()
    main(args.speech_file)
