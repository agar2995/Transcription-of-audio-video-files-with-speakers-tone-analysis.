import os
import json
import speech_recognition as sr
from tqdm import tqdm
import video2audio
from googletrans import Translator 

with open("api-key.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()


r = sr.Recognizer()

all_text = []
filepath = '../Frontend/audiofile.txt'
readfile = open(filepath,"r")
fileName= readfile.read()
sample_file = "../Frontend/tmp/" + fileName
filePath = "../Frontend/recordings.txt"
f1 = open(filePath, "w")
f1.write(sample_file)
f1.close()
name = video2audio.videoToAudio(sample_file)
# Load audio file
with sr.AudioFile(name) as source:
    audio = r.record(source)
# Transcribe audio file
text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language='en-IN')
all_text.append(text)

translator = Translator()
english = translator.translate(text)
print(english.text)

with open("transcript.txt", "w") as f:
    f.write(english.text)

fileJson = "../Frontend/tone.json"
f = open(fileJson, "w")
var = {'text': english.text }
toJson = json.dumps(var)
f.write(toJson)
f.close()
