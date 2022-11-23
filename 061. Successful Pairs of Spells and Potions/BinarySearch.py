def successfulPairs(spells, potions, success):
    output = [0] * len(spells)
        
    # Why did above solution gave TLE?
    # Because for every spell, we have to go through each potion
    # That is, we have to traverse the whole potions list for each spell
    # But, what if potions list was sorted?
    # In that case, as soon as we find a potion that can make a valid pair, 
    # All potions after that can also make a valid pair since list is sorted
    # And hence, we can use Binary Search instead of linear search
    potions.sort()

    # For each Spell
    for i,spell in enumerate(spells):
        # Find how many potions can be paired up with it
        # This time, we use Binary Search
        # We want the leftmost valid potion
        # Because we know that after that, all potions wil be valid only
            
        start = 0
        end = len(potions) - 1
        leftmostValidIndex = -1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            # If potion at "mid" makes a valid pair, it may be leftmost valid potion
            # But to be sure, we keep searching on left side of mid
            if spell * potions[mid] >= success:
                leftmostValidIndex = mid
                end = mid - 1
            else: start = mid + 1

        output[i] = 0 if leftmostValidIndex == -1 else len(potions) - leftmostValidIndex
            
    return output

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

print("Output -> ", successfulPairs(spells, potions, success))