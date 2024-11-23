# -*- coding: cp936 -*-
from Tkinter import *

speed = 5
x = 20
y = 10
statex = 1
statey = 1
xlen = 300
ylen = 200

def speedUp():   #按了+以后的反应
    global speed,label,win
    speed = speed + 1
    label = Label(win, text = "Speed = "+str(speed))
    label.place(relx = 0.60, rely = 0)

def speedDown():   #按了-以后的反应
    global speed,label,win
    if speed >= 1:
        speed = speed - 1
    else:
        speed = 0
    label = Label(win, text = "Speed = "+str(speed))
    label.place(relx = 0.60, rely = 0)

def refresh():   #更新球的位置
    global cv,ball,x,y,statex,statey
    x = x + speed*statex
    y = y + speed*statey
    if(x>=xlen):
        statex = -1
    if(x<=0):
        statex = 1
    if(y>=ylen):
        statey = -1
    if(y<=0):
        statey = 1
    cv.coords(ball,x,y,x+10,y+10)
    cv.after(10,refresh)

win = Tk()
#win.geometry(str(xlen)+'x'+str(ylen))

cv = Canvas(win,width = xlen-10,height = ylen-10,bg='white')
ball = cv.create_oval(x,y,x+10,y+10)
cv.pack(fill='both',expand='yes')
refresh()

label = Label(win, text = "Speed = "+str(speed))
label.place(relx = 0.60, rely = 0)
    
btn = Button(win,text='+',width = 5,height= 1,command = speedUp)
btn.place(relx=0.85,rely=0)

btn = Button(win,text='-',width = 5,height= 1,command = speedDown)
btn.place(relx=0.85,rely=1-0.15)

win.mainloop()

