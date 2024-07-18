
import cv2
import os
dire="JPEGImages"
save="Resize_Img"
if not os.path.exists(save):
    os.makedirs(save)
img_list = os.listdir(dire)
for i in img_list:
    
    
    img = cv2.imread(os.path.join(dire, i))
    img = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(save, i),img)
