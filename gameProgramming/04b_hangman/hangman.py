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


# i = 0
# while i < 100:
#    word = getRandomWord(words)
#    print(word)
#    i += 1





