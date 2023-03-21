import turtle
turtle.delay(0)
turtle.speed(0)

def n_uholnik(pocet_uhlov: int, velkost: int, objekt) -> None:
    if isinstance(objekt, list) or isinstance(objekt, tuple):
        uhol = 360 / pocet_uhlov
        for _ in range(pocet_uhlov):
            for obj in objekt:
                obj.left(uhol)
                obj.fd(velkost)
    else:
        uhol = 360 / pocet_uhlov
        for _ in range(pocet_uhlov):
            objekt.left(uhol)
            objekt.fd(velkost)

def prve_cvicenie(pocet: int) -> None:

    # Zadanie:
    #  Vykresli naraz kruh s n korytnackami.

    korytnacky = [turtle.Turtle() for _ in range(pocet)]
    x, uhol = -400, 20
    for obj in korytnacky:
        obj.setx(x)
        obj.left(uhol)
        obj.fd(20)
        x += 10
        uhol += 20
    n_uholnik(360, 1, korytnacky)

prve_cvicenie(36)

def druhe_cvicenie():

    # Zadanie:
    #  Vykresli naramok z 20 kruznic
    pass
    

turtle.mainloop()
