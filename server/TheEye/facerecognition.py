#face_recognition --show-distance true ./unknown ./known
import os,face_recognition
from pathlib import Path
import numpy as np,cv2
from PIL import Image,ImageDraw,ImageFont
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
known_classifier=os.path.join(BASE_DIR,'haarcascade_frontalface_default.xml')
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

# def passimage(image):
#         known_path=os.path.join(BASE_DIR,'known')
#         x=Image.open(image)
#         unknown_image=np.array(x)
#         unknown_image_encoding=face_recognition.face_encodings(unknown_image)[0]
#         wrong_image=face_recognition.load_image_file(os.path.join(BASE_DIR,'unknown/unknown.jpg'))
#         font_path=os.path.join(BASE_DIR,"SIXTY.TTF")
#         for root,dirs,files in os.walk(known_path):
#                 for i in range(len(files)):
#                         print(os.path.join(root,files[i]))
#                         known_image=face_recognition.load_image_file(os.path.join(root,"milliegang.jpg"))
#                         known_image_encoding=face_recognition.face_encodings(known_image)[0]
#                         results=face_recognition.compare_faces([unknown_image_encoding],known_image_encoding)
#                         print(face_recognition.face_locations(known_image))
#                         if results[0]:
#                             success_image=face_recognition.face_locations(unknown_image)
#                             length=len(files[i])-4
#                             for face in success_image:
#                                 print(files[i][:length])
#                                 top,right,bottom,left=face
#                                 face_image=unknown_image
#                                 pil_image=Image.fromarray(face_image)
#                                 draw=ImageDraw.Draw(pil_image)
#                                 draw.rectangle(((left,top),(right,bottom)),outline=(255,255,0))
#                                 textwidth,textheight=draw.textsize(files[i][:length])
#                                 font=ImageFont.truetype(font_path,60)
#                                 draw.text((left,bottom-textheight),files[i][:length],fill=(250,0,100),font=font)
#                                 worst_ra=np.array(pil_image)
#                                 print(worst_ra)
#                         else:
#                             pil_wrong_image=Image.fromarray(wrong_image)
#                             output_image=pil_wrong_image
# passimage(os.path.join(BASE_DIR,"unknown/pretty.jpg"))
