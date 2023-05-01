from math import sqrt


def fibonacci(num):
    # obliczanie za pomocą wzoru Bineta
    fib = ((1 / sqrt(5)) * ((1 + sqrt(5)) / 2) ** num) - ((1 / sqrt(5)) * ((1 - sqrt(5)) / 2) ** num)
    return fib


if __name__ == '__main__':
    print(int(fibonacci(93)))
