import sys

""" Для красивой записи степеней """
def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

def errorMessage(str):
    print("Ошибка: " + str, file = sys.stderr)

""" Деление с комментариями для комплексных чисел """
def divide(a, b):
    if isinstance(b, complex):
        print("Деление на комплексное число")
        print(f"{a} / {b}")
        print(f"{a} * {b.conjugate()} / {b} * {b.conjugate()}")
        print(f"{a * b.conjugate()} / {b * b.conjugate()}")
        print(f"{a / b}")
        print(f"")

    return a / b

"""
basePoly - изначальное уравнение
workPoly - уравнение, с которым происходит работа
isTransformed - потребовалось ли привести число к стандартному виду
"""
basePoly = []
workPoly = []
isTransformed = False

print("ВВОД КОМПЛЕКСНЫХ ЧИСЕЛ ДОЛЖЕН ИСПОЛЬЗОВАТЬ СЛИТНУЮ ЗАПИСЬ И ЛИТЕРАЛ j")
print("Пример: 3.1+2j\n")
print("Введите 4 коэффициента кубического уравнения:")
basePoly = [complex(x) for x in input().split(maxsplit=4)[:4]]

print("Вы ввели многочлен:", end = " ")
for i in range(len(basePoly)):
    print(

""" Проверка размера """
if len(basePoly) != 4:
    errorMessage("Необходимо ввести 4 коэффициента")
    sys.exit(1)

""" Проверка корректности ввода """
if basePoly[0] == 0:
    errorMessage("Ошибка: Многочлен не должен иметь коэффициент a = 0")
    sys.exit(1)

if basePoly[0] != 1
