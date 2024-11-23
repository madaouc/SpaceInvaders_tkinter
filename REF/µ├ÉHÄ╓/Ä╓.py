#-*-coding:utf-8-*-
from Tkinter import *
from time import *
from Queue import *
wind = Queue()
ar = Queue()
dan = Queue()
Canv = Queue()
ini = Queue()
wal = Queue()
fea = Queue()
gmt = Queue()
cm = Queue()
ma = Queue()
spt = Queue()
ari= Queue()
spd = Queue()
im1 = Queue()
im2 = Queue()
root = Tk()

def init():
    from random import randint
    ar.put(300);ar.put(300)
    dan.put(4)
    ini.put(1)
    canvas = Canvas(root,width=620,height=640,bg='white');Canv.put(canvas)
    x1 = randint(2,28);y1 = randint(2,28)
    while x1 == 15 and y1 ==14:
        x1 = randint(2,28);y1 = randint(2,28)
    #imbg = PhotoImage(file = 'C:\大作\草坪2.gif')
    #canvas.create_image(310,320,image = imbg)
    #im1.put(imbg)
    fea.put(canvas.create_rectangle(x1*20,y1*20+20,x1*20+20,y1*20+40,fill='yellow'))
    imfd = PhotoImage(file = 'C:\大作\果1.gif')
    canvas.create_image(x1*20+10,y1*20+30,image = imfd)
    im2.put(imfd)
    gmt.put(canvas.create_text(300,20,text='time: %0.1f'% 0))
    ari.put(time())
    spd.put(100)

    
def background():
    try:
        txt = open('mark.txt','r')
    except:
        txt = open('mark.txt','w')
        txt.write('0')
        txt.close()
        txt = open('mark.txt','r')
    canvas = Canv.get();Canv.put(canvas)
    x1 = ar.get();y1 = ar.get();canvas = Canv.get()
    ar.put(x1);ar.put(y1);Canv.put(canvas)
    snake = [canvas.create_oval(x1,y1,x1+20,y1-20,fill='',width=2),canvas.create_rectangle(x1,y1,x1+20,y1-20,fill='blue',width=1)]
    ar.put(snake)
    canvas.pack()
    cm.put(canvas.create_text(200,20,text='cursc：%d'%(len(snake)-2)))
    ma.put(canvas.create_text(400,20,text='maxsc：%d'%int(txt.readline())))
    spt.put(canvas.create_text(500,20,text='cursp：%d'%100))
    txt.close()

def wa_ob():
    canvas = Canv.get();Canv.put(canvas)
    wall = []
    l = 0
    k = 1
    for j in range(20,600,20):
        wall.append(canvas.create_rectangle(l*560+20,j+20,l*560+40,j+40,fill='green'));wall.append(canvas.create_rectangle(k*560+20,j+20,k*560+40,j+40,fill='green'))
    for i in range(20,600,20):
        wall.append(canvas.create_rectangle(i,l*560+40,i+20,l*560+60,fill='green'));wall.append(canvas.create_rectangle(i,k*560+40,i+20,k*560+60,fill='green'))
    wal.put(wall)
    
def fo_ob():
    from random import randint
    x = ar.get();y = ar.get();snake = ar.get()
    canvas = Canv.get();Canv.put(canvas)
    food = fea.get()
    running = True
    while running:
        canvas.delete(food)
        x1 = randint(2,28);y1 = randint(2,28)
        food = canvas.create_rectangle(x1*20,y1*20+20,x1*20+20,y1*20+40,fill='yellow')
        for i in snake:
            if canvas.bbox(i) == canvas.bbox(food):
                running = True;break
            else: running = False
    imfd = im2.get()
    imfd = PhotoImage(file = 'C:\大作\果1.gif')
    canvas.create_image(x1*20+10,y1*20+30,image = imfd)
    im2.put(imfd)
    
    fea.put(food)
    ar.put(x);ar.put(y);ar.put(snake)

def ma_ob():
    txt =  open('mark.txt')
    mark = cm.get();mmark = ma.get();canvas = Canv.get()
    cm.put(mark);ma.put(mmark);Canv.put(canvas)
    x = ar.get();y = ar.get();snake = ar.get()
    ar.put(x);ar.put(y);ar.put(snake)
    canvas.itemconfig(mark,text='cursc：%d'%(len(snake)-2))
    if int(txt.readlines()[0])<(len(snake)-2):
        txt.close()
        txt =  open('mark.txt','w')
        txt.write(str(len(snake)-2))
        txt.close()
        canvas.itemconfig(mmark,text='maxsc：%d'%(len(snake)-2))

def clock():
    clocktext = gmt.get();canvas = Canv.get();t = ari.get()
    gmt.put(clocktext);Canv.put(canvas);ari.put(t)
    canvas.itemconfig(clocktext,text = 'time: %0.1f'% (time()-t))
    canvas.after(100,clock)

def up(*ignore):
    x1 = ar.get();y1 = ar.get()-20;canvas = Canv.get();snake = ar.get()
    ar.put(x1);ar.put(y1);Canv.put(canvas);ar.put(snake)
    canvas.coords(snake[0],x1,y1,x1+20,y1-20)
def down(*ignore):
    x1 = ar.get();y1 = ar.get()+20;canvas = Canv.get();snake = ar.get()
    ar.put(x1);ar.put(y1);Canv.put(canvas);ar.put(snake)
    canvas.coords(snake[0],x1,y1,x1+20,y1-20)
def left(*ignore):
    x1 = ar.get()-20;y1 = ar.get();canvas = Canv.get();snake = ar.get()
    ar.put(x1);ar.put(y1);Canv.put(canvas);ar.put(snake)
    canvas.coords(snake[0],x1,y1,x1+20,y1-20)
def right(*ignore):
    x1 = ar.get()+20;y1 = ar.get();canvas = Canv.get();snake = ar.get()
    ar.put(x1);ar.put(y1);Canv.put(canvas);ar.put(snake)
    canvas.coords(snake[0],x1,y1,x1+20,y1-20)

def pressup(*ignore):
    dan.get();dan.put(0)
def pressdown(*ignore):
    dan.get();dan.put(1)
def pressleft(*ignore):
    dan.get();dan.put(2)
def pressright(*ignore):
    dan.get();dan.put(3)

def direction():
    dire = dan.get()
    if dire == 0 :
        clock()
        up()
        root.unbind('<Up>');root.unbind('<Down>')
        root.bind('<Left>',pressleft);root.bind('<Right>',pressright)
    if dire == 1 :
        clock()
        down()
        root.unbind('<Up>');root.unbind('<Down>')
        root.bind('<Left>',pressleft);root.bind('<Right>',pressright)
    if dire == 2 :
        clock()
        left()
        root.unbind('<Left>');root.unbind('<Right>')
        root.bind('<Up>',pressup);root.bind('<Down>',pressdown)
    if dire == 3 :
        clock()
        right()
        root.unbind('<Left>');root.unbind('<Right>')
        root.bind('<Up>',pressup);root.bind('<Down>',pressdown)
    dan.put(dire)

def failure():
    canvas = Canv.get();Canv.put(canvas)
    x1 = ar.get();y1 = ar.get();snake = ar.get()
    ar.put(x1);ar.put(y1);ar.put(snake)
    wall = wal.get();wal.put(wall)
    for i in wall:
        if canvas.bbox(snake[0]) == canvas.bbox(i):
            return True
    for i in range(2,len(snake),1):
        if canvas.bbox(snake[0]) == canvas.bbox(snake[i]):
            return True

def move():
    canvas = Canv.get();Canv.put(canvas)
    direction()
    x1 = ar.get();y1 = ar.get();snake = ar.get()
    ar.put(x1);ar.put(y1);ar.put(snake)
    if failure():return
    for i in range(len(snake)-1,0,-1):
        coord = canvas.bbox(snake[i-1])#为什么？
        canvas.coords(snake[i],coord[0]+1,coord[1]+1,coord[2]-1,coord[3]-1)
    canvas.coords(snake[0],x1,y1,x1+20,y1-20)
    x1 = ar.get();y1 = ar.get();snake = ar.get()
    ar.put(x1);ar.put(y1);ar.put(snake)
    ma_ob()
    speed = spd.get();spd.put(speed)
    canvas.after(speed,move)
    canvas = Canv.get();Canv.put(canvas)
    x1 = ar.get();y1 = ar.get();snake = ar.get()
    ar.put(x1);ar.put(y1);ar.put(snake)
    food = fea.get();fea.put(food)
    if canvas.bbox(snake[0]) == canvas.bbox(food):
        fo_ob()
        x1 = ar.get();y1 = ar.get();canvas = Canv.get();snake = ar.get()
        snake.append(canvas.create_oval(x1,y1,x1+20,y1-20,fill='blue',width=1))
        ar.put(x1);ar.put(y1);Canv.put(canvas);ar.put(snake)

def main(*ignore):
    init()
    background()
    wa_ob()
    root.bind('<Up>',pressup)
    root.bind('<Down>',pressdown)
    root.bind('<Left>',pressleft)
    root.bind('<Right>',pressright)
    move()
    root.mainloop()

main()
