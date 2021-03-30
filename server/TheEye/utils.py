import cv2 ,pymongo
import os,face_recognition,numpy as np
from pathlib import Path
from io import BytesIO
from PIL import Image,ImageDraw,ImageFont
from pymongo import MongoClient

try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

# database
db = conn.TheEye
# Created or Switched to collection names: my_gfg_collection
collection = db.InfoDB_lead
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
known_classifier=os.path.join(BASE_DIR,'haarcascade_frontalface_default.xml')
l=[]
truevalues=[]
def get_filtered_images(image,action):
    img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    if action=='NO_FILTER':
        img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        filtered=img
    elif action=='COLORIZED':
        save_path=os.path.join(BASE_DIR,'unknown/personimg.jpg')
        known_path=os.path.join(BASE_DIR,'known')
        face_cascade=cv2.CascadeClassifier(known_classifier)
        cap=cv2.VideoCapture(0)
        while cap.isOpened():
            ref,frame=cap.read()
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(frame,1.1,4)
            cv2.imshow("image",frame)
            cv2.imwrite(save_path,gray)
            if cv2.waitKey(1) & 0xFF==ord("q"):
                break
        imageofbill=face_recognition.load_image_file(save_path)
        billfaceencoding=face_recognition.face_encodings(imageofbill)[0]
        for root,dirs,files in os.walk(known_path):
            for i in range(len(files)):
                length=len(files[i])-4
                known_images=face_recognition.load_image_file(os.path.join(root,files[i]))
                knownimagesencodings=face_recognition.face_encodings(known_images)[0]
                results=face_recognition.compare_faces([knownimagesencodings],billfaceencoding)
                if results[0]:
                    img=cv2.imread(os.path.join(root,files[i]))
                    cv2.putText(img,files[i][:length],(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3,cv2.LINE_AA)
                    cv2.imshow("images",img)
                else:
                    continue
        cv2.waitKey()
        cv2.destroyAllWindows()

        filtered=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    elif action=='GRAYSCALE':
        known_path=os.path.join(BASE_DIR,'known')
        unknown_image=image
        unknown_image_encoding=face_recognition.face_encodings(unknown_image)[0]
        wrong_image=face_recognition.load_image_file(os.path.join(BASE_DIR,'unknown/unknown.jpg'))
        font_path=os.path.join(BASE_DIR,"SIXTY.TTF")
        for root,dirs,files in os.walk(known_path):
            for i in range(len(files)):
                known_image=face_recognition.load_image_file(os.path.join(root,files[i]))
                known_image_encoding=face_recognition.face_encodings(known_image)[0]
                results=face_recognition.compare_faces([unknown_image_encoding],known_image_encoding)
                if results[0]:
                    success_image=face_recognition.face_locations(unknown_image)
                    length=len(files[i])-4
                    for face in success_image:
                        print(files[i][:length])
                        top,right,bottom,left=face
                        face_image=unknown_image
                        pil_image=Image.fromarray(face_image)
                        draw=ImageDraw.Draw(pil_image)
                        draw.rectangle(((left,top),(right,bottom)),outline=(255,255,0))
                        textwidth,textheight=draw.textsize(files[i][:length])
                        font=ImageFont.truetype(font_path,60)
                        draw.text((left,bottom-textheight),files[i][:length],fill=(250,0,100),font=font)
                        output_image=np.array(pil_image)
                        emp_rec1 = {
                            "name":files[i][:length],
                            }
                        cursor=collection.find()
                        for record in cursor:
                            l.append(record["name"])
                        for i in range(len(l)):
                            truevalues.append(l[i]==emp_rec1["name"])
                        if True in truevalues:
                            print(l)
                            print(truevalues)
                            print("YOUR NAME HAS ALREADY EXISTED")
                            l.clear()
                            truevalues.clear()
                        else:
                            rec_id1=collection.insert_one(emp_rec1)
                            print(rec_id1)
                            print("NEW NAME HAS BEEN ADDED")
                else:
                    continue
        filtered=output_image
    elif action=='BLURRED':
        width,height=img.shape[:2]
        if width>50:
            k=(50,50)
        elif width>200 and width<=500:
            k=(25,25)
        else:
            k=(10,10)
        blur=cv2.blur(img,k)
        filtered=cv2.cvtColor(blur,cv2.COLOR_BGR2RGB)
    elif action=='BINARY':
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        _,filtered=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    elif action=='INVERT':
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        _,filtered=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
        filtered=cv2.bitwise_not(img)
    elif action=='DELETE':
        pass
    return filtered