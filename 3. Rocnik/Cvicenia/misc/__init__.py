# @Nazov:
# n_uholnik
# @Popis
# vykresli na korytnaciom platne
# n_uholnik na zaklade zadanych
# hodnot
def n_uholnik(pocet_uhlov: int, velkost: int, objekt) -> None:
    uhol = 360 / pocet_uhlov
    for _ in range(pocet_uhlov):
        objekt.left(uhol)
        objekt.fd(velkost)

# @Nazov:
# are_integers
# @Popis:
# returne boolean na zaklade toho
# ci je hodnota list a zaroven ci
# je mozne ho premenit na integery
def are_integers(arr) -> bool:
    if not isinstance(arr, list): return False
    try:
        for i in arr: int(i)
    except ValueError:
        return False
    else:
        return True
