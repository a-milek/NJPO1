import time

if __name__ == '__main__':
    # Zadanie 1
    # Prześledź szybkość dodawania elementów do tablicy.
    tab = []
    timer = time.monotonic()
    print(timer)
    for x in range(20000):
        tab.append(12)
    timer = timer - time.monotonic()
    print("Elapsed time: ", timer)
