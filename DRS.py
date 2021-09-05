import tkinter
from tkinter.constants import ANCHOR
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils

stream = cv2.VideoCapture("clip.mp4")

flag = True

def play(Speed):
    global flag
    print(f"you clicked on play. Speed is{Speed}")
    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + Speed)
    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=ScreenWith, height= ScreenHeight)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag



def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("D:\pythonUniverse\galaxiOfProgrammingHeros\pythonProject\DRS\pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=ScreenWith, height= ScreenHeight)
    frame = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.Image= frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)
    # 2. Wait for 1 second
    time.sleep(1.5)
    # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("D:\pythonUniverse\galaxiOfProgrammingHeros\pythonProject\DRS\sponsor.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=ScreenWith, height= ScreenHeight)
    frame = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.Image= frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)
    # 4. Wait for 1.5 second
    time.sleep(2.5)
    # 5. Display out/notout image
    if decision == 'out':
        decisionIng = "out.png"
    else:
        decisionIng = "not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionIng),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=ScreenWith, height= ScreenHeight)
    frame = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.Image= frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)



def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is Out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not Out")


# Width and height of our main screen
ScreenWith = 650
ScreenHeight = 365

# Tkinter gui starts here
window = tkinter.Tk()
window.title("my Third Umpire Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("D:\pythonUniverse\galaxiOfProgrammingHeros\pythonProject\DRS\welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width = ScreenWith, height = ScreenHeight)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
imageOnLineCanvas = canvas.create_image(0, 0, ancho = tkinter.NW, image = photo)
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)", width= 50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow )", width= 50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="next (slow) >>", width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="next (fast ) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()

btn= tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()

window.mainloop()