import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
lastValue = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    landmarks = []
    value = 0
    i = 0
    finger1 = 0
    finger2 = 0
    finger3 = 0
    finger4 = 0
    finger5 = 0

    if results.multi_hand_landmarks:
        for handLand in results.multi_hand_landmarks:
            for id, lm in enumerate(handLand.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append(cy)
            for x in landmarks:
                value = value + x
            finger1 = landmarks[1] + landmarks[2] + landmarks[3] + landmarks[4]
            finger2 = landmarks[5] + landmarks[6] + landmarks[7] + landmarks[8]
            finger3 = landmarks[9] + landmarks[10] + landmarks[11] + landmarks[12]
            finger4 = landmarks[13] + landmarks[14] + landmarks[15] + landmarks[16]
            finger5 = landmarks[17] + landmarks[18] + landmarks[19] + landmarks[20]
            if finger3 < (finger1 - 100) and finger3 < (finger2 - 100) and finger3 < (finger4 - 100) and finger3 < (finger5 - 100):
                print("Fuck You Too, buddy!")
            mpDraw.draw_landmarks(img, handLand, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)