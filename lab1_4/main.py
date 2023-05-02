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


def primary_numbers(a, b):
    primaries = []
    for x in range(a, b):
        if is_primary(x):
            primaries.append(x)
    return primaries


if __name__ == '__main__':
    print(primary_numbers(2, 100))
