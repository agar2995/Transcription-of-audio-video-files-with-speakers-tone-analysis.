import os
from flask import Flask, request, redirect, url_for, render_template, send_file
from werkzeug import secure_filename

UPLOAD_FOLDER = 'tmp/'
ALLOWED_EXTENSIONS = set(['wav', 'mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/web/", methods=['GET', 'POST'])
def downloads():
    return send_file('/home/user1/Documents/Hackathon_2k18/hackathon/Frontend/tmp/output.txt')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = "./audiofile.txt"
            filepath = open(path, "w")
            filepath.write(filename)           
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath.close()
            os.system('python ../speech-to-text/speech2text.py')
            os.system('python ../sentiment-analysis/test.py')
            return redirect(url_for('index'))
            
            
    return """
    <!doctype html>
    <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Online audio/video transcription!</title>

  <link rel="stylesheet" type="text/css" href="static/bootstrap.min.css"/>
  </head>
    <title>Upload new File</title><br>
    <center>
    <h1>Upload new File</h1><br>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file><br/><br/>
         <input class=btn-success type=submit value=Upload>
    </form>
    <hr>
    <h4>Download transcription file <a href='/web/'>here</a>!</h4>
    </center>

    <p>%s</p>
    """ % "<br>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
