# ----------------------------------------------------------------------------------------------------------------------
# Count the sum of two natural numbers A and B, which have written in roman system of numeration. The answer you must
# write too in roman system of numeration.
#
# M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1 (all numbers is less 2000).
#
# Input
# In line wrote two number of roman system numeration, between which stand mark "+".
#
# Output
# One number, sum of numbers is roman system numeration too. Numbers in roman system numeration wrote big Latin letters.
# ----------------------------------------------------------------------------------------------------------------------
d = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}  # словарь

b = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM',
    1000: 'M',
    2000: 'MM',
    3000: 'MMM'
}


def toNum(num):
    last = ''
    finish_sum = 0
    for i in num[::-1]:
        now = i
        if last != '':
            if d[last] < d[now]:
                finish_sum += d[last]
                last = now
                now = ''
            if now != '':
                if d[last] == d[now]:
                    finish_sum += d[last]
                    last = now
                if d[last] > d[now]:
                    finish_sum += d[last] - d[now]
                    last = ''
                    now = ''
        else:
            last = now
    if last != '':
        finish_sum += d[last]
    return finish_sum


def sumNum(_list):
    return toNum(_list[0]) + toNum(_list[1])


def toRoman(num):  # '123'
    _length = len(num) - 1
    Roman = ''
    for i in num:
        if i == '0':
            _length -= 1
            continue
        Roman += b[int(i + '0' * _length)]
        _length -= 1
    return Roman


print(toRoman(str(sumNum(list(input().split('+'))))))