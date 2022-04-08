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
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,self.detectionCon,self.trackCon) #creating object with default parameters
        self.mpDraw = mp.solutions.drawing_utils
    

    #creating method to find pose
    def FindPose(self,img, draw = True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB) #passingv the image to the model
        #print(results.pose_landmarks)
   
        if results.pose_landmarks:
             #if landmark exists
            if draw:
                 self. mpDraw.draw_landmarks(img, results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)

            #POSE_LAMDMARKS -> TO DRAW LANDMARKS(RED SPOTS)
            #POSE_CONNECTIONS -> TO DRAW CONNECTIONS BETWEEN THE LANDMARKS

            return img
            #Extracting information from the landmarks
            # for id, landmark in enumerate(results.pose_landmarks.landmark):
            #         #getting the shape
            #         h,w,c = img.shape
            #         cx = int(landmark.x * w) #getting the pixel value for width 
            #         cy = int(landmark.y * h)

            #         #drawing circle to check are the cx,cy pixels are calculated properly
            #         # cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)

                



def main():
    cap = cv2.VideoCapture('danceVideo.mp4')
    pt = 0
    detector = poseDetector()
    while True:
        _, img = cap.read()
        img = detector.FindPose(img)
        ct = time.time()
        #print(ct,pt)

        fps = 1/(ct - pt)
        pt = ct
        cv2.putText(img,"Frame Rate"+str(int(fps)),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)

        cv2.imshow("frame",img)
        cv2.waitKey(1) #for 1 millisecond delay



if __name__ == '__main__':
    main()