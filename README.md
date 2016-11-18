# TalkGoogle


Step 1:

	Get a Account on Google CloudPlatform. Do not bite your nails. Google CloudPlatform provides a free 60 days trail. you can unsubscribe anytime. And they will not charge you with your input.
	
	Click on the below link and follow the instuctions.
	Cloud Speech API BETA 
	Speech to text conversion powered by machine learning

	https://cloud.google.com/speech/
	
Step 2:
	Install the Google cloud SDK https://cloud.google.com/sdk/
	
	Authenticate yourself to run locally. use the below command
		gcloud beta auth application-default login

Step 3:
	Install the project dependencies.
	
	pip install -r ./google-client-api/requirements.txt
	
Step 4:
		Using Google Speech api converts speech to text. Next we need to query the text to cloud to get answers. I took wolframalpha free api help to do that.
		
		Get your own free API key here http://products.wolframalpha.com/api/
		
		Paste your key in queryText.py file under "app_id" variable
		
Step 5:
		Next we need to convert Text to Speech . I use "Python text-to-speech with pyttsx" to do that.
		
Step 6:
	Combining all together.
	run the ./queryspeech2speech.sh
