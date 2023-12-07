# Example Game FUNCTIONS project, Albert Laguerre, v0.0
import random

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rollDice = 0
    rounds = 1
    

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1


def diceRoll():
    diceRoll = random.randint(1, 6)
    return diceRoll


dice = int(input("Dice: "))

if (dice <= 0):
    print("Must at least have one dice!")

sides = int(input("Sides: "))

if (sides <= 0):
    print("Must at least have one side!")

roll = []

for i in range(0,dice):
    face = random.randint(1,sides)
    roll.append(face)

print(roll)

random.randint(1,6)

def rounds():
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

    





