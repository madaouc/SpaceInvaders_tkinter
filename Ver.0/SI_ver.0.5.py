from Tkinter import*
from time import*
from random import*


#time() -> system time
#Ref = Reference


"""-------------------------PIC-------------------------------------------"""

#Enemy Type1!!!!
def Enemy_1():
    t=int(time())       #get System time, smallest time unit 1s
    
    E1=[1,2]
    E1[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E1_1.PPM")
    E1[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E1_2.PPM")
    #SIZE 70*46 pix^2

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
    #SIZE 64*46 pix^2

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
    #SIZE 47*46 pix^2
    
    if(t%4==0 or t%4==1):         #Change the State per 2seconds
        stat=0
    else:
        stat=1
        
    return E3[stat]     #return corresponding Image


#Space Invader Beam!!!
def Beam():
    AT=[1,2]            #AT=Attack
    t=int(time()*10)
    if(t%4==0 or t%4==1):    #get System time & Change per 0.1s
        stat=0
    else:
        stat=1
    
    AT[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\A1.PPM")
    AT[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\A2.PPM")
    #SIZE 17*30 pix^2
    return AT[stat]

"""------------------------------PIC------------------------------------"""


def SpaceInvader():
    global Enemy,CoordX,CoordY,x,y,k,cv,B_AT,BeamBeam
    
    Type=[1,2,3]
    Type[0]=Enemy_1()
    Type[1]=Enemy_2()
    Type[2]=Enemy_3()

    Enemy=[[i for i in range(7)]for j in range(3)]
    for i in range(3):
        for j in range(7):
            Enemy[i][j]=Type[i]
    
    CoordX=[i for i in range(7)]        # Enemy's X coordinates
    CoordX[0]=x
    for i in range(1,7):
        CoordX[i]=CoordX[i-1]+80

    CoordY=[i for i in range(3)]        # Enemy's Y coordinates
    CoordY[0]=y
    for i in range(1,3):
        CoordY[i]=CoordY[i-1]-56

    BeamAttack()
    
    for i in range(3):          #draw Image
        for j in range(7):
            cv.create_image(CoordX[j],CoordY[i],image=Enemy[i][j])

    if(x+480+80>720):       #Enemy move left & right
        k=-1
    elif(x<80):
        k=1
    x=x+k*0.25
    
def BeamAttack():
    global BeamBeam,BeamAT,B_AT,AT_X,AT_Y
    
    if(B_AT==0):                    #BeamAT initialization
        for i in range(3):
            for j in range(7):
                BeamAT[i][j]="N"
        B_AT=1
    
    for i in range(3):
        for j in range(7):
            shoot=int(random()*1000000)%5000       #Attack probability 1/5000
            if(shoot==1 and BeamAT[i][j]=="N"):
                BeamAT[i][j]="Y"
                AT_X[i][j]=CoordX[j]
                AT_Y[i][j]=CoordY[i]
            if(BeamAT[i][j]=="Y"):
                BeamBeam[i][j]=Beam()
                cv.create_image(AT_X[i][j],AT_Y[i][j],image=BeamBeam[i][j])
                AT_Y[i][j]=AT_Y[i][j]+3
                if(AT_Y[i][j]>480+20):          #BeamAT reset
                    BeamAT[i][j]="N"

  
def rush():  
    global cv,x1,y1,SI,Enemy
    
    SpaceInvader()
    cv.after(10,rush)
    


root=Tk()

cv=Canvas(root,width=720,height=480,bg="black")

x=120       #Space Invaders' first Ref Coordinate
y=180
k=1         #parameter of func SpaceInvader()
x1=360
y1=30
B_AT=0      #parameter of func BeamAttack()
BeamBeam=[[i for i in range(7)]for j in range(3)]
BeamAT=[[i for i in range(7)]for j in range(3)]
AT_X=[[i for i in range(7)]for j in range(3)]
AT_Y=[[i for i in range(7)]for j in range(3)]

cv.pack()
rush()
print "B"
btn=Button(root,text="Quit",command=root.destroy)
btn.place(relx=.6,rely=0)

root.mainloop()
print"A"


