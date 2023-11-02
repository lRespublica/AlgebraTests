import sys

# Для красоты -
def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

"""
basePoly - изначальное уравнение
workPoly - уравнение, с которым происходит работа
"""
basePoly = []
workPoly = []
isTransformed = False

print("Введите 4 коэффициента кубического уравнения:")
basePoly = [float(x) for x in input().split(maxsplit=4)[:4]]

if len(basePoly) != 4:
    print("Требуется ровно 4 коэффициента", file=sys.stderr)
    sys.exit(1)

if basePoly[0] == 0:
    print("Многочлен не должен иметь коэффициент a = 0", file=sys.stderr)
    sys.exit(1)

