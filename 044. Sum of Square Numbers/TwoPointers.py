from math import sqrt
def judgeSquareSum(c):
    # Since we want two numbers "a" and "b" such that 
    # a^2 + b^2 = c
        
    # So, these two numbers should be in the range -> 0 to square root of "c"

    # We can use a two pointer approach where initially "a" is smallest possible value
    # and "b" is the largest possible value in the range 0 to sqrt(c)
    a = 0
    b = int(sqrt(c))
        
    while a <= b:
        value = (a * a) + (b * b)
            
        # If the result of expression is equal to "c", we found a pair
        if value == c: return True
            
        # If the value is less than "c", that means "a" needs to be increased
        # Because "b" is already a larger number among the two so "a" needs to be increased
        if value < c: a += 1
                
        # If the value is more than "c", that means "b" needs to be decreased
        # Because "a" is already a smaller number among the two
        else: b -= 1
            
        
    return False

c = 5
print("Output -> ", judgeSquareSum(c))