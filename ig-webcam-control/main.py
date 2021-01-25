import cv2
import numpy as np
import pyautogui
import time

def moveDown():
    global prev_y
    yellow_lower = np.array([22, 93, 0])
    yellow_upper = np.array([45, 255, 255])

    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if y < prev_y:
                pyautogui.press('down')
                time.sleep(0.1)
            prev_y = y
            
def moveUp():
    global prev_y
    lower_blue = np.array([101,50,38])
    upper_blue = np.array([110,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if y < prev_y:
                pyautogui.press('up')
                time.sleep(0.1)
            prev_y = y



cap = cv2.VideoCapture(0)


prev_y = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    moveDown()
    moveUp()

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
