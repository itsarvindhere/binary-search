def fullBloomFlowers(flowers, persons):
    output = []
        
    # For each person's arriving time
    # We will count how many flowers will be in full bloom
    for time in persons:
        count = 0
        for start, end in flowers:
            # When the person arrives
            # If this flower is in full bloom
            # We increment the count
            if time >= start and time <= end: 
                count += 1
            
            
        output.append(count)
            
            
    return output

flowers = [[1,6],[3,7],[9,12],[4,13]]
persons = [2,3,7,11]

print("Output -> ", fullBloomFlowers(flowers, persons))