import turtle
korytnacka = turtle.Turtle()
korytnacka.penup()
korytnacka.setx(-200)
korytnacka.pendown()

def prve_cvicenie(num):

    # Zadanie:
    #  Vykresli nejake ciarky alebo nieco
    #  ja neviem ja nechapem vobec co robim.

    if num == 1: return korytnacka.forward(50)
    prve_cvicenie(num-1)
    korytnacka.left(60)
    prve_cvicenie(num-1)
    korytnacka.right(120)
    prve_cvicenie(num-1)
    korytnacka.left(60)
    prve_cvicenie(num-1)

#prve_cvicenie(4)

korytnacka.left(90)
def druhe_cvicenie(num, size=120):

    # Zadanie:
    #  Vykresli do sestuholnika
    #  nejake sestuholniky, neviem
    #  kolko ani preco ale jo.

    pass

druhe_cvicenie(2)

turtle.mainloop()
