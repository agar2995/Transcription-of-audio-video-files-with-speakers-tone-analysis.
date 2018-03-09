# Transcription-of-audio-video-files-with-speakers-tone-analysis.
Taken audio/video files as input and converted to corresponding text files using Google API. Further, the text transcription is used for sentiment (tone) analysis of the speaker using yet another IBM Watson API. The software comes as a web application where in the user can upload the audio/video file to be converted and can download the transcribed file. Along with the transcription, the output file conveys information about the sentiment of the speaker at the sentence level of speech. The team aims at taking this project to a level where the application could live stream the audio/video files without any lag.

PREREQUISITES:
->intall requirements by command: pip install --uprade -r requirement.txt present in all folders
->If any errors occurs try the following command-
sudo apt-get insatll python-setuptools python-dev build-essential
->pip install the following:
	gooletrans
	moviepy.editor
->Download google API-KEY by signing into google cloud services and similarly create and copy username, password for tone analyser service in IBM Watson
->Install Flask 

PROCEED:
->The application runs by running server.py in Frontend folder, using command: python server.py
->After running the server, go to link "localhost:5001" in browser.
->Some sample files, to test, are present in tmp folder inside Frontend folder. (You can find hindi audio - test.wav )
->The path given in send_file() in server.py is a an absolute path of the file in the system, owing to the constraints of flask
->Upon clicking on the web app to download transcription file, the txt file from last session coud be cached, so refresh the page.

