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


timezones = {'y': timezone_y,
             'x': timezone_x,
             'w': timezone_w,
             'v': timezone_v,
             'u': timezone_u,
             't': timezone_t,
             's': timezone_s,
             'r': timezone_r,
             'q': timezone_q,
             'p': timezone_p,
             'o': timezone_o,
             'n': timezone_n,
             'z': timezone_z,
             'a': timezone_a,
             'b': timezone_b,
             'c': timezone_c,
             'd': timezone_d,
             'e': timezone_e,
             'f': timezone_f,
             'g': timezone_g,
             'h': timezone_h,
             'i': timezone_i,
             'k': timezone_k,
             'l': timezone_l,
             'm': timezone_m,
             }


def get_timezone(timezone, now):
    if timezone not in timezones:
        raise NotImplemented()
    return timezones[timezone](now)


if __name__ == '__main__':
    time_now = datetime.datetime.utcnow()
    print("Greenwich time: ", time_now)
    print("Polish time: ", get_timezone("b", time_now))
