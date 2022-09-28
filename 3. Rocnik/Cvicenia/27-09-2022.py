# Cely tento subor (kod, vsetky funkcie) predstavuje jedno zadanie.

# Zadanie: 
#  Na zaklade vlozeneho rodneho cisla, overte jeho platnost
#  teda ci obsahuje "/" na spravnom mieste, ci lava cast obsahuje
#  6 cisel a prava 4 cisla.
#  Nasledne na zaklade mesiaca urcite ci sa jedna o muza alebo zenu
#  Muz ma na mieste mesiaca 0 alebo 1
#  Zena ma na mieste mesiaca 5 alebo 6, lebo pri ich mesiacoch sa
#  pripocitava cislo 50.


# Integer checker
def je_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

# Prevod rokov (98 -> 1998, 03 -> 2003)
def rok_kalkulacia(str):
    cislo = int(str)
    if cislo > 22:
        return "19"+str
    return "20"+str

# Prevod ciselnych mesiacov na nazvy
def mesiac_kalkulacia(str_mesiac):
    mesiace = {
        "01": "Januar",
        "02": "Februar",
        "03": "Marec",
        "04": "April",
        "05": "Maj",
        "06": "Jun",
        "07": "Jul",
        "08": "August",
        "09": "September",
        "10": "Oktober",
        "11": "November",
        "12": "December",
    }
    return mesiace[str_mesiac]

# Main kod
def cvicenie_jeden():
    while True:
        str = input("Zadaj svoje rodne cislo:\n")
        # Rodne cislo: 851208/4321
        list_str = list(str)
        if len(list_str) == 11:
            # Obsahuje znak "/"
            if list_str[6] == "/":
                strany = str.split("/")
                prva_strana = strany[0]
                druha_strana = strany[1]
                if je_int(prva_strana) and je_int(druha_strana):
                    # Obe cisla su integery
                    cele_cislo = int(prva_strana+druha_strana)
                    if cele_cislo%11 == 0:
                        # prva strana je delitelna 11kou cize je to spravne
                        rok = rok_kalkulacia("".join(list_str[0:2]))
                        den = "".join(list_str[4:6]) 
                        if int(prva_strana[2]) == 0 or int(prva_strana[2]) == 1:
                            # Teda jeho datum narodeni
                            mesiac = "".join(list_str[2:4])
                            mesiac_text = mesiac_kalkulacia(mesiac)
                            print("\nMUZ -> Datum narodenia: {}.{}.{} ({})\n".format(den,mesiac,rok,mesiac_text))
                        else:
                            mesiac = 50-int("".join(list_str[2:4]))
                            mesiac_text = mesiac_kalkulacia(str(mesiac))
                            print("\nZENA -> Datum narodenia: {}.{}.{} ({})\n".format(den,mesiac,rok,mesiac_text))
                    else:
                        # Obe strany nie su delitelne 11kou
                        print("Obe strany nie su delitelna 11kou!")
                else:
                    # Nejaka strana nie je integer
                    print("Jedna zo stran nie je integer!")
            else:
                # Dlzka nie je 12 indexov
                print("Rodne cislo musi obsahovat / (lomku)")
        else:
            print("Rodne cislo nezodpoveda spravnej dlzke!")
        # Overenie rodneho cisla, prv ci je to vobec rodne cislo
cvicenie_jeden()
