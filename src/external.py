import numpy as np
import cv2

# returns numpy arrays with xy coordinates and descriptors
def calling_function(image):
    
    im2=cv2.imdecode(np.frombuffer(image,dtype='uint8'), cv2.IMREAD_COLOR)
    gray= cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    kp,desc = sift.detectAndCompute(gray,None)    
#    img=cv2.drawKeypoints(gray,kp,im2,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#    cv2.imwrite('debug/sift_keypoints.jpg',img)
    return cv2.KeyPoint_convert(kp), desc

