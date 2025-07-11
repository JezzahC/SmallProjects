import random

allColours = ["R", "G", "B", "Y", "O", "W", "S", "P"]
colours = ["R", "G", "B", "Y", "O", "W", "S", "P"]
code = []
tries = 0

def setCode():
    if len(code) != 5:
        for i in range(5):
            code.append(colours.pop(random.randint(0, colours.index(colours[-1]))))
        random.shuffle(code)
        return code
    else:
        return code

def makeGuess(colour):
    incorrect = True
    while incorrect == True:
        guess: list = input(f"Enter a guess for the code. Use only 5 of these letters {' '.join(colour)}. There are no duplicates: ").upper()
        incorrect = False
        for guesses in guess:
            if guesses in allColours:
                continue
            else:
                incorrect = True
                break

        if incorrect == False:
            if len(guess) == 5:
                return list(guess)
            elif len(guess) == 10:
                guess: list = "".join(guess)
                return guess
            else:
                print("You have either too many or not enough colours. This will not effect your tries.")
                incorrect = True
        else:
            print("You had incorrect colours in your guess. This will not effect your tries.")

def checkGuessAndCode():
    guess: list = makeGuess(colour=allColours)
    correctColour = 0
    correctColourPlacement = 0
    codeStore = []
    guessStore = []
    indexStore = []
    index = -1

    for i in range(5):
        index += 1
        guessIndex = guess.pop(guess.index(guess[0]))
        codeIndex = code.pop(code.index(code[0]))
        if guessIndex == codeIndex:
            correctColourPlacement += 1
            codeStore.append(codeIndex)
            guessStore.append(guessIndex)
            indexStore.append(index)
        else:
            code.append(codeIndex)
            guess.append(guessIndex)

    if correctColourPlacement != 5:
        for i in range((5 - correctColourPlacement)):
            guessIndex = guess.pop(guess.index(guess[0]))
            if guessIndex in code:
                correctColour += 1
            else:
                pass
            guess.append(guessIndex)

    if len(codeStore) != 0:
        while len(indexStore) != 0:
            index = indexStore.pop(0)
            code.insert(index, codeStore.pop(0))
            guess.insert(index, guessStore.pop(0))
    else:
        pass

    if correctColourPlacement != 5:
        return f"Your guess {''.join(guess)} has {correctColourPlacement} colours in the right place and {correctColour} correct colours in the code."
    else:
        return True 

def main():
    completed = False
    code = setCode()
    tries = 0
    print("Welcome to Mastermind! You'll have 12 goes to guess the code!")
    for i in range(12):
        tries += 1
        verify = checkGuessAndCode()
        if verify == True:
            print(f"You got the code {''.join(code)} in {tries} tries!")
            completed = True
            break
        else:
            print(verify)

    if completed != True:
        print(f"You didn't guess the code! The code was {code}")
    else:
        print(f"You got the code {''.join(code)} in {tries} tries!")

if __name__ == "__main__":
    main()

print("Thanks for playing!")