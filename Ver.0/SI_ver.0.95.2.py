from Tkinter import*
from time import*
from random import*


#time() -> system time
#Ref = Reference

"""---------------------------Set_Global_Parameters----------------------"""
def GloPara():              
    #------------------------For_Func_SpaceInvader--------------------------
    global x,y,k,E_ATed
    x=120       #Space Invaders' first Ref Coordinate
    y=180
    k=1         #parameter for move left and right

    E_ATed=[[i for i in range(7)]for j in range(3)]  #show if the Enemy be Attacked
    for i in range(3):
        for j in range(7):
            E_ATed[i][j]="N"
    #========================For_Func_SpaceInvader==========================
    
    #------------------------For_Func_BeamAttack()----------------------------
    global BeamBeam,BeamAT,AT_X,AT_Y,BAT_count
    BeamBeam=[[i for i in range(7)]for j in range(3)]
    BeamAT=[[i for i in range(7)]for j in range(3)]     #show Beam shooting status
    for i in range(3):
        for j in range(7):
            BeamAT[i][j]="N"
 
    #when Attack draws,help to keep the boom Image for a while        
    BAT_count=[[i for i in range(7)]for j in range(3)]   
    for i in range(3):
        for j in range(7):
            BAT_count[i][j]=0
            
    AT_X=[[i for i in range(7)]for j in range(3)]       #Coordinate of Beam
    AT_Y=[[i for i in range(7)]for j in range(3)]
    #=========================For_Func_BeamAttack()==========================
    global pX,Shooting
    pX=360          #initial X coordinate of Player
    Shooting="N"    #show if Player shoots

    global P_ATed,EB_count,PB_count
    EB_count=[[i for i in range(7)]for j in range(3)]   #Help to count time 
    for i in range(3):
        for j in range(7):
            EB_count[i][j]=0
    PB_count=0          #Help to count time
    P_ATed="N"          #show if Player be Attacked

    global score,stock
    score=0
    stock=3

    global B_Y
    B_Y=660         #initial Y of Bullet

"""=======================Set_Global_Parameters============================="""



"""-------------------------PIC_PlugIn_Func---------------------------------"""
#Enemy Type1 !!!
def Enemy_1():
    global Path         #Path way of folder
    t=int(time())       #get System time, smallest time unit 1s
    
    E1=[1,2]
    E1[0]=PhotoImage(file=Path+"\PY_Project\PIC\E1_1.PPM")
    E1[1]=PhotoImage(file=Path+"\PY_Project\PIC\E1_2.PPM")
    #SIZE 70*46 pix^2

    if(t%4==0 or t%4==1):         #Change the State per 2seconds
        stat=0
    else:
        stat=1
        
    return E1[stat]     #return corresponding Image

#Enemy Type2 !!!
def Enemy_2():
    global Path         #Path way of folder
    t=int(time())       #get System time, smallest time unit 1s
    
    E2=[1,2]
    E2[0]=PhotoImage(file=Path+"\PY_Project\PIC\E2_1.PPM")
    E2[1]=PhotoImage(file=Path+"\PY_Project\PIC\E2_2.PPM")
    #SIZE 64*46 pix^2

    if(t%4==0 or t%4==1):         #Change the State per 2seconds
        stat=0
    else:
        stat=1
        
    return E2[stat]     #return corresponding Image


#Enemy Type3 !!!
def Enemy_3():
    global Path         #Path way of folder
    t=int(time())       #get System time, smallest time unit 1s
    
    E3=[1,2]
    E3[0]=PhotoImage(file=Path+"\PY_Project\PIC\E3_1.PPM")
    E3[1]=PhotoImage(file=Path+"\PY_Project\PIC\E3_2.PPM")
    #SIZE 47*46 pix^2
    
    if(t%4==0 or t%4==1):         #Change the State per 2seconds
        stat=0
    else:
        stat=1
        
    return E3[stat]     #return corresponding Image


#Space Invader Beam!!!
def Beam():
    global Path         #Path way of folder
    AT=[1,2]            #AT=Attack
    t=int(time()*10)
    if(t%4==0 or t%4==1):    #get System time & Change per 0.2s
        stat=0
    else:
        stat=1
    
    AT[0]=PhotoImage(file=Path+"\PY_Project\PIC\A1.PPM")
    AT[1]=PhotoImage(file=Path+"\PY_Project\PIC\A2.PPM")
    #SIZE 17*30 pix^2
    
    return AT[stat]     #return corresponding Image

def Player():
    global Path         #Path way of folder
    PL=PhotoImage(file=Path+"\PY_Project\PIC\Player.PPM")
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
    global Shooting,B_Y,Bull,B_X
    if(Shooting=="N"):      #every time can only shoot One Bullet
        B_X=pX              #B_X -> Bullet's x coord
        B_Y=630-60
        Shooting="Y"        #Shooting Lock
"""======================Button_Pressed================================="""

"""--------------------------------------------------------------------"""
def SpaceInvader():
    global cv,x,y,k
    global Enemy,CoordX,CoordY,EB_count,score,Path
    
    Type=[1,2,3]
    Type[0]=Enemy_1()
    Type[1]=Enemy_2()
    Type[2]=Enemy_3()

    Enemy=[[i for i in range(7)]for j in range(3)]
    for i in range(3):
        for j in range(7):
            Enemy[i][j]=Type[i]         #Define Enemy Type
    
    CoordX=[i for i in range(7)]        #Enemy's X coordinates
    CoordX[0]=x
    for i in range(1,7):
        CoordX[i]=CoordX[i-1]+80

    CoordY=[i for i in range(3)]        #Enemy's Y coordinates
    CoordY[0]=y
    for i in range(1,3):
        CoordY[i]=CoordY[i-1]-56

    BeamAttack()
    
    for i in range(3):          #draw Space Invaders
        for j in range(7):
            if(E_ATed[i][j]=="N"):
                cv.create_image(CoordX[j],CoordY[i],image=Enemy[i][j])
            #show the Boom Image after attacked
            elif(EB_count[i][j]<10):    #keep the Image showing for a while
                Enemy[i][j]=PhotoImage(file=Path+"\PY_Project\PIC\Boom.PPM")
                cv.create_image(CoordX[j],CoordY[i],image=Enemy[i][j])
                score=score+10+20*i
                EB_count[i][j]=EB_count[i][j]+1
            
    if(x+480+80>720):       #Enemy move left & right
        k=-1
    elif(x<80):
        k=1
    x=x+k*0.25

   
def BeamAttack():
    global Path
    global BeamBeam,BeamAT,AT_X,AT_Y,BAT_count
    
    for i in range(3):
        for j in range(7):
            if(E_ATed[i][j]=="N"):
                shoot=int(random()*1000000)%2000     #Attack probability 1/2000
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
                if(BeamAT[i][j]=="D"):
                    BeamBeam[i][j]=PhotoImage(file=Path+"\PY_Project\PIC\Draw.PPM")
                    cv.create_image(AT_X[i][j],AT_Y[i][j],image=BeamBeam[i][j])
                    BAT_count[i][j]=BAT_count[i][j]+1
                    if(BAT_count[i][j]>4):
                        BAT_count[i][j]=0
                        AT_Y[i][j]=700
            elif(BeamAT[i][j]=="Y" and AT_Y[i][j]<660):
                BeamBeam[i][j]=Beam()
                cv.create_image(AT_X[i][j],AT_Y[i][j],image=BeamBeam[i][j])
                AT_Y[i][j]=AT_Y[i][j]+3
                
"""----------------------------------------------------------------------"""

def Play():
    global cv,Def,P_ATed,PB_count,stock,Path
    if(P_ATed=="N"):
        Def=Player()
        cv.create_image(pX,630-60,image=Def)
        Shoot_Bullet()
    elif(PB_count<4):   #keep showing the image for a while
        Def=PhotoImage(file=Path+"\PY_Project\PIC\Player_D.PPM")
        cv.create_image(pX,630-60-3,image=Def)
        PB_count=PB_count+1
        stock=stock-.25
    else:
        sleep(2.5)
        PB_count=0
        P_ATed="N"
        print stock

def Shoot_Bullet():
    global Shooting,B_Y,Bull,Path
    if(Shooting=="Y"):
        Bull=PhotoImage(file=Path+"\PY_Project\PIC\Bullet.PPM")
        cv.create_image(B_X,B_Y,image=Bull)
        if(B_Y>-15):        
            B_Y=B_Y-5       #keep the Bullet moving upward
        else:
            Shooting="N"    #reset the status when the Bullet is out of screen

"""---------------------------------------------------------------------"""
def AT_Detect():
    global CoordX,CoordY,AT_X,AT_Y,E_ATed
    global pX,B_X,B_Y,P_ATed,Shooting
    global cv,Path,Draw
    E_Width=[70,64,47]      #the height of all Enemies is 56
    for i in range(3):
        for j in range(7):
            if(E_ATed[i][j]=="N"):
                #Bullet's lenght is 30, width is 5
                if(B_Y-15<=CoordY[i]+28 and B_Y+15>=CoordY[i]-28):        
                    if(B_X-2<=CoordX[j]+E_Width[i]/2.0 and B_X+2>CoordX[j]-E_Width[i]/2.0):
                        E_ATed[i][j]="Y"
                        B_Y=-30         #B_Y<-15 -> Shooting=>"N"
                        print "Destroy Enemy"
    
            if(P_ATed=="N"):
                #AT Size 17*30, Player Size 43*30
                if(AT_Y[i][j]+15>=570-15 and AT_Y[i][j]-15<=570+15):
                    if(AT_X[i][j]-8.5<=pX+43/2.0 and AT_X[i][j]+8.5>=pX-43/2.0):
                        P_ATed="Y"
                        AT_Y[i][j]=700
                        print "Destroy Yourself"
            if(BeamAT[i][j]=="Y" and Shooting=="Y"):
                #AT Size 17*30, Bullet Size 5*30
                if(AT_Y[i][j]+15>=B_Y-15 and AT_Y[i][j]-15<=B_Y+15):
                    if(AT_X[i][j]-8.5<=B_X+2.5 and AT_X[i][j]+8.5>=B_X-2.5):
                        BeamAT[i][j]="D"
                        B_Y=-30
                        #AT_Y[i][j]=700
                        print "Draw"
    
            

"""---------------------------------------------------------------------"""                 
 
      
def rush():  
    global cv,x1,y1,SI,Enemy
    SpaceInvader()
    Play()
    AT_Detect()
    cv.after(10,rush)
    

global Path
Path="C:\Users\user\Desktop"
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


