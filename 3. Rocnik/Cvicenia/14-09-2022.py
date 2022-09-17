
def prve_cvicenie():
    # Vypiste a spocitajte vsetky trojficerne cisla, ktorych sucet cifier
    # je rovny cislu 12 (Napr: 354 -> 3 + 5 + 4 = 12)
    
    cisla,count = 100, 0

    while cisla < 1000:
        cisla += 1
        cisla_list = list(str(cisla))
        cislo_jeden, cislo_dva, cislo_tri = int(cisla_list[0]), int(cisla_list[1]), int(cisla_list[2])

        if cislo_jeden + cislo_dva + cislo_tri == 12:
            print (cisla)
            count += 1

    print('Dokopy ich bolo',count)

#prve_cvicenie()

def druhe_cvicenie():
    # Hadzeme 3 kocky naraz, spocitajte kolko pokusov treba
    # aby padli 3 rovnake cisla. (Pripadne tie pokusy aj vypiste.)
    
    import random
    import tkinter

    canvas = tkinter.Canvas(width=500, height=500)
    canvas.pack()

    def random_farba():
        a = random.randint(11,99)
        b = random.randint(11,99)
        c = random.randint(11,99)
        farba = "#"+str(a)+str(b)+str(c)
        return farba

    print(random_farba())
    count = 0
    a, b, c = 1, 2, 3
    while not (a == b == c):

        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)

        y = 250

        canvas.delete("all")
        stvorec_a, stvorec_b, stvorec_c = canvas.create_rectangle(75,y-25,120,y+25,fill=random_farba(),width=3), canvas.create_rectangle(225,y-25,275,y+25,fill=random_farba(),width=3), canvas.create_rectangle(375,y-25,425,y+25,width=3,fill=random_farba())
        canvas_a, canvas_b, canvas_c = canvas.create_text(100,y,text=a,font="Arial, 25",fill=random_farba()), canvas.create_text(250,y,text=b,font="Arial, 25",fill=random_farba()), canvas.create_text(400,y,text=c,font="Arial, 25",fill=random_farba())
        pokus = canvas.create_text(450,450,font="Arial, 20",text=count+1)
        canvas.update()
        canvas.after(300)

        print('padlo -> {} - {} - {}'.format(a,b,c))
        count += 1

    print('pokusy: {}'.format(count))

#druhe_cvicenie()
