#C.A.T.E.R - CURSOR ASSISTANCE THROUGH ENHANCED RECOGNITION 
import cv2
import mediapipe as mp 
import pyautogui
import time
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width , screen_height = pyautogui.size()
cap = cv2.VideoCapture(0)
index_y = 0
max_duration = 0
user_response = "y"

while user_response == "y":
    start_time = time.time()
    while time.time()-start_time < max_duration:
        _, frame = cap.read()
        frame = cv2.flip(frame , 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame , hand) # drawing the landmarks on the hand
                landmarks = hand.landmark
                for id , landmark in enumerate(landmarks):
                    x = int(landmark.x*frame_width)
                    y = int(landmark.y*frame_height)
                    
                    if id == 8:
                        cv2.circle(img=frame , center = (x,y) , radius = 10 , color = (0,255,255))
                        index_x = screen_width/frame_width*x
                        index_y = screen_height/frame_height*y
                        pyautogui.moveTo(index_x, index_y)
                    if id == 4:
                        cv2.circle(img=frame , center = (x,y) , radius = 10 , color = (0,255,255))
                        thumb_x = screen_width/frame_width*x
                        thumb_y = screen_height/frame_height*y
                        print('outside' , abs(index_y - thumb_y))
                        if abs(index_y - thumb_y) < 20: 
                            pyautogui.click()
                            pyautogui.sleep(1)
            

        elapsed_time = time.time()- start_time
        print('Elapsed time = ' , round(elapsed_time , 2), "s")
        cv2.imshow('C.A.T.E.R' , frame)
        cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()