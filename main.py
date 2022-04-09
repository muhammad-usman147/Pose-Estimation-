import cv2
import mediapipe as mp #framework for pose estimationn 
import time

#creating our model to detect pose
mpPose = mp.solutions.pose
pose = mpPose.Pose() #creating object with default parameters


mpDraw = mp.solutions.drawing_utils

#read our  video 
cap = cv2.VideoCapture('danceVideo.mp4')
pt = 0
while True:
    _, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img) #passing the image to the model
    #print(results.pose_landmarks)
    if results.pose_landmarks: #if landmark exists
        mpDraw.draw_landmarks(img, results.pose_landmarks,mpPose.POSE_CONNECTIONS)

        #POSE_LAMDMARKS -> TO DRAW LANDMARKS(RED SPOTS)
        #POSE_CONNECTIONS -> TO DRAW CONNECTIONS BETWEEN THE LANDMARKS

        #Extracting information from the landmarks
        for id, landmark in enumerate(results.pose_landmarks.landmark):
            #getting the shape
            h,w,c = img.shape
            cx = int(landmark.x * w) #getting the pixel value for width 
            cy = int(landmark.y * h)

            #drawing circle to check are the cx,cy pixels are calculated properly
            # cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)



    ct = time.time()
    #print(ct,pt)

    fps = 1/(ct - pt)
    pt = ct
    cv2.putText(img,"Frame Rate"+str(int(fps)),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

    cv2.imshow("frame",img)
    cv2.waitKey(1) #for 1 millisecond delay

