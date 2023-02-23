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
