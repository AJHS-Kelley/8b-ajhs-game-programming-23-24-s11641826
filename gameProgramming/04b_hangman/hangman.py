# Hangman Game by Albert Laguerre, v0.3
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

i = 0
while i < 100:
    word = getRandomWord(words)
    print(word)
    i += 1





