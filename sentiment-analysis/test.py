from watson_developer_cloud import ToneAnalyzerV3
import json
import re

tone_analyzer = ToneAnalyzerV3(
  username='cd3afb4a-d970-48c1-a04e-32e13e2cba3a',
  password='ixVkmRwxkSWz',
  version='2017-09-21'
)

with open('tone.json', 'r') as tone_json:
  tone = tone_analyzer.tone(tone_json.read())

jsonobject =json.dumps(tone, indent=2);
print(jsonobject)
f2 = open("./tone.json", "r")
js = f2.read()
js2 = json.loads(js)
data = json.loads(jsonobject)


filePath = "../Frontend/recordings.txt"
f1 = open(filePath, "r")
input = f1.read()
st = []
st = input.split('/',2)
name = st[len(st)-1];
filename = name.split('.',1)

outputfile = "./tmp/output.txt"
output = open(outputfile, "w")

if len(data.keys())==1 :
	output.write(js2.get('text'))
	print(js2.get('text')),
	for tones in data['document_tone']['tones']:
		print ('('+str(tones.get('tone_name'))+')')
		output.write('('+str(tones.get('tone_name'))+')')
else:
	for sent in data['sentences_tone']:
	  output.write(sent.get('text'))
	  print(sent.get('text')),
	  for tones in sent['tones']:
		print ('('+str(tones.get('tone_name'))+')')
		output.write('('+str(tones.get('tone_name'))+')')


fileSentiments = "./tmp/output.json"
print(fileSentiments)
f = open(fileSentiments, "w")
f.write(json.dumps(tone, indent=2))
f.close()
f1.close()
f2.close()

