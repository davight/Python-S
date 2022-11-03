# Cvicenia z labakov.
# Den - 27.10.2022 ; Skupina - I

# +++> Info:
# 
#  - Delenie integerov a floatov v pythone pomocou operatora '/'
#    returne VZDY float typ.
#    @ Priklad:
#       8 / 4 => 2.0
# 
# -  Delenie integerov a floatov v pythone pomocou operatora '//'
#    zaokruhli vysledok a teda returne VZDY integer typ.
#    @ Priklad:
#      8 // 3 => 2
# 
#  - V Pythone existuje operator nazyvany ako "Modulo Operator",
#    ktory nam zobrazi zvysok po deleni celych cisel. Znak: '%'
#    @ Priklad:
#       10 % 4 => 2
#       Vysledok je 2, pretoze ak delime 10ku cislom 4 ostane nam zvysok 2.



# ++ Zadanie k prvemu cviceniu:
#   Napis program, ktory nahradi "Modulo Operator"
#   Vstup nacitavaj pomocou input funkcie.

# ++ Obmedzenia:
#   Nesmies pouzit samotny Modulo Operator ( % )

# Mozne riesenie:
def prveCvicenie():
    
    prveCislo, druheCislo = int(input("Zadaj prve cislo: ")), int(input("Zadaj druhe cislo: "))
    
    return prveCislo - ((prveCislo // druheCislo) * druheCislo)

print(prveCvicenie())



# ++ Zadanie k prvemu cviceniu:
#   Napis program, ktory nahradi "Modulo Operator"
#   Vstup nacitavaj pomocou input funkcie.

# ++ Obmedzenia:
#   Nesmies pouzit samotny Modulo Operator ( % )
#   Nesmies pouzit delenie ( '/' ani '//' )

# Mozne riesenie:
def druheCvicenie():

    prveCislo, druheCislo = int(input("Zadaj prve cislo: ")), int(input("Zadaj druhe cislo: "))

    count, zakladneCislo = 0, prveCislo

    while prveCislo >= druheCislo:

        prveCislo -= druheCislo
        count += 1
    
    return zakladneCislo - ( druheCislo * count )

print(druheCvicenie())