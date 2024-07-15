import cv2 as cv

img1= cv.imread('C:/Users/subha/Pictures/singleG.jpg')
new_width = 500
new_height = 500
resized_image = cv.resize(img1, (new_width, new_height))
cv.imshow('SingleG',img1)

img2= cv.imread('C:/Users/subha/Pictures/both.jpg')
def rotate(img2, angle, rotPoint=None):
    (height,width) = img2.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img2, rotMat, dimensions)
rotated = rotate(img2, 90)
#cv.imshow('Rotated', rotated)
new_width1 = 500
new_height1 = 500
rotated = cv.resize(rotated, (new_width1, new_height1))
#cv.imshow('SingleG',rotated)


gray=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
new_width2 = 500
new_height2 = 500
resized_image2 = cv.resize(gray, (new_width2, new_height2))
#cv.imshow('gray singleG',resized_image2)

haar_cascade=cv.CascadeClassifier('D:/Studies/Open CV/opencv-course-master/opencv-course-master/Section #3 - Faces/haar_face.xml')
faces_rect=haar_cascade.detectMultiScale(resized_image,scaleFactor=1.1,minNeighbors=3)

print(f"Number of faces found in pic : {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(resized_image,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('detected_faces',resized_image)

cv.waitKey(0)