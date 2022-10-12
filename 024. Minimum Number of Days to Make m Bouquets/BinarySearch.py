# Helper method to check if after waiting certain number of days We can make m bouquets
def isValid(days, bloomDay, m, k):
    bouquets = 0
    flowerCount = 0
        
    for day in bloomDay:
        # If we have to wait <= "days" for this flower, increment flowerCount 
        if day <= days: flowerCount += 1
        # Otherwise we have to reset flowerCount because we can only take adjacent flowers
        else: flowerCount = 0
            
        # If we got k flowers, we can make one bouquet. So increment bouquet count and also reset flowerCount
        if flowerCount == k: 
            bouquets += 1
            flowerCount = 0
                
    # If we can make at least m bouquet after waiting "days" days then return True
    return bouquets >= m
    
def minDays(bloomDay, m, k):  
    # For one bouquet, we need k flowers
    # For m bouquet, we need m * k flowers
    # And length of array = flowers we have
        
    # If we don't have enough flowers at all
        
    if len(bloomDay) < m * k: return -1
        
        
    # Binary Search on Answer
    # We want the minimum number of days to wait to make m bouquets
        
        
    # What is the lower bound for minimum days to wait?
    # It is the lowest value in bloomDay, right?
    # What is the upper bound? It is the highest value.
        
    start = min(bloomDay)
    end  = max(bloomDay)
    result = -1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # We need to check if after waiting for mid days, we can make m bouquets
            
        if isValid(mid, bloomDay, m, k):
            # If we can wait mid days for m bouquets, this is one possible solution
            # But since we want minimum days to wait, we keep searching for a lower possible valid value
                
            result = mid
            end = mid - 1
        else:
            start = mid + 1
                
    return result

bloomDay = [1,10,3,10,2]
m = 3
k = 1

print("Minimum Days to wait -> ", minDays(bloomDay, m, k))