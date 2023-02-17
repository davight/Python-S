import turtle
import random

tu = turtle.Turtle()

def Filler(funkcia):
    farba = "red", "blue", "green", "pink", "yellow", "orange", "brown", "white", "purple", "lime"

    def wrapper(*args, **kwargs):
        tu.fillcolor(random.choice(farba))
        tu.begin_fill()
        f = funkcia(*args, **kwargs)
        tu.end_fill()
        return f
    return wrapper

@Filler
def n_uholnik(pocet_uhlov: int, velkost: int):
    uhol = 360 / pocet_uhlov
    for _ in range(pocet_uhlov):
        tu.left(uhol)
        tu.fd(velkost)

@Filler
def lupienka():
    for _ in range(2):
        for _ in range(9):
            tu.fd(10)
            tu.left(10)
        tu.left(90)


# Zadanie:
#  Vykresli co najpresnejsiu kruznicu
#  a vyfarbi ju.

def prve_cvicenie() -> None:
    n_uholnik(360, 1)

# prve_cvicenie()

# Zadanie:
#  Vykresli n stvorcov vedla seba na
#  platne, kazdy stvorec ma inu farbu.

def druhe_cvicenie(n: int) -> None:
    for _ in range(n):
        tu.pu()
        tu.fd(70)
        tu.pd()
        n_uholnik(4, 50)

# druhe_cvicenie(5)

# Zadanie:
#  Vykresli n pocet lupienkov kvetu.
#  Kazdy lupienok vyfarby inou farbou.

def tretie_cvicenie(lupene: int) -> None:
    for _ in range(lupene):
        lupienka()
        tu.left(int(360 / lupene))

# tretie_cvicenie(10)

turtle.mainloop()
