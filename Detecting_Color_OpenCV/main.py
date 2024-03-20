import cv2

from PIL import Image  # to Draw the box around the object
from util import get_limits

Orange = [0,165,255]  # Ornage in the BGR Colorspace
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit= get_limits(color=yellow)

    mask=cv2.inRange(hsvImage,lowerLimit,upperLimit)

    mask_=Image.fromarray(mask)

    bbox=mask_.getbbox() # Function to get the boundery Box

    if bbox is not None:
        x1,y1,x2,y2=bbox

        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

        # (0,255,0) is the Green Color and 5 is the thickness of the line around the boundery box.

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
