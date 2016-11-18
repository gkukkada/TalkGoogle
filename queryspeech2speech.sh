#!/bin/bash

echo "Recording… Press Ctrl+C to Stop."
rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 audio.wav > /dev/null 2>&1

echo "Processing speech to text…"
python ./google-client-api/transcribe.py audio.wav > stt.txt

echo -n "You Said: "
cat stt.txt

echo "--------------generating the response from server…-----------"
python /home/sandy/queryText.py stt.txt > query.txt

echo "--------------here is the answer.-------------------"
cat query.txt

echo "--------------Reading out loud-------------------------"
python /home/sandy/textToSpeech.py query.txt

rm audio.wav > /dev/null 2>&1