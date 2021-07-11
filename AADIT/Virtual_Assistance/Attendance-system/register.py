import cv2
import os
from django.conf import settings

path = os.path.join(settings.BASE_DIR, 'Training_images')
print(path)
#path = "Training_images"
#path = "E:\Minor\AADIT\Virtual_Assistance\Attendance-system\Training_images"
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    classNames.append(os.path.splitext(cl)[0])


name = input('Enter Name: ')


if name.title() not in classNames:
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Register")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Register", frame)

        k = cv2.waitKey(1)
        if k == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = f'./Training_images\{name}.jpg'
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))   

    cam.release()
    cv2.destroyAllWindows()
else:
    print('Already Register and open up the camera for attendence')