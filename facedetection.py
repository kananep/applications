import cv2


face_cascade_model =  cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread('re.png')
resize_image = cv2.resize(img, (int(img.shape[1]/7) , int(img.shape[0]/7)))


face_figures = face_cascade_model.detectMultiScale(resize_image, 
                                                   scaleFactor=1.05,
                                                   minNeighbors=5,
                                                   )


for x, y, w, h in face_figures:
    img = cv2.rectangle(resize_image, (x,y),(x+w,y+h),(0,255,0),3)
     
print('Face Detected')
print()
print('Face Type')
print(type(face_figures))
print()
print('Face Cordinate points')
print(face_figures)
     
cv2.imshow('Retouch',img)
cv2.waitKey(0)
cv2.destroyAllWindows



