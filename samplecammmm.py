import requests
import cv2
import numpy as np
import imutils

url = "http://192.168.29.15:8080/shot.jpg"
from src.yoga import maincode

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr,1)
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # stretch_near = cv2.resize(img, (780, 540),
    #                           interpolation=cv2.INTER_LINEAR)
    # cv2.imshow("Android_cam", stretch_near)
    # print(img.shape)

    cv2.imwrite("sample.jpg", img)
    res = maincode("sample.jpg")
    if res == 'na':
        cv2.putText(img, res, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.imshow('img', img)
    else:
        img = cv2.imread("static/img/output.jpg")
        cv2.imshow('img', img)

    if cv2.waitKey(1) == 27:
        break

