import cv2
from pyzbar.pyzbar import decode
import webbrowser
import tkinter as tk
from datetime import datetime
import numpy as np


def record_url(url):
    with open("urls.txt","r") as r:
        x=r.readlines()
        if url in x:
            pass
        else:
         with open("urls.txt","+a") as a:
          a.write(
              f"\n\n[{count}]=>{url}\t[{datetime.now().strftime('%Y-%m-%d %H:%M:%S %p')}]")
          a.close()



def open_win(url):
  x = webbrowser.open(
      f"{url}")
  record_url(url)
  root.destroy()
  
def close_win():
  root.destroy()
  
  
def resize_image():
    cap.set(4,1920)# width dimintions
    cap.set(4,1080) # hight dimintions



def tkinter_win(url):
    
    global root


    root=tk.Tk()
    w_width, w_height = 400, 200
    s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
    root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
    
    root.attributes("-topmost",True)
    
    root.resizable(0,0)
    
    
    root.overrideredirect(1)
    
    root.title("Go Now!!")
    
    root.iconbitmap("images//ico.ico")
    
    header_lbl=tk.Label(text="WebBrowser",font=("Impact",25),fg="black")
    
    header_lbl.pack()
    
    
    url_entry=tk.Entry(font=("arial",23),bd=1,relief="solid",justify="center")
    
    url_entry.pack(padx=10,pady=10)
    
    
    url_entry.insert(0,url)
    
    
    go_btn=tk.Button(text="❌",command=lambda :close_win(),font=("Impact",15),fg="red",relief="flat",bd=1,activebackground="white",activeforeground="red")
    
    go_btn.place(x=355,y=3)
    
    go_btn=tk.Button(text="GO!",command=lambda :open_win(url),font=("Impact",15),fg="white",width=15,bg="green",relief="flat",bd=1,activebackground="green",activeforeground="white")
    
    go_btn.pack(padx=20,pady=20)
    
    # enter action #


    root.bind("<Return>", lambda event:open_win(mydata))
    
    root.bind("<Escape>", lambda event:close_win())

    # enter action #
    
    
    root.mainloop()


face_classifier = cv2.CascadeClassifier("cascade//haarcascade_frontalface_default.xml")




 
     
cap = cv2.VideoCapture(0)  

resize_image()


background_image=cv2.imread("images//back.png")
count=0


def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(
        gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

while True:
    _, img = cap.read()
    
    
    background_image[180:180+480,55:55+640]=img 
    
    faces=detect_bounding_box(img)


    for barcode in decode(img):
         
         global mydata
         mydata = barcode.data.decode('utf-8')
         barcodeType = barcode.type
         (x, y, w, h) = barcode.rect
         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 128, 0), 2)
        #  text = f"{mydata}\tBarcode-Type= {barcodeType}"
        #  cv2.putText(img, text, (x, y - 10),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
         count+=1
        #  tkinter_win(mydata)
        
    


    cv2.imshow('BarCode Reader', background_image)
    cv2.waitKey(1)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
       break



cap.release
cv2.destroyAllWindows()
exit()

