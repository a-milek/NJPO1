# Zadanie 2
# Stwórz kalkulator do obliczenia aktualnej godziny w konkretnej strefie czasowej.
# Do zadania wystarczy utworzyć słownik z przesunięciami czasowymi z i od i *UTC*.
import datetime


def timezone_y(now):
    return now - datetime.timedelta(hours=12)


def timezone_x(now):
    return now - datetime.timedelta(hours=11)


def timezone_w(now):
    return now - datetime.timedelta(hours=10)


def timezone_v(now):
    return now - datetime.timedelta(hours=9)


def timezone_u(now):
    return now - datetime.timedelta(hours=8)


def timezone_t(now):
    return now - datetime.timedelta(hours=7)


def timezone_s(now):
    return now - datetime.timedelta(hours=6)


def timezone_r(now):
    return now - datetime.timedelta(hours=5)


def timezone_q(now):
    return now - datetime.timedelta(hours=4)


def timezone_p(now):
    return now - datetime.timedelta(hours=3)


def timezone_o(now):
    return now - datetime.timedelta(hours=2)


def timezone_n(now):
    return now - datetime.timedelta(hours=1)


def timezone_z(now):
    return now


def timezone_a(now):
    return now + datetime.timedelta(hours=1)


def timezone_b(now):
    return now + datetime.timedelta(hours=2)


def timezone_c(now):
    return now + datetime.timedelta(hours=3)


def timezone_d(now):
    return now + datetime.timedelta(hours=4)


def timezone_e(now):
    return now + datetime.timedelta(hours=5)


def timezone_f(now):
    return now + datetime.timedelta(hours=6)


def timezone_g(now):
    return now + datetime.timedelta(hours=7)


def timezone_h(now):
    return now + datetime.timedelta(hours=8)


def timezone_i(now):
    return now + datetime.timedelta(hours=9)


def timezone_k(now):
    return now + datetime.timedelta(hours=10)


def timezone_l(now):
    return now + datetime.timedelta(hours=11)


def timezone_m(now):
    return now + datetime.timedelta(hours=12)


def get_timezone(timezone, now):
    if timezone == 'y':
        return timezone_y(now)
    if timezone == 'x':
        return timezone_x(now)
    if timezone == 'w':
        return timezone_w(now)
    if timezone == 'v':
        return timezone_v(now)
    if timezone == 'u':
        return timezone_u(now)
    if timezone == 't':
        return timezone_t(now)
    if timezone == 's':
        return timezone_s(now)
    if timezone == 'r':
        return timezone_r(now)
    if timezone == 'q':
        return timezone_q(now)
    if timezone == 'p':
        return timezone_p(now)
    if timezone == 'o':
        return timezone_o(now)
    if timezone == 'n':
        return timezone_n(now)
    if timezone == 'z':
        return timezone_z(now)
    if timezone == 'a':
        return timezone_a(now)
    if timezone == 'b':
        return timezone_b(now)
    if timezone == 'c':
        return timezone_c(now)
    if timezone == 'd':
        return timezone_d(now)
    if timezone == 'e':
        return timezone_e(now)
    if timezone == 'f':
        return timezone_f(now)
    if timezone == 'g':
        return timezone_g(now)
    if timezone == 'h':
        return timezone_h(now)
    if timezone == 'i':
        return timezone_i(now)
    if timezone == 'k':
        return timezone_k(now)
    if timezone == 'l':
        return timezone_l(now)
    if timezone == 'm':
        return timezone_m(now)


if __name__ == '__main__':
    time_now = datetime.datetime.utcnow()
    print("Greenwich time: ", time_now)
    print("Polish time: ", get_timezone("b", time_now))
