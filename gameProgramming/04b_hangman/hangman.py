# Hangman Game by Albert Laguerre, v0.6
import random
words = 'cat cow dog elephant sheep lion snack mouse cheetah bat red blue yellow orange black white purple pink violet silver phytoplanton mitochondria supercalifragilistiexpiealadous Sesquipedalian Antidisestablishmentarianism aintbiotics'

# VARIABLE_NAMES IN ALL-CAPS ARE CONSTANTS AND NOT MEAN TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |           
        |            
     =======''', '''   
    +---+
    O   |
        |           
        |            
     =======''', '''   
    +---+
    O   |
   /|     |           
        |            
     =======''', '''   
  +---+
    O   |
   /|\  |           
        |            
     =======''', ''' 
    +---+
    O   |
   /|\  |           
   /    |            
     =======''', '''   
    +---+
    O   |
   /|\  |           
   / \  |            
     =======''']

i = 0
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i += 1

# Pick Word from List
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordList) - 1)
    # len(listName) - 1 is EXTRAMELY COMMON FOR WORKING WITH LISTS
    return wordList[wordIndex]

def displayBoard(missedLetters,  correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end =' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()
    
    blanks = '_' * len(secretWord)

    # Replace Blanks with correct letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters: 
            blanks = blanks[:i] + secretWord[i] + blanks[i:1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter and press enter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print(' Please enter a single letter.') 
        elif guess in alreadyGuessed:
            print(' Letter has been guessed already, try again.')
        elif guess not in 'abcdefghjklmnopqrstuvwxyz':
            print(' Please guess a LETTER from the english alphabet.')
        else:
            return guess 

def playAgain():
    print(' Do you want to play again? Yes or No?')
    return input().lower().startswith('y')

# Introduce the game
print('Welcome to Hangman by Albert L.')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# MAin Game Loop
while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check to see if winner, winner checken dinner
        foundAllLetters = True 
        for i in range (len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:     # if true:
                print('Much wow! Very win! Well done.')
                print('The secret word was' + secretWord)
                gameIsDone = True 
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses and lost the game.')
            print('You made this number of correct guesses ' + str(len(correctLetters)))
            print('The secret word was ' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break







