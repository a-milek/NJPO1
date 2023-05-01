# Napisz algorytm obliczający kolejne liczby pierwsze dla zadanych wartości.
def is_primary(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n ** 0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True


def next_primary(num):
    prim = num
    while not is_primary(prim):
        prim = prim + 1
    return prim


if __name__ == '__main__':
    print (next_primary(100))