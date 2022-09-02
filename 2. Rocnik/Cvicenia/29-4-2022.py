#+------------------------------+
#Zadanie: Urobit kresliace platno, kde sa da nastavit farba, tvar stetca a velkost
#+------------------------------+

import tkinter
import random

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()
h = 12
f = 'black'
t = 'oval'
while True:
    # Oddelovacia ciara
    odx = 40
    canvas.create_line(odx-1,0,odx-1,500,fill="black")
    # Misc
    canvas.create_rectangle(1,449,21,469,outline='black',width=1)
    canvas.create_text(11,459,text="?",font="Arial, 17")
    #pozadie platna
    canvas.create_rectangle(40,0,500,500,fill='white',outline='')
    #Vyber farby z tabulky
    canvas.create_text(20,10,text="Farby:",font="Arial 8",fill="black")
    canvas.create_rectangle(1,20,21,40,fill='red',outline='black')
    canvas.create_rectangle(1,50,21,70,fill='blue',outline='black')
    canvas.create_rectangle(1,80,21,100,fill='green',outline='black')
    canvas.create_rectangle(1,110,21,130,fill='yellow',outline='black')
    canvas.create_rectangle(1,140,21,160,fill='black',outline='black')
    # Vyber hrubky z tabulky
    canvas.create_text(20,170,text="Hrubka:",font="Arial 8",fill="black")
    #Mazanie
    canvas.create_rectangle(1,479,21,499,outline='red',width=4)
    canvas.create_line(1,479,21,499,fill='red',width=3)
    canvas.create_line(21,479,1,499,fill='red',width=3)
    #Hrubka
    canvas.create_rectangle(1,180,21,200,outline='black')
    canvas.create_oval(1+2,180+2,21-2,200-2,fill='black')
    canvas.create_rectangle(1,210,21,230,outline='black')
    canvas.create_oval(1+4,210+4,21-4,230-4,fill='black')
    canvas.create_rectangle(1,240,21,260,outline='black')
    canvas.create_oval(1+6,240+6,21-6,260-6,fill='black')
    #Tvar
    canvas.create_text(15,270,text="Tvar:",font="Arial 8",fill="black")
    canvas.create_rectangle(1,280,21,300,outline='black')
    canvas.create_rectangle(1+6,280+6,21-6,300-6,fill='black')
    canvas.create_rectangle(1,310,21,330,outline="black")
    canvas.create_oval(1+6,310+6,21-6,330-6,fill="black")
    canvas.create_rectangle(1,340,21,360,outline="black")
    canvas.create_text(11,360,text="*",font="Arial 30")

    # Vykreslovanie 
    def tahanie(m):
        global odx
        vh = odx+h/2+3
        if m.x > vh:
            if t == "oval":
                canvas.create_oval(m.x-h,m.y-h,m.x+h,m.y+h,fill=f,outline=f)
            elif t == "rect":
                canvas.create_rectangle(m.x-h,m.y-h,m.x+h,m.y+h,fill=f,outline=f)
            elif t == "hvz":
                p = "Arial " + str(h*5)
                canvas.create_text(m.x,m.y+h,text="*",font=p,fill=f)
                
    
    # Vyber farby / hrubky
    def klik(m):
        global f,h,t
        if m.x >= 1 and m.x <= 21 and m.y >= 20 and m.y <= 40:
            f = 'red'
        elif m.x >= 1 and m.x <= 21 and m.y >= 50 and m.y <= 70:
            f = 'blue'
        elif m.x >= 1 and m.x <= 21 and m.y >= 80 and m.y <= 100:
            f = 'green'
        elif m.x >= 1 and m.x <= 21 and m.y >= 110 and m.y <= 130:
            f = 'yellow'
        elif m.x >= 1 and m.x <= 21 and m.y >= 140 and m.y <= 160:
            f = 'black'
        elif m.x >= 1 and m.x <= 21 and m.y >= 180 and m.y <= 200:
            h = 16
        elif m.x >= 1 and m.x <= 21 and m.y >= 210 and m.y <= 230:
            h = 12
        elif m.x >= 1 and m.x <= 21 and m.y >= 240 and m.y <= 260:
            h = 8
        elif m.x >= 1 and m.x <= 21 and m.y >= 280 and m.y <= 300:
            t = "rect"
        elif m.x >= 1 and m.x <= 21 and m.y >= 310 and m.y <= 330:
            t = "oval"
        elif m.x >= 1 and m.x <= 21 and m.y >= 340 and m.y <= 360:
            t = "hvz"
        elif m.x >= 1 and m.x <= 21 and m.y >= 449 and m.y <= 469:
            f = str()
            for i in range(6):
                a = random.choice("ABCDEF1234567890")
                f += a
            f = "#"+f
        elif m.x >= 1 and m.x <= 21 and m.y >= 479 and m.y <= 499:
            canvas.create_rectangle(40,0,500,500,fill='white',outline='')

        # Update
        canvas.create_oval(1+2,180+2,21-2,200-2,fill=f)
        canvas.create_oval(1+4,210+4,21-4,230-4,fill=f)
        canvas.create_oval(1+6,240+6,21-6,260-6,fill=f)
        canvas.create_text(11,360,text="*",font="Arial 30",fill=f)
        canvas.create_oval(1+6,310+6,21-6,330-6,fill=f)
        canvas.create_rectangle(1+6,280+6,21-6,300-6,fill=f)
    
    canvas.bind("<B1-Motion>",tahanie)
    canvas.bind("<Button-1>",klik)
    canvas.update()
    canvas.mainloop()
