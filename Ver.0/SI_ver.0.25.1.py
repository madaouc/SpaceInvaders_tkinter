from Tkinter import*
from time import*

#time() -> system time

x1=360
y1=30



#Enemy Type1!!!!
def Enemy_1():
    t=int(time())       #get System time, smallest time unit 1s
    
    E1=[1,2]
    E1[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E1_1.PPM")
    E1[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E1_2.PPM")

    if(t%4==0 or t%4==1):         #Change the State per 2seconds
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

    if(t%4==0 or t%4==1):         #Change the State per 2seconds
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

    if(t%4==0 or t%4==1):         #Change the State per 2seconds
        stat=0
    else:
        stat=1
        
    return E3[stat]     #return corresponding Image

#Space Invader Beam!!!
def Beam():
    At=[1,2]
    t=int(time()*10)
    if(t%4==0 or t%4==1):    #get System time & Change per 0.1s
        stat=0
    else:
        stat=1
    
    At[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\A1.PPM")
    At[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\A2.PPM")
    return At[stat]



def SpaceInvader():
    global Enemy,CoordX,CoordY,x,y,k,cv
    
    Type=[1,2,3]
    Type[0]=Enemy_1()
    Type[1]=Enemy_2()
    Type[2]=Enemy_3()

    Enemy=[[i for i in range(7)]for j in range(3)]
    for j in range(3):
        for i in range(7):
            Enemy[j][i]=Type[j]
    
    CoordX=[i for i in range(7)]        # Enemy's X coordinates
    CoordX[0]=x
    for i in range(1,7):
        CoordX[i]=CoordX[i-1]+80

    CoordY=[i for i in range(3)]        # Enemy's Y coordinates
    CoordY[0]=y
    for i in range(1,3):
        CoordY[i]=CoordY[i-1]-56

    for j in range(3):          #draw Image
        for i in range(7):
            cv.create_image(CoordX[i],CoordY[j],image=Enemy[j][i])

    if(x+480+80>720):       #Enemy move left & right
        k=-1
    elif(x<80):
        k=1
    x=x+k*0.25
    

  
def rush():  
    global cv,x1,y1,SI,Enemy
    
    
    SI=Beam()
    cv.create_image(x1,y1,image=SI)
    y1=y1+3
    if(y1>480):
        y1=-10

    
    SpaceInvader()
    print CoordX[1]
    cv.after(10,rush)
    


root=Tk()

cv=Canvas(root,width=720,height=480,bg="black")

x=120
y=180
k=1
x1=360
y1=30

cv.pack()
rush()
print "B"
btn=Button(root,text="Quit",command=root.destroy)
btn.place(relx=.6,rely=0)

root.mainloop()
print"A"


