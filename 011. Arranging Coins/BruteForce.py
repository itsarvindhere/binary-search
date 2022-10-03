def arrangeCoins(n):
    completeStairs = 0
        
    # i = row number
    i = 1
    while n >= 0:
        # For ith row, we use i coins to fill it completely
        # So reduce i coins from n
        n -= i
        # If n is not negative
        # that means this row can be fully filled so increment count of completeStairs
        if n >= 0: completeStairs += 1
        # Move to the next row
        i += 1

    return completeStairs


n = 5

print("Number of Completely Filled Rows -> ",  arrangeCoins(n))