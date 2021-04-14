# ----------------------------------------------------------------------------------------------------------------------
# Lets write the decimal integer n in binary notation and create all its left cycle shifts where first digit of the
# number goes to the end.
#
# For example, if n = 11, than it will be 1011 in binary notation, cycle shifts are 0111, 1110, 1101, 1011. So the
# maximal value m among all received numbers equals to 11102 = 1410.
#
# For the number n find the maximal value of m.prb27
#
# Input
# One number n (1 ≤ n ≤ 2 ·109).
#
# Output
# One number m.
# ----------------------------------------------------------------------------------------------------------------------
num = int(input())


def toTwo(n):
    two = ''
    i = 2
    for j in range(0, 100000000):
        if n - i ** j <= 0:
            for k in range(0, j)[::-1]:
                if n - i ** k >= 0:
                    n = n - i ** k
                    two += '1'
                else:
                    two += '0'
            return two


def ToInt(n):
    i = 2
    finish = 0
    for j in range(0, len(n))[::-1]:
        finish += int(n[j]) * (i ** (len(n) - j - 1))
    return finish


def giveMax(n):
    some = toTwo(n)
    finishMax = 0
    for i in range(0, len(some)):
        Max = ToInt(some)
        if Max > finishMax:
            finishMax = Max
        some += some[0]
        some = some[1:]
    return finishMax


# print(toTwo(num))
# print(ToInt(toTwo(num)))
print(giveMax(num))
