import math
import random


def monte_carlo(iterations):
    calosc = 0
    suma_poprawne = 0
    for x in range(iterations):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        calosc = calosc + 1
        if (x ** 2) + (y ** 2) <= 1:
            suma_poprawne = suma_poprawne + 1
    liczba_pi = (suma_poprawne * 4) / calosc
    return liczba_pi


if __name__ == '__main__':
    a = monte_carlo(1200000)
    print("wyliczona wartosc: ", a)
    dokladnosc = abs(math.pi - a) / math.pi
    print("dokładnosc: ", dokladnosc)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
