import cv2
import numpy as np
from PIL import Image

cam=cv2.VideoCapture(0)
green=[0,255,0] #in bgr 
font = cv2.QT_FONT_NORMAL
font_scale = 1
font_color = (0, 0, 255) # red color for text (BGR)
font_thickness=2


def get_limits(color):
    c=np.uint8([[color]])
    hsvC=cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower_limit=hsvC[0][0][0]- 10,100,100
    upper_limit=hsvC[0][0][0]+ 10,255,255

    lower_limit=np.array(lower_limit,dtype=np.uint8)
    upper_limit=np.array(upper_limit,dtype=np.uint8)

    return lower_limit,upper_limit

while True:
    ret,frame=cam.read()
    hsv_image=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limit,upper_limit=get_limits(color=green)

    mask=cv2.inRange(hsv_image,lower_limit,upper_limit)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    print(bbox)
    if bbox is not None:
        x1,y1,x2,y2=bbox
        flower=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
        # rsize=cv2.resize(flower,(1980,1980),interpolation=cv2.INTER_LINEAR)
        
        cv2.putText(flower, "GREEN", (x1+10 , y1-10), font_scale, font,font_color,font_thickness, cv2.LINE_AA)

        cv2.imshow('my show',flower)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()