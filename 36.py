# ----------------------------------------------------------------------------------------------------------------------
# In some kingdom Gorynych the Dragon lived.He had N heads and M tails. Ivan-Tsarevich decided slaythe ruiner of human
# souls, and for this his godmother, Baba-Yaga, presented to him a magic sword, because only it he can kill Gorynych
# the Dragon. If he cuts off one head, than on that place grows up new head. If he cuts off tail than on that place
# grows up two tails. If he cuts off two tails, than grows up 1 head. When he cuts off 2 heads only, than grows up
# nothing. Gorynych, dragon dies in situation when Ivan-Tsarevich cuts off all heads and all tails. Find the minimal
# quantity of impacts by sword for slaying Gorynych the Dragon.
#
# Input
#
# Two numbers N, M (0 ≤ N, M ≤ 1000).
#
# Output
#
# A unique number, which is the minimal quantity of impacts by sword, or -1, if the slaying of Gorynych the Dragon is
# impossible.
# ----------------------------------------------------------------------------------------------------------------------
num = list(map(int, input().split()))

num2 = num[0]
num1 = num[1]
finish = 0
if num1 == 0 and not (num2 % 2 == 0):
    print('-1')
else:
    while True:
        if num1 % 2 == 0:
            if (int(num1 / 2) + num2) % 2 == 0:
                break
        num1 += 1
        finish += 1

    print(int(finish + ((int(num1 / 2) + num2) / 2) + num1 / 2))
