#NovusLive

from flask import Flask, render_template, Response
import cv2
import numpy as np

#path to classifiers
path = 'C:/Users/mrspe/OneDrive - Waterford Institute of Technology/Desktop/Local Github/opencv/data/haarcascades/'

#get image classifiers
face_cascade = cv2.CascadeClassifier(path +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(path +'haarcascade_eye.xml')

#read image
img = cv2.imread('people.jpg')

#convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#for each face
for (x,y,w,h) in faces:

    #draw rectangle around face
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    #select face as region of interest 
    roi_g = gray[y:y+h,x:x+h]
    roi_c = img[y:y+h,x:x+h]

    #within region of interest find eyes
    eyes = eye_cascade.detectMultiScale(roi_g)
    
    #for each eye
    for (ex,ey,ew,eh) in eyes:
        #draw retangle around eye
        cv2.rectangle(roi_c, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img) #shows image
cv2.waitKey(0) #waits until a key is pressed to progress
cv2.destroyAllWindows() #closes windows






# app = Flask(__name__)

# camera = cv2.VideoCapture(0)  # use 0 for web camera

# def gen_frames():  # generate frame by frame from camera
#     while True:
#         # Capture frame-by-frame
#         success, frame = camera.read()  # read the camera frame
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


# @app.route('/video_feed')
# def video_feed():
#     #Video streaming route. Put this in the src attribute of an img tag
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/')
# def index():
#     #Video streaming Home Page
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

#mux

