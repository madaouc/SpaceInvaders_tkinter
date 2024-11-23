from Tkinter import*
from time import*

#time() -> system time

x=360
y=30
stat=1
t=time()
def Attack(stat):
    SI=[1,2]
    SI[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\A1.PPM")
    SI[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\A2.PPM")
    return SI[stat]
    
def rush():  
    global cv,x,y,SI,stat
    SI=Attack(stat)
    if(stat==0):
        stat=1
    else:
        stat=0
    
    y=y+5
    if(y>480):
        y=-10

    cv.move(Cir,3,3)
        
    cv.create_image(x,y,image=SI)
    
    cv.after(300,rush)
     
    


root=Tk()

#stat=1
cv=Canvas(root,width=720,height=480,bg="black")
cv.coords(720,480,0,0)
Cir=cv.create_oval(x,y,x+10,y+10)


cv.pack()
rush()

btn=Button(root,text="Quit",command=root.destroy)
btn.place(relx=.6,rely=0)

root.mainloop()
print"A"


