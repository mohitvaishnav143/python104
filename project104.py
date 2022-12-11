import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
             (120,100),
             cv2.FONT_HERSHEY_COMPLEX,
             2,
             (0,0,255)
             )

cv2.putText(img,
            "Mercury",
             (120,200),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Venus",
             (180,150),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Earth",
             (310,150),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "Mars",
             (390,150),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "Jupiter",
             (500,100),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )            
            
cv2.putText(img,
            "Saturn",
             (700,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             ) 

cv2.putText(img,
            "Uranus",
             (970,150),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Neptune",
             (1080,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.imshow("Output",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)