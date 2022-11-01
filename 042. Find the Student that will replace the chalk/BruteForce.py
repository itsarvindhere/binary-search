def chalkReplacer(chalk, k):
    i = 0
    n = len(chalk)
        
    while chalk[i] <= k:
        k -= chalk[i]
        i += 1
        if i == n: i = 0
                
    return i

chalk = [3,4,1,2]
k = 25

print("Student that will replace chalk -> ", chalkReplacer(chalk, k))