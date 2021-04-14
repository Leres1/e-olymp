# ----------------------------------------------------------------------------------------------------------------------
# n pirates fairly divided the treasure of m gold coins - everyone got his part according to their rank and seniority
# pirate. Youngest pirate took a coin and each pirate taking on the next one coin more than the previous colleague.
# The last was the captain, who got twice as much of the plan, it is obvious that after the coins are no more.
#
# How many pirates along with the captain, if we know a and m. Since the captain without a team just a pirate,
# then n > 1.
#
# Input
# Two positive integers a and m (1 ≤ a ≤ 100, m < 15150). Input values are correct.
#
# Output
# The number of pirates n.
# ----------------------------------------------------------------------------------------------------------------------
def func(list_):
    num = list_[0]  # 5
    count = list_[1]  # 25
    sum = 0
    pirats = 1
    while(True):
        sum += num
        pirats += 1
        if sum + (num + 1) * 2 != count:
            num += 1
        else:
            return pirats


print(func(list(map(int, input().split()))))