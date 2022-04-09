import cv2 
import time 
import posemodule as pm

cap = cv2.VideoCapture('danceVideo.mp4')
pt = 0
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    img = detector.FindPose(img)
    list = detector.findPosition_or_landmarks(img,draw=False)
    if len(list) != 0: #WHEN IT DOESN'T DETECT ANY LANDMARKS
        cv2.circle(img,(list[12][1],list[12][2]),10,(98,255,22),cv2.FILLED)
        cv2.circle(img,(list[15][1],list[15][2]),10,(98,255,22),cv2.FILLED)

    ct = time.time()
    fps = 1/(ct-pt)
    pt = ct 
    cv2.putText(img,"Frame Rate -> "+str(int(fps)),(0,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2)
    cv2.imshow("frame",img)
    cv2.waitKey(1) #for 1 millisecond delay

