
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

    count = 0
    a, b, c = 1, 2, 3

    while not (a == b == c):
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        print('padlo -> {} - {} - {}'.format(a,b,c))
        count += 1

    print('pokusy: {}'.format(count))

#druhe_cvicenie()
