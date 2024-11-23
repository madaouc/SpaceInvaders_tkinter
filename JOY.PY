#Just for Fun!!

from tkinter import*
from time import*
def Enemy_2():
    t=int(time())       #get System time, smallest time unit 1s
    
    E2=[1,2]
    #E2[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E2_1.PPM")
    #E2[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E2_2.PPM")
    E2[0]=PhotoImage(file="C:\PY_Project\PIC\E2_1.PPM")
    E2[1]=PhotoImage(file="C:\PY_Project\PIC\E2_2.PPM")
    #SIZE 64*46 pix^2

    if(t%4==0 or t%4==1):         #Change the State per 2seconds
        stat=0
    else:
        stat=1
        
    return E2[stat]     #return corresponding Image

def Enemy_2pi():
    t=int(time())       #get System time, smallest time unit 1s
    
    E2=[1,2]
    #E2[0]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E2_1.PPM")
    #E2[1]=PhotoImage(file="C:\Users\user\Desktop\PY_Project\PIC\E2_2.PPM")
    E2[0]=PhotoImage(file="C:\PY_Project\PIC\E2_1.PPM")
    E2[1]=PhotoImage(file="C:\PY_Project\PIC\E2_2.PPM")
    #SIZE 64*46 pix^2

    if(t%4==0 or t%4==1):         #Change the State per 2seconds
        stat=1
    else:
        stat=0
        
    return E2[stat]     #return corresponding Image

def rush():
    global SI,cv
    SI=[[i for i in range(14)]for j in range(14)]
    for i in range(14):
        for j in range(14):
            if((i+j)%2==0):
                SI[i][j]=Enemy_2()
                cv.create_image(j*74+37,i*56+28,image=SI[i][j])
            else:
                SI[i][j]=Enemy_2pi()
                cv.create_image(j*74+37,i*56+28,image=SI[i][j])
    cv.after(10,rush)


root=Tk()
cv =Canvas(root,width=1036,height=784-56*3,bg="black")
cv.pack()
rush()

root.mainloop()



    
