# Example Game FUNCTIONS project, Albert Laguerre, v0.0
import random

rollDice = 0
numberofDice = 2
betAmount = ''
numberofPlayers = ''

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1

def numberofDice(param1):
    pass
    
def betAmount(param1):
    pass

def numberofPlayers(param1, param2, param3):
    pass




