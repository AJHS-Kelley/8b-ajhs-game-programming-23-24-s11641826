import dice


roll1 = dice.display(1, 6)
roll2 = dice.display(1, 6)

#if dice.isDoubles(roll1, roll2):
#    print("You rolled a double, go again!\n")
#else:
#    print("It was not a double.\n")

if dice.isExploding(roll1, 6):
    print(roll1)
    print("This roll exploded!\n")
    roll1 += dice.roll(1, 6)
    print(roll1)



