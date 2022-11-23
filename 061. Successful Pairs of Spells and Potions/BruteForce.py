def successfulPairs(spells, potions, success):
    output = [0] * len(spells)
        
    # For each Spell
    for i,spell in enumerate(spells):
        count = 0
        # Find how many potions can be paired up with it
        for potion in potions:
            if spell * potion >= success: count += 1
            
        # And finally, set the count for that spell in the output array
        output[i] = count
    return output

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

print("Output -> ", successfulPairs(spells, potions, success))