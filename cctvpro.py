
from tkinter import *
import cv2
import time
face_cascade=cv2.CascadeClassifier("facefile.xml")
vid = cv2.VideoCapture(0)

root=Tk()
root["bg"]="pink"

frm =Frame(root,width=600,height=400)
frm.place(x=400,y=80)

lbl=Label(frm,text="Smart CCTV Camera",font="arial 15 bold")
lbl.place(x=200,y=30)

def open():
    while True:
        ret,frame=vid.read()
        cv2.imshow("camera",frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    vid.release()
    cv2.distroyAllWindows()

btn=Button(frm,text="opencv",font="arial 10 bold",command=open)
btn.place(x=80,y=120)

def face():
    while True:
        ret,frame = vid.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
            cv2.imshow("camera",frame)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break
            vid.release()
            cv2.distroyAllWindows()

btn=Button(frm,text="Face Detection",font="arial 10 bold",command=face)
btn.place(x=430,y=120)

def main():
    cap=cv2.VideoCapture(0)
    start_time=time.time()
    while True:
        ret,frame =cap.read()
        cv2.imshow("camera",frame)
        if time.time()-start_time >=3:
            image=frame
            break
        if cv2.waitKey(1) & 0Xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    file_name=input("enter file name:")
    cv2.imwrite(file_name,image)

btn=Button(frm,text="Click Photo",font="arial 10 bold",command=main)
btn.place(x=80,y=260)

btn=Button(frm,text="Recording",font="arial 10 bold")
btn.place(x=430,y=260)

mainloop()