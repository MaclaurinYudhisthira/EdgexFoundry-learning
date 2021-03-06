import cv2
import time
import requests
import json

edgex_ip    = "localhost"
core_metadata = 59881
core_data = 59880
core_command = 59882 
device_rest = 59986

device_name="Camera-Device-1"
sensor_name="Camera"


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

# font
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)

# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2


def main():
    while True:
        _, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        total_people = 0

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            total_people +=1
        temp = 'Total people in image: ' + str(total_people)
        img = cv2.putText(img, temp, org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)


        print("Total people in image:", total_people)
        # cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        print("k:",k)

        print("Sending data to edgex...")
        url = f"http://{edgex_ip}:{device_rest}/api/v2/resource/{device_name}/{sensor_name}"
        payload=total_people
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
        print("Result of sending data: %s with message %s" % (response, response.text))

        if k==27:
            break


        time.sleep(1)

    cap.release()
    

    return total_people

if __name__=="__main__":
    main()