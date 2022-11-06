def reachNumber(target):
    target = abs(target)
        
    moves = 0
    pos = 0
        
    # First, try to make moves till we get to target or more than target
    while pos < target:
        moves += 1
        pos += moves
            
    # Now, pos is either equal to target or more than target
    # If it is equal, we can simply return moves.
    if pos == target: return moves
        
    # But if it is more than target, we have to make sure "pos - target" is even
    # If not, we need to increase moves till we get even
    while (pos - target) % 2 != 0:
        moves += 1
        pos += moves
            
     # Once (pos - target) is even, the number of moves is the required output
    return moves

target = 8

print("Minimum Number of moves -> ", reachNumber(target))