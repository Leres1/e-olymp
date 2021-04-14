# ----------------------------------------------------------------------------------------------------------------------
# Program reads two-digit number and prints every digit, separated by a space.
#
# Input
# One integer from 10 to 99 including.
#
# Output
# Two digits separated by a space.
# ----------------------------------------------------------------------------------------------------------------------

def func1(num):
    print(int(num / 10), num % 10, sep=' ')


func1(int(input()))
