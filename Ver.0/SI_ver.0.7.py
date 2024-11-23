from Tkinter import*
from time import*
from random import*


#time() -> system time
#Ref = Reference

def GloPara():              #set Global Parameter of functions
    #------------------------Func_SpaceInvader--------------------------
    global x,y,k,E_ATed
    x=120       #Space Invaders' first Ref Coordinate
    y=180
    k=1         #parameter of func SpaceInvader()

    E_ATed=[[i for i in range(7)]for j in range(3)]  #detect if the enemy be attacked
    for i in range(3):
        for j in range(7):
            E_ATed[i][j]="N"
    
    

    #========================Func_SpaceInvader==========================
    
    #------------------------Func_BeamAttack()----------------------------
    global BeamBeam,BeamAT,AT_X,AT_Y
    BeamBeam=[[i for i in range(7)]for j in range(3)]
    BeamAT=[[i for i in range(7)]for j in range(3)]
    for i in range(3):
        for j in range(7):
            BeamAT[i][j]="N"

    AT_X=[[i for i in range(7)]for j in range(3)]
    AT_Y=[[i for i in range(7)]for j in range(3)]
    #=========================Func_BeamAttack()==========================
    global pX,Shooting
    pX=360
    Shooting="N"



"""-------------------------PIC_PlugIn_Func---------------------------------"""

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

def Player():
    PL=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\Player.PPM")
    #SIZE 43*30 pix^2
    return PL

"""==========================PIC_PlugIn_Func==============================="""

"""-----------------------Button_Pressed----------------------------------"""
def MoveL(event):
    global pX
    pX=pX-5
    

def MoveR(event):
    global pX
    pX=pX+5

def Shoot(event):
    global Shooting,B_Y,Bull
    print Shooting,
    if(Shooting=="N"):      #every time can only shoot one bullet
        B_X=pX              #B_X -> Bullet's x coord
        B_Y=630-60
        Bull=cv.create_line(B_X,B_Y-15,B_X,B_Y+15,width=5,dash=15,fill="white")
        Shooting="Y"
    print Shooting
"""======================Button_Pressed================================="""




def SpaceInvader():
    global cv,x,y,k,Enemy,CoordX,CoordY
    
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
    if(k==-1):
        E_ATed[1][1]="Y"
    
    for i in range(3):          #draw Image
        for j in range(7):
            if(E_ATed[i][j]=="N"):
                cv.create_image(CoordX[j],CoordY[i],image=Enemy[i][j])
            """else:
                Enemy[i][j]=ATed()"""

    if(x+480+80>720):       #Enemy move left & right
        k=-1
    elif(x<80):
        k=1
    x=x+k*0.25

    
def BeamAttack():
    global BeamBeam,BeamAT,AT_X,AT_Y
    
    for i in range(3):
        for j in range(7):
            shoot=int(random()*1000000)%3000       #Attack probability 1/5000
            if(shoot==1 and BeamAT[i][j]=="N"):
                BeamAT[i][j]="Y"
                AT_X[i][j]=CoordX[j]
                AT_Y[i][j]=CoordY[i]
            if(BeamAT[i][j]=="Y"):
                BeamBeam[i][j]=Beam()
                cv.create_image(AT_X[i][j],AT_Y[i][j],image=BeamBeam[i][j])
                AT_Y[i][j]=AT_Y[i][j]+3
                if(AT_Y[i][j]>630+20):          #BeamAT reset
                    BeamAT[i][j]="N"


def Play():
    global cv,Def
    Def=Player()
    cv.create_image(pX,630-60,image=Def)
    Shoot_Bullet()

def Shoot_Bullet():
    global Shooting,B_Y
    if(Shooting=="Y" and B_Y>-15):
        cv.move(Bull,0,-5)
        B_Y=B_Y-5
    else:
        Shooting="N"
    
    

  
def rush():  
    global cv,x1,y1,SI,Enemy
    
    SpaceInvader()
    Play()
    cv.after(10,rush)
    




root=Tk()

cv=Canvas(root,width=720,height=630,bg="black")

GloPara()

cv.pack()
rush()
btn=Button(root,text="Quit",command=root.destroy)
btn.place(relx=.95,rely=0)

root.bind("<Left>",MoveL)
root.bind("<Right>",MoveR)
root.bind("<space>",Shoot)

root.mainloop()


