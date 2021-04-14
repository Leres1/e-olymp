# ----------------------------------------------------------------------------------------------------------------------
# You have a positive integer m. If it is not a palindrome, than we write it in back order and add it to original number
# m. Steps are repeated till we'll receive a number - palindrome. The number of such operations we call the palindrome
# level for m.
#
# Find the level of palindrome for m.
#
# Input
# One number m (0 < m < 10000).
#
# Output
# Print the palindrome level for m.
# ----------------------------------------------------------------------------------------------------------------------
num = input()


def ChekPalindrome(txt):
    if len(txt) % 2 == 0:
        return txt[:int(len(txt) / 2)] == txt[int(len(txt) / 2):][::-1]
    else:
        return txt[:int(len(txt) / 2)] == txt[int(len(txt) / 2 + 1):][::-1]


def func(txt):
    i = 0
    while True:
        if not ChekPalindrome(txt):
            txt = str(int(txt) + int(txt[::-1]))
            i += 1
        else:
            return i


print(func(num))
