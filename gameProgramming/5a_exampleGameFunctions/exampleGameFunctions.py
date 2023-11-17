# Example Game FUNCTIONS project, Albert Laguerre, v0.0
import random

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rollDice = 0
    rounds = 1
    numberofDice = 2
    diceRoll = 0
    

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1

def numberofDice(numDice, sizeDice):
    numberofDice = 2
    sum = 2

    
def diceRoll(param1):
    diceRoll = random.randint(1, 6)
    return diceRoll

def rounds(param1, param2, param3):
    print("Round " + str(rounds))
    player1 = rollDice()
    player2 = rollDice()
    print("Player 1 Roll: " + str(player1))
    print("Player 2 Roll: " + str(player2))

    if player1 == player2:
        print("Draw!")
    elif player1 > player2:
        player1wins = player1wins + 1
        print("Player 1 wins!")
    else:
        player2wins = player2wins + 1
        print("Player 2 wins!")
    
    rounds = rounds + 1 

    if player1wins == player2wins:
        print("Draw!")
    elif player1wins > player2wins:
        print("Player 1 Wins! ")
    else:
        print("Player 2 Wins! ")
    





