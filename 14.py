# ----------------------------------------------------------------------------------------------------------------------
# On the stop we have N passengers, which Vanja and Peter were among, called at a trolleybus. The Vanja purchased a ticket
# the first. Peter glanced on the ticket and saw that the number of ticket is a prime number, and decided, that he must
# purchase a ticket with a simple number. Whether there is a chance at Peter to purchase a ticket to a next stop, if at a
# conductor only one roll of tickets, in the numbers of tickets is determined the amount by the bought ticket. In case if
# a roll is closed, Peter will stow "away", and he is expected by a failure.
#
# Input
# An entrance line contains two numbers: amount of passengers and number of trolleybus ticket. The amount of numbers in
# the number of ticket does not exceed 6.
#
# Output
# Show out the amount of passengers, which it is necessary to skip Peter, to purchase a ticket with a simple number, or
# –1, if doing it is impossible.
# ----------------------------------------------------------------------------------------------------------------------
nums = list(map(int, input().split()))


def primeNumbersTo(num):
    i = num
    if num == 1:
        return 2
    if num == 2:
        return 3
    while True:
        i += 2
        n = int(i ** 1 / 2)
        for j in range(2, n + 1):
            if j == n:
                return i
            if i % j == 0:
                break


finish = primeNumbersTo(nums[1])
# print(finish)
if finish <= nums[1] - 1 + nums[0]:
    print(finish - nums[1] - 1)
else:
    print('-1')

