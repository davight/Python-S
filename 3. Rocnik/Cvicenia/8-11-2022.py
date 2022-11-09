# Global variabilita
teploty = []

# Main funkcia
def main():

    # Main funkcia pre zadavanie teploty, ktoru
    # opakovane vyuzijeme v dalsich funkciach.
    global teploty
    vstup, count = "iHateItHere", 1

    print("Zadaj teplotu, ktoru chces pridat do zoznamu teplot!\nAk chces ukoncit zadavanie zadaj STOP.")
    while str(vstup).upper() != "STOP":

        vstup = input(f"Den {count}. -> Teplota: ")
        count += 1

        if vstup.upper() != "STOP":

            try:
                vstup = int(vstup)
                teploty.append(vstup)

            except ValueError:
                return print(f"Neplatne cislo / STOP prikaz -> \'{vstup}\'!")

main()

def prveCvicenie():

    # ++ Zadanie:
    #  Vytvor list, ktory obsahuje teploty 7 dni.
    #  Z teplot vypis priemernu teplotu za tyzden,
    #  najmensiu teplotu za tyzden,
    #  najvacsiu teplotu za tyzden.

    # ++ Obmedzenia:
    #  Funkcie na returnutie maximalnej, a minimalnej
    #   teploty si musis napisat sam :(

    # List teplot
    global teploty

    # Funckia pre returnutie najvacsej hodnoty z listu
    def maxCislo(cisla):

        count = cisla[0]

        for i in cisla:
            if i > count:
                count = i

        return count

    # Funckia pre returnutie najmensej hodnoty z listu
    def minCislo(cisla):

        count = maxCislo(cisla)

        for i in cisla:
            if i < count:
                count = i

        return count

    # Funckia pre returnutie priemernej hodnoty z listu
    def priemerCislo(cisla):

        sucetHodnot, pocetHodnot = 0, 0

        for i, cislo in enumerate(cisla):
            sucetHodnot += cislo
            pocetHodnot = i + 1

        return sucetHodnot/pocetHodnot

    teplotyFormat = '°C, '.join(map(str, teploty))
    maxTeplota, minTeplota, priemerTeplota = maxCislo(teploty), minCislo(teploty), round(priemerCislo(teploty))
    maxTeplotaDen, minTeplotaDen = teploty.index(maxTeplota) + 1, teploty.index(minTeplota) + 1

    print(f"\nZ tyzdna so zadanymi teplotami: {teplotyFormat}°C boli namerane tieto hodnoty:")
    print(f"Najvacsia teplota: {maxTeplota}°C, namerana v {maxTeplotaDen}. den")
    print(f"Najmensia teplota: {minTeplota}°C, namerana v {minTeplotaDen}. den")
    print(f"Priemerna teplota: {priemerTeplota}°C\n")

#prveCvicenie()

def druheCvicenie():

    # ++ Zadanie:
    #  Vytvor list, ktory obsahuje teploty 7 dni.
    #  Z teplot vypis priemernu teplotu za tyzden,
    #  najmensiu teplotu za tyzden,
    #  najvacsiu teplotu za tyzden.
    #  Mozes pouzit built-in funkcie ako sum, len, max, min ...

    # List teplot
    global teploty

    teplotyFormat = '°C, '.join(map(str, teploty))
    maxTeplota, minTeplota, priemerTeplota = max(teploty), min(teploty), round( max(teploty) / len(teploty) )
    maxTeplotaDen, minTeplotaDen = teploty.index(maxTeplota) + 1, teploty.index(minTeplota) + 1

    print(f"\nZ tyzdna so zadanymi teplotami: {teplotyFormat}°C boli namerane tieto hodnoty:")
    print(f"Najvacsia teplota: {maxTeplota}°C, namerana v {maxTeplotaDen}. den")
    print(f"Najmensia teplota: {minTeplota}°C, namerana v {minTeplotaDen}. den")
    print(f"Priemerna teplota: {priemerTeplota}°C\n")

#druheCvicenie()

def tretieCvicenie():
    
    # ++ Zadanie:
    #  Zo zoznamu teplot sprav listy
    #  s parnymi a neparnymi cislami

    global teploty

    # Variability
    parneTeploty = [ i for i in teploty if i%2 == 0]
    neparneTeploty = [ i for i in teploty if i%2 != 0 ]
    teplotyFormat = '°C, '.join( map(str, teploty) )

    print(f"\nZ tyzdna so zadanymi teplotami: {teplotyFormat}°C boli namerane tieto hodnoty:")
    print(f"Parne teploty: {}°C".format( '°C, '.join( map(str, parneTeploty) ) ) )
    print(f"Neparne teploty: {}°C".format( '°C, '.join( map(str, neparneTeploty) ) ) )

#tretieCvicenie()
