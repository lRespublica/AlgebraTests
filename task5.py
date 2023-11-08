import sys
import cmath
import math

""" Для красивой записи степеней """
def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

def subscript(n):
    return "".join(["₀₁₂₃₄₅₆₇₈₉"[ord(c)-ord('0')] for c in str(n)])

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
        if val.imag == 0 or abs(val.imag) < 1e-4:
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
def cleanFromComplex(arr):
    for i in range(len(arr)):
        arr[i] = clearComplex(arr[i])

""" Извлечение комплексных корней """
def complexRootExtraction(val, deg):
    if not isinstance(val, complex):
        val = val+0j

    roots = []
    a = val.real
    b = val.imag

    mod = math.sqrt(a**2 + b**2)
    if a >= 0 and b >= 0:
        arg = math.atan(b/a)
    elif a < 0 and b >= 0:
        arg = (math.pi/2) + math.atan(abs(a/b))
    elif a >= 0 and b < 0:
        arg = - math.atan(abs(b/a))
    else:
        arg = (math.pi/2) + math.atan(abs(b/a))
    cosz = math.cos(arg)
    sinz = math.sin(arg)
    trig = complex(cosz, sinz)

    print(f"\nНачинаем извлечения корня {deg} степени из {roundComplex(val)}")
    print(f"\nДля начала требуется привести число к тригонометрической форме:")
    print(f"a = {roundComplex(a)}; b = {roundComplex(b)};")
    print(f"|z| = √(a{superscript(2)} + b{superscript(2)}) = √({roundComplex(a**2)} + {roundComplex(b**2)}) = {roundComplex(mod)}")
    if a >= 0 and b >= 0:
        print(f"φ = atan(b/a) = atan({roundComplex(b)}/{roundComplex(a)}) = {roundComplex(arg)}")
    elif a < 0 and b >= 0:
        print(f"φ = π/2 + atan(|a/b|) = π/2 + atan(|{roundComplex(a)}/{roundComplex(b)}|) = π/2 + atan({roundComplex((abs(a/b)))}) = π/2 + {roundComplex(math.atan(abs(a/b)))} = {roundComplex(arg)}")
    elif a >= 0 and b < 0:
        print(f"φ = - atan(|b/a|) = - atan(|{roundComplex(b)}/{roundComplex(a)}|) = - {roundComplex(math.atan(abs(a/b)))} = {roundComplex(arg)}")
    else:
        print(f"φ = π/2 + atan(|b/a|) = π/2 + atan(|{roundComplex(b)}/{roundComplex(a)}|) = π/2 + {roundComplex(math.atan(abs(b/a)))} = {roundComplex(arg)}")
    print(f"sin(φ) = sin({roundComplex(arg)}) = {roundComplex(sinz)}; cos(φ) = cos({roundComplex(arg)}) = {roundComplex(cosz)}")
    print(f"\nz = {roundComplex(mod)}*{roundComplex(trig)}")
    print(f"\nДля извлечения корня воспользуемся теоремой Муавра")
    print(f"ᶰ√z = ᶰ√|z| * (cos[(φ+2πk)/n] + sin[(φ+2πk)/n]j")

    mod = mod ** (1/deg)
    for i in range(deg):
        angel = (arg + 2*i*math.pi)/deg
        cosz = math.cos(angel)
        sinz = math.sin(angel)
        trig = complex(cosz, sinz)
        roots.append(clearComplex(mod*trig))

        print(f"\nВозьмём k = {i}")
        print(f"φ{subscript(i)} = ({roundComplex(arg)} + {roundComplex(2*math.pi)}*{i})/{deg} = {roundComplex(angel)}")
        print(f"cos (φ{subscript(i)}) = {roundComplex(cosz)}")
        print(f"sin (φ{subscript(i)}) = {roundComplex(sinz)}")
        print(f"{superscript(deg)}√z = {roundComplex(mod)} * {roundComplex(trig)} = {roundComplex(roots[i])}")

    return roots


"""
basePoly - изначальное уравнение
workPoly - уравнение, с которым происходит работа
answers - корни уравнения
isTransformed - потребовалось ли привести уравнение к стандартному виду
changedValue - значение -b/3a, не равно нулю если уравнение приводится к стандартному виду
curSymbol - символ, которым записывается переменная
"""
basePoly = [0, 0, 0, 0]
workPoly = [0, 0, 0, 0]
answers = []
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
    changedValue = -divide(basePoly[1],  3*basePoly[0])
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

q = workPoly[-1]
p = workPoly[-2]
print(f"q = {roundComplex(q)}; p = {roundComplex(p)}")

print("\nПриступаем к решению:")
D = (q**2)/4 + (p**3)/27
print(f"Считаем D = q{superscript(2)}/4 + p{superscript(3)}/27 = {roundComplex(q**2)}/4", end = " ")
print(f"+ {roundComplex(p**3)}/27 = {roundComplex(q**2/4)} + {roundComplex(p**3/27)} = {roundComplex(D)}")

""" Приводим D, к float, если оно не комплексное """
D = clearComplex(D)

if(not isinstance(D, complex)):
    print("D - вещественное и", end = " ")
    if D > 0:
        print("> 0, следовательно имеет один вещественный и два комплексных корня)")
    elif D == 0:
        print("= 0, следовательно имеет три вещественных корня, из которых два - кратные")
    else:
        print("< 0, следовательно имеет три различных вещественных корня")
else:
    complexRootExtraction(D, 2)

alphaPowered = -q/2 + cmath.sqrt(D)

print(f"\nСчитаем корни")
print(f"α{superscript(3)} = -q/2 + √D = {-roundComplex(q)}/2 + {roundComplex(cmath.sqrt(D))} = {-roundComplex(q)/2} + {roundComplex(cmath.sqrt(D))} = {roundComplex(alphaPowered)}")

alphaRoots = complexRootExtraction(alphaPowered, 3)

for i in range(len(alphaRoots)):
    alpha = alphaRoots[i]
    beta = (-p/3) / alpha
    answers.append(alpha + beta)

    print(f"\nКорень {i+1}")
    print(f"{curSymbol}{subscript(i+1)} = α{subscript(i+1)} + β{subscript(i+1)}")
    print(f"α{subscript(i+1)} = {roundComplex(alpha)}")
    print(f"β{subscript(i+1)} = -p/(3 * α{subscript(i+1)}) = {roundComplex(-p)}/3*(1/{roundComplex(alpha)}) = {roundComplex(-p/3)}/{roundComplex(alpha)} = {roundComplex(beta)}")
    print(f"{curSymbol}{subscript(i+1)} = {roundComplex(alpha)} + {roundComplex(beta)} = {roundComplex(answers[i])}")

if isTransformed:
    print("\nВозвращаемся к x:")
    for i in range(len(answers)):
        print(f"x{subscript(i)}={roundComplex(answers[i])} + {roundComplex(changedValue)} = {roundComplex(answers[i] + changedValue)}")
        answers[i] += changedValue
