import cv2
import numpy as np

StopCascade = cv2.CascadeClassifier("Ressources/stopsign_classifier.xml")
priorityCascade = cv2.CascadeClassifier("Ressources/priority.xml")
cederCascade = cv2.CascadeClassifier("Ressources/ceder.xml")

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img =cap.read()
    cv2.imshow("Video", img)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stops = StopCascade.detectMultiScale(imgGray, 1.1, 4)
    priority = priorityCascade.detectMultiScale(imgGray, 1.1, 4)
    ceder = cederCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in stops:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print('Stop')
    for (x, y, w, h) in priority:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        print('Priority')
    """    
    for (x, y, w, h) in limit50:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        #print('Limit 50km/h')
    for (x, y, w, h) in parking:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        print('No parking here')
    cv2.imshow("a", img)"""
    for (x, y, w, h) in ceder:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        print('ceder')
    cv2.imshow("a", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.waitKey(0)

