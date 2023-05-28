# Napisz dekorator, który ogranicza argument funkcji do zadanego przedziału.

def limit_range(given_minimum, given_maximum):
    def outer(func):
        def inner(*args, **kwargs):
            for arg in args:
                if (arg < given_minimum) | (arg > given_maximum):
                    return False
            for key, value in kwargs.items():
                if (value < given_minimum) | (value > given_maximum):
                    return False
            return func(*args, **kwargs)
        return inner
    return outer


@limit_range(0, 100)
def some_func(value, value2):
    return True


@limit_range(0, 5)
def some_func2(value):
    return True


if __name__ == "__main__":
    assert some_func(50, 50) is True
    assert some_func(0, 100) is True
    assert some_func(0, 101) is False

    assert some_func2(0) is True
    assert some_func2(5) is True
    assert some_func(101) is False
    assert some_func(-101) is False

