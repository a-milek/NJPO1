# Napisz generator, który dla zadanego wielomianu i przedziału wartości, zwróci jego miejsca zerowe.
# Dla pierwszego wywołania wynikiem ma być pierwsze miejsce zerowe, dla drugiego, drugie itd.
# Można zastosować naiwny algorytm sprawdzający kolejne wartości wielomianu.
# Można również zastosować kodowanie wielomianu bezpośrednio w kodzie języka Python: `x**n*x**(n-1)`.

def generate_polynomial_roots(polynomial, range_floor, range_ceiling):
    for x in range(range_floor, range_ceiling):
        if polynomial(x) == 0:
            yield x


def define_polynomial(*coefficients):
    def polynomial(x):
        result = 0
        for i in range(len(coefficients)):
            result += coefficients[i] * x ** (len(coefficients) - i - 1)
        return result
    return polynomial


if __name__ == '__main__':

    # Test 1
    polynomial = define_polynomial(1, 6, 11, 6)
    range_floor = -100
    range_ceiling = 100
    roots = []
    expected_roots = [-3, -2, -1]

    for root in generate_polynomial_roots(polynomial, range_floor, range_ceiling):
        roots.append(root)

    assert roots == expected_roots
