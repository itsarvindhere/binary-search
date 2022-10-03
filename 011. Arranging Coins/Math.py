from math import sqrt
def arrangeCoins(n):
        return int(sqrt(2 * n + 0.25) - 0.50)


n = 5

print("Number of Completely Filled Rows -> ",  arrangeCoins(n))