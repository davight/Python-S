import tkinter
import random

def prvecvicenie():
    import sys

    patsto = dvesto = sto = patdesiat = dvadsat = desat = pat = 5
    udajpatsto = udajdvesto = udajsto = udajpatdesiat = udajdvadsat = udajdesat = udajpat = b = int()
    print('Vitajte v Bankomate, mozete vyberat iba hodnotu do 4 425eur, zadana hodnota musi byt delitelna 5kou, pretoze mince nemame.')
    a = input('Zadajte hodnotu, ktoru si prajete vybrat:\n')
    
    try:
        a = int(a)
    except ValueError:
        print('Zadana hodnota nie je integer!')
        sys.exit()
    
    if a > 4425 or a%5 != 0:
        print('Zadana hodnota nie je delitelna 5kou, alebo presahuje limit 4 425eur')
    elif a <= 0:
        print('Zadana hodnota je prilis mala.')
    else:
        c = a 
        while a >= 500:
            a -= 500
            udajpatsto += 1
        while a >= 200:
            a -= 200
            udajdvesto += 1
        while a >= 100:
            a -= 100
            udajsto += 1
        while a >= 50:
            a -= 50
            udajpatdesiat += 1
        while a >= 20:
            a -= 20
            udajdvadsat += 1
        while a >= 10:
            a -= 10
            udajdesat += 1
        while a >= 5:
            a -= 5
            udajpat += 1
        print('Bolo ta ti vydana hodnota',c,'eur ktora sa sklada z:\n',udajpatsto,'x 500eur\n',udajdvesto,'x 200eur\n',udajsto,'x 100eur\n',udajpatdesiat,'x 50eur\n',udajdvadsat,'x 20eur\n',udajdesat,'x 10eur\n',udajpat,'x 5eur')

prvecvicenie()

def druhecvicenie():
    canvas = tkinter.Canvas(width=600, height=400)
    canvas.pack()
    #Rychlost
    r = 0
    
    x = int()
    while x != 600:
        canvas.create_rectangle(1,1,x,401,fill='red',outline='')
        x += 1
        canvas.after(r)
        canvas.update()
    x = int()
    while x != 600:
        canvas.create_rectangle(1,101,x,201,fill='white',outline='')
        x += 1
        canvas.after(r)
        canvas.update()
    y = int()
    while y != 400:
        canvas.create_rectangle(101,1,201,y,fill='white',outline='')
        y += 1
        canvas.after(r)
        canvas.update()
    x = int()
    while x != 600:
        canvas.create_rectangle(1,121,x,181,fill='blue',outline='')
        x += 1
        canvas.after(r)
        canvas.update()
    y = int()
    while y != 400:
        canvas.create_rectangle(121,1,181,y,fill='blue',outline='')
        y += 1
        canvas.after(r)
        canvas.update()
    tkinter.mainloop()
druhecvicenie()

def tretiecvicenie():
    canvas = tkinter.Canvas(width=600, height=600)
    canvas.pack()
    c = int()
    while c != 5000:
        x = random.randint(1,600)
        y = random.randint(1,600)
        if not (x <= 100 and y <= 100 or x <= 100 and y >= 500 or x >= 500 and y <= 100 or x >= 500 and y >= 500):
            canvas.create_oval(x-10,y-10,x+10,y+10,fill='red')
            c += 1
    tkinter.mainloop()
tretiecvicenie()

def stvrtecvicenie():
    import sys

    udajdvojky = udajjednotky = udajpatdesiat = udajdvadsat = udajdesat = udajpat = b = int()
    a = input('Zadajte vasu vyplatu pre jej vypocet v bankovkach')
    
    try:
        a = int(a)
    except ValueError:
        print('Zadana hodnota nie je integer!')
        sys.exit()
    
    if a <= 0:
        print('Zadana hodnota je prilis mala.')
    else:
        c = a 
        while a >= 50:
            a -= 50
            udajpatdesiat += 1
        while a >= 20:
            a -= 20
            udajdvadsat += 1
        while a >= 10:
            a -= 10
            udajdesat += 1
        while a >= 5:
            a -= 5
            udajpat += 1
        while a >= 2:
            a -= 2
            udajdvojky += 1
        while a >= 1:
            a -= 1
            udajjednotky += 1 
            
        print('Tvoja vyplata sa sklada z',c,'eur ktora sa sklada z:\n',udajpatdesiat,'x 50eur\n',udajdvadsat,'x 20eur\n',udajdesat,'x 10eur\n',udajpat,'x 5eur\n',udajdvojky,'x 2eur\n',udajjednotky,'x 1eur')
stvrtecvicenie()
