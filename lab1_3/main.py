# Zmodyfikuj kod związany z losowaniem liczb z przedziału od 1 do 10,
# tak aby obliczał przybliżoną wartość oczekiwaną obliczoną jako średnią (z prób).
# Uśrednienie ma nastąpić 1m razy (milion razy).
import random

def wartosc_oczekiwana():
    n = 1000000
    suma = 0
    for i in range(n):
        suma = suma + random.randint(1, 10)
    return suma / n


if __name__ == '__main__':
    print(wartosc_oczekiwana())
