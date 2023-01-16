# @Nazov:
# are_integers
# @Popis:
# returne boolean na zaklade toho
# ci je hodnota list a zaroven ci
# je mozne ho premenit na integery
def are_integers(arr) -> bool:
    if not isinstance(arr, list): return False
    try:
        [int(i) for i in arr]
        return True
    except ValueError:
        return False
