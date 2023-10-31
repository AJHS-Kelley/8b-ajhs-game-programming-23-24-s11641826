# Hangman Game by Albert Laguerre, v0.2

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
