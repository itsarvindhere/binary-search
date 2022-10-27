def numFriendRequests(ages):
    requestCount = 0
        
    # For every person, we need to find how many friend requests he/she can make
    for i in range(len(ages)):
        for j in range(len(ages)):
                
            if i != j:
                # A person "x" can send a request to "y if
                # age[y] > 0.5 * age[x] + 7
                # and age[y] <= age[x]
                    
                condition1 = ages[j] > 0.5 * ages[i] + 7
                condition2 = ages[j] <= ages[i]
                
                if (condition1 and condition2): requestCount += 1

    return requestCount


ages = [20,30,100,110,120]
print("Total Number of Friend Requests -> ", numFriendRequests(ages))