from tkinter import*
from time import*
from random import*
import winsound

#time() -> system time
#Ref = Reference

"""---------------------------Set_Global_Parameters----------------------"""
def GloPara():              
    global process #control the run down of the game
    process=0
    #------------------------For_Func_SpaceInvader--------------------------
    global x,y,k,E_ATed,ED_count
    x=120       #Space Invaders' first Ref Coordinate
    y=214
    k=1         #parameter for move left and right
    ED_count=0    #parameter to help the Invaders go down
    E_ATed=[[i for i in range(7)]for j in range(5)]  #show if the Enemy be Attacked
    for i in range(5):
        for j in range(7):
            E_ATed[i][j]="N"
    #========================For_Func_SpaceInvader==========================
    
    #------------------------For_Func_BeamAttack()----------------------------
    global BeamBeam,BeamAT,AT_X,AT_Y,BAT_count
    BeamBeam=[[i for i in range(7)]for j in range(5)]
    BeamAT=[[i for i in range(7)]for j in range(5)]     #show Beam shooting status
    for i in range(5):
        for j in range(7):
            BeamAT[i][j]="N"
 
    #when Attack draws,help to keep the boom Image for a while        
    BAT_count=[[i for i in range(7)]for j in range(5)]   
    for i in range(5):
        for j in range(7):
            BAT_count[i][j]=0
            
    AT_X=[[i for i in range(7)]for j in range(5)]       #Coordinate of Beam
    AT_Y=[[i for i in range(7)]for j in range(5)]
    #=========================For_Func_BeamAttack()==========================
    global pX,Shooting,B_X
    pX=360          #initial X coordinate of Player
    B_X=0
    Shooting="N"    #show if Player shoots

    global P_ATed,EB_count,PB_count
    EB_count=[[i for i in range(7)]for j in range(5)]   #Help to count time 
    for i in range(5):
        for j in range(7):
            EB_count[i][j]=0
    PB_count=0          #Help to count time
    P_ATed="N"          #show if Player be Attacked

    global score,stock
    score=0
    stock=3

    global B_Y
    B_Y=660         #initial Y of Bullet

    global HTP_count #parameter of How to Play
    HTP_count=0
    

"""=======================Set_Global_Parameters============================="""



"""-------------------------PIC_PlugIn_Func---------------------------------"""
#Enemy Type1 !!!
def Enemy_1():
    global Path         #Path way of folder
    t=int(time())       #get System time, smallest time unit 1s
    
    E1=[1,2]
    E1[0]=PhotoImage(file=Path+"\PY_Project\PIC\E1_1.PPM")
    E1[1]=PhotoImage(file=Path+"\PY_Project\PIC\E1_2.PPM")
    #SIZE 35*23 pix^2

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
    #SIZE 32*23 pix^2

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
    #SIZE 23.5*23 pix^2
    
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
    #SIZE 8.5*15 pix^2
    
    return AT[stat]     #return corresponding Image

def Player():
    global Path         #Path way of folder
    PL=PhotoImage(file=Path+"\PY_Project\PIC\Player.PPM")
    #SIZE 21.5*15 pix^2
    return PL

def CoverPIC():
    global Path         #Path way of folder
    CV=[1,2]            #AT=Attack
    t=int(time()*10)
    if(t%20==17 or t%20==18 or t%20==19):    #get System time & Change         stat=1
        stat=1
    else:
        stat=0
    
    CV[0]=PhotoImage(file=Path+"\PY_Project\PIC\Cover_1.PPM")
    CV[1]=PhotoImage(file=Path+"\PY_Project\PIC\Cover_2.PPM")
    
    return CV[stat]     #return corresponding Image
    
def HowToPlay():
    global Path,HTP_count        #Path way of folder
    HTP=[1,2,3,4]            #AT=Attack
    
    sleep(1.2)
    HTP[0]=PhotoImage(file=Path+"\PY_Project\PIC\HTP_1.PPM")
    HTP[1]=PhotoImage(file=Path+"\PY_Project\PIC\HTP_2.PPM")
    HTP[2]=PhotoImage(file=Path+"\PY_Project\PIC\HTP_3.PPM")
    HTP[3]=PhotoImage(file=Path+"\PY_Project\PIC\HTP_4.PPM")
    if(HTP_count%6==0 or HTP_count%6==2 or HTP_count%6==4):
        HTP_count=HTP_count+1
        return HTP[0]
    elif(HTP_count%6==1):
        HTP_count=HTP_count+1
        return HTP[1]
    elif(HTP_count%6==3):
        HTP_count=HTP_count+1
        return HTP[2]
    elif(HTP_count%6==5):
        HTP_count=6
        return HTP[3]
    
"""==========================PIC_PlugIn_Func==============================="""

"""-----------------------Button_Pressed----------------------------------"""
def MoveL(event):
    global pX
    if(pX>60):
        pX=pX-5
    

def MoveR(event):
    global pX
    if(pX<720-60):
        pX=pX+5

def Shoot(event):
    global Shooting,B_Y,Bull,B_X,Path
    if(Shooting=="N"):      #every time can only shoot One Bullet
        B_X=pX              #B_X -> Bullet's x coord
        B_Y=600-60
        Shooting="Y"#Shooting Lock
        #Play sound, BS=Bullet Shoot
        BS=Path+"\PY_Project\Sound\BulletShot.wav"
        #the formate should be BS=r"Path way"
        #But why could it run without the "r"??
        winsound.PlaySound(BS,winsound.SND_ASYNC)

def NextProcess(event):
    global process,Cover,HTP
    if(process==0):
        process=1
        Cover=PhotoImage(file=Path+"\PY_Project\PIC\Black.PPM")
        cv.create_image(360,315,image=Cover)
    elif(process==1):
        process=2
        HTP=PhotoImage(file=Path+"\PY_Project\PIC\Black.PPM")
        cv.create_image(360,315,image=HTP)
        

"""======================Button_Pressed================================="""

"""--------------------------------------------------------------------"""
def SpaceInvader():
    global cv,x,y,k
    global Enemy,CoordX,CoordY,EB_count,score,Path,startTime,ED_count
    
    Type=[1,2,3,4,5]
    Type[0]=Enemy_1()
    Type[1]=Enemy_1()
    Type[2]=Enemy_2()
    Type[3]=Enemy_2()
    Type[4]=Enemy_3()

    Enemy=[[i for i in range(7)]for j in range(5)]
    for i in range(5):
        for j in range(7):
            Enemy[i][j]=Type[i]         #Define Enemy Type
    
    CoordX=[i for i in range(7)]        #Enemy's X coordinates
    CoordX[0]=x
    for i in range(1,7):
        CoordX[i]=CoordX[i-1]+80

    CoordY=[i for i in range(5)]        #Enemy's Y coordinates
    CoordY[0]=y
    for i in range(1,5):
        CoordY[i]=CoordY[i-1]-46

    BeamAttack()
    
    for i in range(5):          #draw Space Invaders
        for j in range(7):
            if(E_ATed[i][j]=="N"):
                cv.create_image(CoordX[j],CoordY[i],image=Enemy[i][j])
            #show the Boom Image after attacked
            elif(EB_count[i][j]<10):    #keep the Image showing for a while
                Enemy[i][j]=PhotoImage(file=Path+"\PY_Project\PIC\Boom.PPM")
                cv.create_image(CoordX[j],CoordY[i],image=Enemy[i][j])
                score=score+1+2*i
                EB_count[i][j]=EB_count[i][j]+1
                if(EB_count[i][j]==1):
                        #Play sound, EB=Enemy Booms
                        EB=Path+"\PY_Project\Sound\Disappear.wav"
                        #the formate should be BS=r"Path way"
                        #But why could it run without the "r"??
                        winsound.PlaySound(EB,winsound.SND_ASYNC)
                
            
    if(x+480+80>720):       #Enemy move left & right
        k=-1
    elif(x<80):
        k=1
    x=x+k*0.25
    if(int(time()-startTime)%20==0):        #go down every 20s
        if(ED_count==0):
            y=y+46
            ED_count=1
    else:
        ED_count=0
    

   
def BeamAttack():
    global Path
    global BeamBeam,BeamAT,AT_X,AT_Y,BAT_count
    
    for i in range(5):
        for j in range(7):
            if(E_ATed[i][j]=="N"):
                shoot=int(random()*1000000)%1000     #Attack probability 1/1000
                if(shoot==1 and BeamAT[i][j]=="N"):
                    BeamAT[i][j]="Y"
                    AT_X[i][j]=CoordX[j]
                    AT_Y[i][j]=CoordY[i]
                elif(BeamAT[i][j]=="Y"):
                    BeamBeam[i][j]=Beam()
                    cv.create_image(AT_X[i][j],AT_Y[i][j],image=BeamBeam[i][j])
                    AT_Y[i][j]=AT_Y[i][j]+0.5
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
        cv.create_image(pX,600-60,image=Def)
        Shoot_Bullet()
    elif(PB_count<4):   #keep showing the image for a while
        Def=PhotoImage(file=Path+"\PY_Project\PIC\Player_D.PPM")
        cv.create_image(pX,600-60-1.5,image=Def)
        PB_count=PB_count+1
        stock=stock-.25
        if(PB_count==1):
                #Play sound, PB=Player Booms
                PB=Path+"\PY_Project\Sound\Boom.wav"
                #the formate should be BS=r"Path way"
                #But why could it run without the "r"??
                winsound.PlaySound(PB,winsound.SND_ASYNC)
    else:
        sleep(2.5)
        PB_count=0
        P_ATed="N"

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
    E_Width=[35,35,32,32,23.5]      #the height of all Enemies is 28
    for i in range(5):
        for j in range(7):
            if(E_ATed[i][j]=="N"):
                #Bullet's lenght is 15, width is 2.5
                if(B_Y-7.5<=CoordY[i]+14 and B_Y+7.5>=CoordY[i]-14):        
                    if(B_X-1<=CoordX[j]+E_Width[i]/2.0 and B_X+1>CoordX[j]-E_Width[i]/2.0):
                        E_ATed[i][j]="Y"
                        B_Y=-30         #B_Y<-15 -> Shooting=>"N"
    
            if(P_ATed=="N"):
                #AT Size 8.5*15, Player Size 21.5*15
                if(AT_Y[i][j]+7.5>=540-7.5 and AT_Y[i][j]-7.5<=540+7.5):
                    if(AT_X[i][j]-4.25<=pX+21.5/2.0 and AT_X[i][j]+4.25>=pX-21.5/2.0):
                        P_ATed="Y"
                        AT_Y[i][j]=700
            if(BeamAT[i][j]=="Y" and Shooting=="Y"):
                #AT Size 8.5*15, Bullet Size 2.5*15
                if(AT_Y[i][j]+7.5>=B_Y-7.5 and AT_Y[i][j]-7.5<=B_Y+7.5):
                    if(AT_X[i][j]-4.25<=B_X+1.25 and AT_X[i][j]+4.25>=B_X-1.25):
                        BeamAT[i][j]="D"
                        B_Y=-30
    
            

"""---------------------------------------------------------------------"""                 
def ifGameOver():
    global E_ATed,CoordY,stock
    sta=1
    if(stock>0):
        for i in range(5):
            for j in range(7):
                if(E_ATed[i][j]=="N" and CoordY[i]>540-21.5):
                    sta=sta*0
    else:
        sta=0
    return sta

def GameOver():
    global Path,GameO
    GameO=PhotoImage(file=Path+"\PY_Project\PIC\GameOver.PPM")
    cv.create_image(360,315,image=GameO)


def ifWin():
    global E_ATed
    sta=0
    for i in range(5):
        for j in range(7):
            if(E_ATed[i][j]=="N"):
                sta=sta+1          #count How many Enemies left
    return sta

def YouWin():
    global Path,YouW
    YouW=PhotoImage(file=Path+"\PY_Project\PIC\Win.PPM")
    cv.create_image(360,315,image=YouW)
    
def printStock():
    global Path,stock,Pstock
    Pstock=PhotoImage(file=Path+"\PY_Project\PIC\stock"+str(int(stock))+".PPM")
    cv.create_image(60,600,image=Pstock)

      
def rush():  
    global cv,stock,score,process,startTime
    global Cover,HTP,Warn

    if(process==0):
        Cover=CoverPIC()
        cv.create_image(360,315,image=Cover)
    elif(process==1):
        HTP=HowToPlay()
        cv.create_image(360,315,image=HTP)
    elif(process<3):
        Warn=PhotoImage(file=Path+"\PY_Project\PIC\Warning.PPM")
        cv.create_image(360,315,image=Warn)
        process=process+.05     #the final value will be 3.05
    elif(process<4):
        Warn=PhotoImage(file=Path+"\PY_Project\PIC\Black.PPM")
        cv.create_image(360,315,image=Warn)
        process=4
        startTime=int(time())  #reset the Start Time of the Game
    elif(process==4):
        SpaceInvader()
        Play()
        AT_Detect()
        printStock()
        
        ifGameO=ifGameOver()
        if(ifGameO==0):
            process=5
        ifW=ifWin()
        if(ifW==0):
            process=6
    elif(process==5):
        SpaceInvader()
        GameOver()
    elif(process==6):
        SpaceInvader()
        YouWin()
        Play()
    
    cv.after(10,rush)

   



def main():
    global Path,cv,startTime
    #Path="C:\Users\user\Desktop"
    Path="C:"
    root=Tk()
    startTime=int(time())
    
    cv=Canvas(root,width=720,height=630,bg="black")

    GloPara()

    cv.pack()
    rush()
    btn=Button(root,text="Quit",command=root.destroy)
    btn.place(relx=.95,rely=0)

    root.bind("<Left>",MoveL)
    root.bind("<Right>",MoveR)
    root.bind("<space>",Shoot)
    root.bind("<Return>",NextProcess)


    root.mainloop()

main()



