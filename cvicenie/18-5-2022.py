# Vypisat meno po pismenku, s tym ze zacne cele
# Priklad:
# Peter
# Pete
# Pet
# Pe
# P

def menicko2(meno):
    for i in range(len(meno)):
        print(meno[:len(meno)-i])
menicko2("Peter")

# Opak cvicenia z: Python-S/cvicenie/13-5-2022.py
# https://github.com/analnyroztahovac/Python-S/blob/main/cvicenie/13-5-2022.py
