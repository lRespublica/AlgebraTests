discriminant = lambda a, b, c, n: (b * b - 4 * a * c) % n
module = lambda n, x: x if x >= 0 else x + n


def frac(n, numerator, denominator):
    for elem in range(0, n):  # [0, n-1]
        if (numerator % n) == ((denominator * elem) % n):
            return elem
    return None


def get_quadratic_deduction(n):
    res = dict()
    for elem in range(0, (n // 2) + 1):
        res[(elem*elem) % n] = elem
    return res


def get_remains(n):
    res = dict()
    for elem in range(0, n):  # [0, n-1]
        res[elem] = (elem * elem) % n
    return res


def get_x(a, b, d, n):
    quadratic_deduction = get_quadratic_deduction(n)
    if d not in quadratic_deduction:
        return None, None
    x1 = frac(n, -b + quadratic_deduction[d], 2 * a)
    x2 = frac(n, -b - quadratic_deduction[d], 2 * a)
    return x1, x2


n = int(input("Введите n: "))
print("Квадратичные вычеты:")
for k, v in get_remains(n).items():
    print(f"{k}: {v}")
a, b, c = map(int, input("Введите коэффициенты a, b, c: ").split())

print(f"Уравнение {a}x^4 + {b}x^2 + {c} = 0. В поле {n}")
print("Сделаем замену: x^2 = t")
D = discriminant(a, b, c, n)
print("D =", D)
t1, t2 = get_x(a, b, D, n)
print(f"t1 = {t1}; t2 = {t2}")

quadratic_deduction = get_quadratic_deduction(n)
if t1 in quadratic_deduction:
    print("x1 =", quadratic_deduction[t1], end="; ")
    print("x2 =", -quadratic_deduction[t1], f"= {module(n, -quadratic_deduction[t1])}")
else:
    print(f"t1 = {t1} - не вычет")
if t2 in quadratic_deduction:
    print("x3 =", quadratic_deduction[t2], end="; ")
    print("x4 =", -quadratic_deduction[t2], f"= {module(n, -quadratic_deduction[t2])}")
else:
    print(f"t2 = {t2} - не вычет")
