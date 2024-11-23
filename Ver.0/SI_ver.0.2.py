from Tkinter import*
from time import*

#time() -> system time

x=360
y=30



#Enemy Type1!!!!
def Enemy_1():
    t=int(time())       #get System time, smallest time unit 1s
    
    E1=[1,2]
    E1[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E1_1.PPM")
    E1[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E1_2.PPM")

    if(t%2==0):         #Change the State per second
        stat=0
    else:
        stat=1
        
    return E1[stat]     #return corresponding Image

#Enemy Type2!!!!
def Enemy_2():
    t=int(time())       #get System time, smallest time unit 1s
    
    E2=[1,2]
    E2[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E2_1.PPM")
    E2[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E2_2.PPM")

    if(t%2==0):         #Change the State per second
        stat=0
    else:
        stat=1
        
    return E2[stat]     #return corresponding Image


#Enemy Type3!!!!
def Enemy_3():
    t=int(time())       #get System time, smallest time unit 1s
    
    E3=[1,2]
    E3[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E3_1.PPM")
    E3[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E3_2.PPM")

    if(t%2==0):         #Change the State per second
        stat=0
    else:
        stat=1
        
    return E3[stat]     #return corresponding Image





#Space Invader's Attack Beam!!!
def Attack():
    SI=[1,2]

    if(int(time()*10)%2==0):    #get System time & Change per 0.1s
        stat=0
    else:
        stat=1
    
    SI[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\A1.PPM")
    SI[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\A2.PPM")
    return SI[stat]



    
def rush():  
    global cv,x,y,SI,E2,E3,E1,E2pi,L1,L2,L3,k

    k=k+1
    
    SI=Attack()
    cv.create_image(x,y,image=SI)

    L1=[i for i in range(7)]
    for i in range(7):
        L1[i]=Enemy_1()
    CoordX1=[Cx for Cx in range(7)]
    CoordX1[0]=120
    for Cx in range(1,7):
        CoordX1[Cx]=CoordX1[Cx-1]+80
    for i in range(7):
        cv.create_image(CoordX1[i],240,image=L1[i])
        
    L2=[i for i in range(7)]
    for i in range(7):
        L2[i]=Enemy_2()
    CoordX2=[Cx for Cx in range(7)]
    CoordX2[0]=120
    for Cx in range(1,7):
        CoordX2[Cx]=CoordX2[Cx-1]+80
    for i in range(7):
        cv.create_image(CoordX2[i],240-56,image=L2[i])

    L3=[i for i in range(7)]
    for i in range(7):
        L3[i]=Enemy_3()
    CoordX3=[Cx for Cx in range(7)]
    CoordX3[0]=120
    for Cx in range(1,7):
        CoordX3[Cx]=CoordX3[Cx-1]+80
    
    for i in range(7):
        cv.create_image(CoordX3[i],240-56*2,image=L3[i])

        
    
    E1=Enemy_1()
    E2=Enemy_2()
    E3=Enemy_3()
    
    y=y+5
    if(y>480):
        y=-10

    #cv.move(Cir,3,3)
        
    
    #cv.create_image(40,120,image=E2)
    #cv.create_image(200,120,image=E2)
    cv.after(10,rush)
    


root=Tk()

cv=Canvas(root,width=720,height=480,bg="black")

#Cir=cv.create_oval(x,y,x+10,y+10)
k=0

cv.pack()
rush()
print "B"
btn=Button(root,text="Quit",command=root.destroy)
btn.place(relx=.6,rely=0)

root.mainloop()
print"A"


