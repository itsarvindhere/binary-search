def guess(guess, validGuess = 7):
    if guess == validGuess: return 0
    if guess < validGuess: return 1
    if guess > validGuess: return -1


def guessNumber(n):
    start = 1
    end = n
    steps = 0
    while start <= end:
        steps += 1
        mid = start + (end - start) // 2
        # Get the result from Guess API
        res = guess(mid)
        # If this value is same as guessed number
        if res == 0:
            print("Correct Guess! You guessed in ", steps , 
            (" steps" if steps > 1 else " step"))
            print("Number I picked was -> ", mid)
            return
        # If this value is lower than guessed number
        # Then all values lower than this number are also invalid guesses
        if res == 1: start = mid + 1
        # If this value is higher than guessed number
        # Then all values higher than this number are also invalid guesses
        else: end = mid - 1
        
    return 0

guessNumber(10)