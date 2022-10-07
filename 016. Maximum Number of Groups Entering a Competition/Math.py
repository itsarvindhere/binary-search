from math import sqrt
def maximumGroups(grades):
        # Because we know the formula for a particular number of groups to be valid is
        # x * (x + 1) / 2 <= n
        # If we try to find x value out of this equation we get
        # x <= sqrt(2*n + 0.25) - 0.5
        
        # So, any value x is valid if above condition is valid. 
        # And largest value of x that is valid will be the one for which
        # x == sqrt(2*n + 0.25) - 0.5
        
        return int(sqrt(2 * len(grades) + 0.25) - 0.50)
        

grades = [10,6,12,7,3,5]
print("Maximum Number of Groups -> ", maximumGroups(grades))