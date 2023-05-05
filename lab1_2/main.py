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


# Verify if zone is in the timezones
def check_if_valid_zone(zone):
    if zone not in timezones:
        return 0


# Calculate timezone time
def get_time_in_zone(zone):
    if check_if_valid_zone(zone) != 0:
        offset = datetime.timedelta(hours=timezones[zone])
        return (get_time_now() + offset).strftime("%H:%M:%S")
    else:
        return "No such timezone exists"


def get_time_now():
    return datetime.datetime.utcnow()


def get_timezone(timezone, now):
    if timezone not in timezones:
        raise NotImplemented()
    return timezones[timezone](now)


# Test for different timezones
if __name__ == '__main__':
    # Correct timezone
    print('Current time in GMT:', get_time_in_zone('z'))
    print('Current time in EST:', get_time_in_zone('r'))
    print('Current time in CST:', get_time_in_zone('s'))
    print('Current time in MST:', get_time_in_zone('t'))
    print('Current time in PST:', get_time_in_zone('u'))

    # Incorrect timezones
    print('Current time in incorrect timezone:', get_time_in_zone('nm'))
    print('Current time in incorrect timezone:', get_time_in_zone('1'))
    print('Current time in incorrect timezone:', get_time_in_zone('!'))