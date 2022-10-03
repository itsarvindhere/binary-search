def arrangeCoins(n):
    completeStairs = 0
        
    # What is the lower bound?
    # Since n can be at least 1, that means we can have at least 1 complete row
    # So 1 is the lower bound here
    start = 1
    # And the upper bound can be n itself
    # But to further optimize, it can be at most (n + 1)/ 2
    end = (n + 1) // 2
        
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # Now we need to check how many coins would it take to completely fill "mid" rows
        # As we know, we have number of coins in each row in this pattern -> 1,2,3,4,5...
        # So, to completely fill lets say 3 rows, we need 1 + 2 + 3 coins right?
        # So instead of calculating the sum in O(n) time, we can calculate it in O(1) time using Gauss Summation
            
        if (mid * ( mid + 1)) // 2 <= n:
            completeStairs = mid
            start = mid + 1
        else:
            end = mid - 1


    return completeStairs


n = 5

print("Number of Completely Filled Rows -> ",  arrangeCoins(n))