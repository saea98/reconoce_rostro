#!/usr/bin/python
#   You can run this program and see the detections from your webcam by executing the
#   following command:
#       ./opencv_face_detection.py
# COMPILING/INSTALLING THE DLIB PYTHON INTERFACE
#   You can install dlib using the command:
#       pip install dlib
#   Alternatively, if you want to compile dlib yourself then go into the dlib
#   root folder and run:
#       python setup.py install
#   Compiling dlib should work on any operating system so long as you have
#   CMake installed.  On Ubuntu, this can be done easily by running the
#   command:
#       sudo apt-get install cmake
#   Also note that this example requires Numpy which can be installed
#   via the command:
#       pip install numpy

import sys
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
cam = cv2.VideoCapture(0)
color_green = (0,255,0)
line_width = 1
while True:
    ret_val, img = cam.read()
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dets = detector(rgb_image)
    i=0
    for det in dets:
        i=i+1
        cv2.rectangle(img,(det.left(), det.top()), (det.right(), det.bottom()), color_green, line_width)
        roi_color = img[det.top() + (det.top()-det.bottom()), det.left() + (det.left()-det.right())]
        cv2.imwrite(str((det.right()-det.left())) + str((det.bottom()-det.top())) + '_faces.jpg', roi_color)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'desconocido'+str(i),(det.left(),det.top()-10), font, 0.5,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('webcam', img)
    if cv2.waitKey(1) == 27:
        break  # esc to quit
    elif cv2.waitKey(1)  == 32:
        # SPACE pressed
        h=det.bottom()-det.top()
        w=det.right()-det.left()
        #roi= im[det.top()+h, det.left()+w]
        img_name = "opencv_frame_{}.png".format(det)
        cv2.imwrite(img_name, img)
        print("{} written!".format(img_name))
cv2.destroyAllWindows()
