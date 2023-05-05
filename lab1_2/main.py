# Zadanie 2
# Stwórz kalkulator do obliczenia aktualnej godziny w konkretnej strefie czasowej.
# Do zadania wystarczy utworzyć słownik z przesunięciami czasowymi z i od i *UTC*.
import datetime

timezones = {'y': -12.0,
             'x': -11.0,
             'w': -10.0,
             'v': -9.0,
             'u': -8.0,
             't': -7.0,
             's': -6.0,
             'r': -5.0,
             'q': -4.0,
             'p': -3.0,
             'o': -2.0,
             'n': -1.0,
             'z': 0.0,
             'a': 1.0,
             'b': 2.0,
             'c': 3.0,
             'd': 4.0,
             'e': 5.0,
             'f': 6.0,
             'g': 7.0,
             'h': 8.0,
             'i': 9.0,
             'k': 10.0,
             'l': 11.0,
             'm': 12.0,
             }


def get_timezone(timezone, now):
    if timezone not in timezones:
        raise NotImplemented()
    return timezones[timezone](now)


if __name__ == '__main__':
    time_now = datetime.datetime.utcnow()
    print("Greenwich time: ", time_now)
    print("Polish time: ", get_timezone("b", time_now))
