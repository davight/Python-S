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
