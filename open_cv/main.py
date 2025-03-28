import numpy as np
import cv2 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

#face detection

while 1:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    i = 0
    for(x,y,w,h)in faces:
        i += 1
        cv2.rectangle(frame, (x,y),(x+w, y+h),(255,0,0),2)
        cv2.putText(frame,'face'+str(i),(x, y+h),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

##single frame

# x =1
# while(True):
#     ret, frame = cap.read()
#     x+=1
#     cv2.putText(frame,'Frame count' +str(x),(20,140),cv2.FONT_HERSHEY_PLAIN,1,(200,155,140),1)
#     cv2.imshow('frame',frame)

#     if cv2.waitKey(1)& 0xFF == ord('q'):
#         break

# cap.release()
# cap.destroyAllWindows()


##picture with text

# cap = cv2.VideoCapture(0)
# while(True):
#     ret, frame = cap.read()
#     cv2.putText(frame, 'Machine Learning',(20,140),cv2.FONT_HERSHEY_SIMPLEX, .5 ,(0,0,255),1)
#     cv2.imshow('frame',frame)

#     if cv2.waitKey(1) & 0*FF == ord('q'):
#         break
# cap.release()
# cap.destroyAllWindows()

##shape on image

# import numpy as np 
# import cv2
# from matplotlib import pyplot as plt

# img = cv2.imread('a.jpeg')

# # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # cv2.line(img,(0,0),(150,150),(255, 0, 0),2)
# # cv2.rectangle(img,(10,25),(200,150),(0,255,0),5)
# # cv2.circle(img, (100,75), 55, (0,0,255),5)
# # cv2.putText(img, 'Machine Learning',(20,140),cv2.FONT_HERSHEY_SIMPLEX, .5 ,(0,0,255),1)

# img[206:236, 224:333]=[255,0,255]

# cv2.imshow('A',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # plt.imshow(gray)
# # plt.show()
# # print(img)


# # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # print('image',gray)
