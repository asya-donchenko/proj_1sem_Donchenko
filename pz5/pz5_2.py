# 2. Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
# положительного числа K, а также их сумму S (K — входной, C и S — выходные
# параметры целого типа). С помощью этой функции найти количество и сумму цифр
# для каждого из пяти данных целых чисел.

import random


def DigitCountSum(K, Result):
    s = str(K)
    n = len(s)
    _sum = 0

    for i in range(n):
        _sum += int(s[i])
    Result['C'] = n
    Result['S'] = _sum


R = {'C': None, 'S': None}

for i in range(5):
    K = random.randrange(1, 10000)
    print("Число ", i + 1, ": ", K)
    DigitCountSum(K, R)
    print('Количество цифр = ', R['C'])
    print('Сумма цифр = ', R['S'])
    print()
