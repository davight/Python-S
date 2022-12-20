# Dnesne cvicenia vdaka Alexovi <3

# Preco som nepouzil set miesto manualneho
# deduplikovania? Sety su unordered.
def deduplicate(arr: list) -> list:

    temp = []
    for item in arr:
        if item not in temp: temp.append(item)
    return temp

def prve_cvicenie():

    # Zadanie:
    #  Z n cisla spocitaj vyskyt (v) kazdej cifry (c)
    #  nasledne ju vloz do listu vo formate [v, c]
    # Priklad: 13221 -> [1, 2] [3, 1] [2, 2]

    vstup = input("Zadaj nejake cele cislo: ")
    odpoved = []

    for cifra in deduplicate(list(vstup)):
        odpoved.append(
            [int(cifra), vstup.count(cifra)])
    print(*odpoved)

prve_cvicenie()

def druhe_cvicenie():

    # Zadanie:
    #  Usporiadaj cifry v n cisle podla ich
    #  prveho vyskytu.
    # Priklad:
    #  1,4,3,5,2,1,2,4,1 -> 1,1,1,4,4,3,5,2,2

    vstup = input("Zadaj nejake cele cislo: ")
    usporiadane = []

    for cifra in deduplicate(vstup.split()):
        if len(cifra) > 1: return print("Niesmie byt vacsie ako 9 !")
        usporiadane.extend(cifra * int(vstup.count(cifra)))
    print(", ".join(usporiadane))

druhe_cvicenie()
