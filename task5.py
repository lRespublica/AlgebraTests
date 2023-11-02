import sys
import math

""" Для красивой записи степеней """
def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

def errorMessage(str):
    print("Ошибка: " + str, file = sys.stderr)

def printPoly(poly, exp='x'):
    for i in range(len(poly) - 1):
        print(f"{poly[i]}*{exp}{superscript(len(poly) - 1 - i)} +", end = " ")
    print(f"{poly[-1]}", end=" ")

""" Деление с комментариями для комплексных чисел и округлением до 4 знака после запятой"""
def divide(a, b):
    if isinstance(b, complex):
        print(f"")
        print(f"===")
        print(f"Деление на комплексное число")
        print(f"{a} / {b}")
        print(f"{a} * {b.conjugate()} / {b} * {b.conjugate()}")
        print(f"{a * b.conjugate()} / {b * b.conjugate()}")
        print(f"{a / b}")
        print(f"===")

    return round(a / b, 4)

""" Создание списка с биноминальными коэффициентами """
def getBinominalList(deg):
    return [math.comb(deg, deg - x) for x in range(deg+1)]

""" Возведение в степень многочлена (x + changedValue) """
def getPoweredPoly(changedValue, deg):
    binominal = getBinominalList(deg)
    return [binominal[x] * (changedValue ** x) for x in range(deg + 1)]

""" Приведение некомплексных чисел к float """
def cleanFromComplex(list):
    for i in range(len(list)):
        if list[i].imag == 0:
            list[i] = list[i].real

"""
basePoly - изначальное уравнение
workPoly - уравнение, с которым происходит работа
isTransformed - потребовалось ли привести уравнение к стандартному виду
changedValue - значение -b/3a, не равно нулю если уравнение приводится к стандартному виду
curSymbol - символ, которым записывается переменная
"""
basePoly = []
workPoly = []
isTransformed = False
changedValue = 0
curSymbol = 'x'

print("ВВОД КОМПЛЕКСНЫХ ЧИСЕЛ ДОЛЖЕН ИСПОЛЬЗОВАТЬ СЛИТНУЮ ЗАПИСЬ И ЛИТЕРАЛ j")
print("Пример: 3.1+2j\n")
print("Введите 4 коэффициента кубического уравнения:")
basePoly = [complex(x) for x in input().split(maxsplit=4)[:4]]
cleanFromComplex(basePoly)

print("\nВы ввели многочлен:", end = " ")
printPoly(basePoly, curSymbol)
print("")

""" Проверка размера """
if len(basePoly) != 4:
    errorMessage("Необходимо ввести 4 коэффициента")
    sys.exit(1)

""" Проверка корректности ввода """
if basePoly[0] == 0:
    errorMessage("Ошибка: Многочлен не должен иметь коэффициент a = 0")
    sys.exit(1)

if basePoly[1] != 0:
    isTransformed = True
    curSymbol = 't'
    changedValue = - divide(basePoly[1],  3*basePoly[0])

    print("\nУравнение не в каноническом виде")
    print(f"Выполним замену: x = t - b/3a = x - {basePoly[1]}/{3*basePoly[0]} = x - {-changedValue}\n")

    printPoly(basePoly, f"(t - {-changedValue})")
    print("")

