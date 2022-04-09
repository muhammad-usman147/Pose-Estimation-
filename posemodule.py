import cv2
import mediapipe as mp #framework for pose estimationn 
import time

class poseDetector():
    def __init__(self,mode = False, upbody=False, smooth=True,detectioncon = 0.5, trackingcon=0.5):
        self.mode = mode 
        self.upBody = upbody
        self.smooth = smooth
        self.detectionCon = detectioncon
        self.trackCon = trackingcon 
        #creating our model to detect pose
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose() #creating object with default parameters
        self.mpDraw = mp.solutions.drawing_utils
    

    #creating method to find pose
    def FindPose(self,img, draw = True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB) #passingv the image to the model
        #print(results.pose_landmarks)
   
        if self.results.pose_landmarks:
             #if landmark exists
            if draw:
                 self. mpDraw.draw_landmarks(img, self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)

            #POSE_LAMDMARKS -> TO DRAW LANDMARKS(RED SPOTS)
            #POSE_CONNECTIONS -> TO DRAW CONNECTIONS BETWEEN THE LANDMARKS

        return img
    #finding points

    def findPosition_or_landmarks(self,img,draw= True):
        #checking if the results are available and put them in the list
        landmark_list = []



        #Extracting information from the landmarks
        for id, landmark in enumerate(self.results.pose_landmarks.landmark):
                #getting the shape
                h,w,c = img.shape
                cx = int(landmark.x * w) #getting the pixel value for width 
                cy = int(landmark.y * h)
                landmark_list.append([id,cx,cy])
                if draw:

                    #drawing circle to check are the cx,cy pixels are calculated properly
                    cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)

        return landmark_list



# def main():
#     cap = cv2.VideoCapture('danceVideo.mp4')
#     pt = 0
#     detector = poseDetector()
#     while True:
#         _, img = cap.read()
#         img = detector.FindPose(img)
#         #draw = False, if we only want to draw specific landmarks
#         list = detector.findPosition_or_landmarks(img,draw = False)

#         #if draw = False in findPosition_or_landmarks, then uncomment below circle
#         #if draw = True in findPosition_or_landmarks, then comment below circle
#         cv2.circle(img,(list[15][1],list[15][2]),10,(0,255,0),cv2.FILLED)


 
#         ct = time.time()
#         #print(ct,pt)

#         fps = 1/(ct - pt)
#         pt = ct
#         cv2.putText(img,"Frame Rate"+str(int(fps)),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)

#         cv2.imshow("frame",img)
#         cv2.waitKey(1) #for 1 millisecond delay



if __name__ == '__main__':
    main()