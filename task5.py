import sys
import math

""" Для красивой записи степеней """
def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

def errorMessage(str):
    print("Ошибка: " + str, file = sys.stderr)

def printPoly(poly, exp='x'):
    poly = roundList(poly.copy())
    for i in range(len(poly) - 1):
        try:
            if poly[i] >= 0:
                print(f"{poly[i]}*{exp}{superscript(len(poly) - 1 - i)} +", end = " ")
            else:
                print(f"({poly[i]})*{exp}{superscript(len(poly) - 1 - i)} +", end = " ")
        except TypeError:
            print(f"{poly[i]}*{exp}{superscript(len(poly) - 1 - i)} +", end = " ")

    print(f"{poly[-1]}", end=" ")

def roundList(arr):
    for i in range(len(arr)):
        arr[i] = roundComplex(arr[i], 4)
    return arr

def roundComplex(val, size = 4):
    if isinstance(val, complex):
        val = round(val.real, size) + round(val.imag, size)*1j
    else:
        val = round(val, size)
    return val

def clearComplex(val):
    if isinstance(val, complex):
        if val.imag == 0:
            return val.real
        else:
            return val
    else:
        return val


""" Деление с комментариями для комплексных чисел и округлением до 4 знака после запятой"""
def divide(a, b):
    if isinstance(b, complex):
        num = roundComplex(a * b.conjugate(), 4)
        denum = roundComplex(b * b.conjugate(), 4)
        res = roundComplex(a/b, 4)
        print(f"===")
        print(f"Деление на комплексное число")
        print(f"{a} / {b}")
        print(f"{a} * {b.conjugate()} / {b} * {b.conjugate()}")
        print(f"{num} / {denum}")
        print(f"{res}")
        print(f"===")

    return a / b

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
basePoly = [0, 0, 0, 0]
workPoly = [0, 0, 0, 0]
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

if basePoly[0] != 1:
    print(f"Многочлен не приведён, разделим его на {basePoly[0]}")

    for i in reversed(range(len(basePoly))):
        basePoly[i] = divide(basePoly[i], basePoly[0])

    cleanFromComplex(basePoly)
    printPoly(basePoly, curSymbol)
    print("")

if basePoly[1] != 0:
    tmpPolyList = []
    isTransformed = True
    curSymbol = 't'
    changedValue = - divide(basePoly[1],  3*basePoly[0])
    printedValue = -roundComplex(changedValue, 4)

    print("\nУравнение не в каноническом виде")
    print(f"Выполним замену: x = t - b/3a = t - {roundComplex(basePoly[1], 4)}/{roundComplex(3*basePoly[0], 4)} = t - {printedValue}")

    print("\nПодставим t в выражение:")
    printPoly(basePoly, f"(t - {printedValue})")
    print("\n\nРаскрываем скобки:")

    """ Список содержащий многочлены (t + changedValue)^n"""
    tmpPolyList = [getPoweredPoly(changedValue, x) for x in range(len(basePoly) - 1, 0, -1)]
    for i in range(len(tmpPolyList)):
        printPoly(tmpPolyList[i], curSymbol)
        print("+", end = " ")

        """ Заполняем нулями в начале, для однозначного сопоставления коэффициентов """
        while len(tmpPolyList[i]) < len(basePoly):
            tmpPolyList[i].insert(0, 0)

        """ Умножаем на коэффициенты при соответствующей степени выражения и записываем в workPoly """
        for j in range(len(tmpPolyList[i])):
            tmpPolyList[i][j] *= basePoly[i]
            workPoly[j] += tmpPolyList[i][j]
    workPoly[-1] += basePoly[-1]
    cleanFromComplex(workPoly)

    print(roundComplex(basePoly[-1], 4))
    print("\nПриведём подобные:")
    printPoly(workPoly, curSymbol)
    print("")

else:
    workPoly = basePoly
    print("\nУравнение в каноническом виде")
