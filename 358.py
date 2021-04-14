# ----------------------------------------------------------------------------------------------------------------------
# Artillery has always been a native troops, which were intensively used different counting devices. Once they were
# mechanical and showed the results of calculations by means of wheels with painted figures. However, progress was not
# on the spot. Once the designers have developed an electrical device, which shows the results using segmented
# indicators - LEDs.
#
# prb358
#
# First, the progress necessary to develop a program that, given the number determines the number of LEDs, which should
# catch fire in order to properly display a given number.
#
# Input
#
# Specific numberN (0 <= N <= 109)
#
# Output
#
# The desired number of LEDs.
# ----------------------------------------------------------------------------------------------------------------------
mas = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

num = input()
finish = 0
for i in range(0, len(num)):
    finish += mas[num[i]]

print(finish)
