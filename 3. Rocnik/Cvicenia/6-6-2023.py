import turtle

tu = turtle.Turtle()

def main(count: int = 3, velkost=100) -> None:
    uhol = 90 if count%2 == 0 else -90
    if count == 1: return
    for _ in range(4):
        tu.forward(velkost/3)
        main(count-1, velkost/3)
        tu.forward(2*(velkost/3))
        tu.left(uhol)

main(4)
turtle.mainloop()
