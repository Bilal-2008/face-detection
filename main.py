import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import cv2

UPLOAD_FOLDER = './'

face_cascade = cv2.CascadeClassifier('./face.xml')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/face/detection/', methods=['POST'])
def face_detection():
    info=None
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath=os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    img = cv2.imread(filepath)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        infos={
                "x": x,
                "y": y,
                "w": w,
                "h": h
            }
    return infos

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=12345)
