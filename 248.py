# ----------------------------------------------------------------------------------------------------------------------
# Mom asked Vasya to water all the young trees in the garden. Vasya knows that while trees are small, they must be very
# well watered. But how much to water - is unknown. But Vasya is a very clever boy. He carefully read the entire
# textbook of botany for secondary schools and found that irrigation is directly proportional to the number of leaves
# on the tree. For a good tree growth enough to pour under the tree every day for one liter of water for each leaf.
#
# Fortunately Wasya found that the leaves on the trees are growing in layers, with the upper layer of two leafs,
# the second - four at the next - six, and so on, at each successive layer two leafs more than at previous one.
# And at the very tip of growing another leaf. Sly Vasya sent his younger sister Masha to count the number of layers
# for each tree, and asks you to write a program that for each tree compute the number of liters of water for its
# irrigation.
#
# Input
# The number of layers n (0 ≤ n ≤ 1000) in the tree.
#
# Output
# Print the number of liters of water to pour the tree.
# ----------------------------------------------------------------------------------------------------------------------
num = int(input())


def func(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    nums = 3
    sums = 2
    for i in range(1, n):
        sums += 2
        nums += sums
    else:
        return nums


print(func(num))
