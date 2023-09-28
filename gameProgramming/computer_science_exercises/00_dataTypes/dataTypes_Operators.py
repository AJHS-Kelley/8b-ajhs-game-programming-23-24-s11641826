# Data Types and Operators, Albert Laguerre, v0.5

# Variable Rules
# CANNOT START WITH A NUMBER!!!!!!!!
# CANNOT USE BUILT-IN KEYWORDS AS VARIABLES.
# VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORED.
# snake_case variables use _ to sparate words, all lower case.
# camelCase variables do not use spaces, 1t word lower, rest upper.

# String liiteral Examples
playerName = "Timmy Turner"
emptyString = ""
spaceString = " "
monsterName = "Mr. Crocker"

# Integer Data Type
health = 100
extralives = 5
temperature = -17

#Floating Point Data Type 
pi = 3.1415678
lapTime = 3.5
velocity = -2.0

# Boolean Data Types
isFireType = False
weaponEquipped = True 
pvpEnabled = False 

# Arithmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(31 + -11) # Addition
print(15 - 30) # Subtraction
print(6 * -4) # Multipulcation
print(9 / 3) # Division
print(6 ** 7) # Exponents
print(15 % 5) # Modulus -- Divides, then returns remainder , most commonly used to determan odd/even

# Comparrison Operators
# Evaluate the expression, then return True or False
print(5 > 3) # Greater Than
print(7 >= -1) # Greater Than or Equal To 
print(-1 < 2) # Less Than
print(0 <= 0) # Less Than or Equal To 
print(5 == 3) # Is Equal To
print(-99 != 99) # Not Equal To

# Assignment Operators
myVariable = "myValue" # Assign variable on the left the value on the right, throw away any recent value
myOtherVariable = (10 + 5)

# Addition Assignment -- Add the value on the right, keeping any current value
myWallet = 0
myWallet += 1 
myWallet += 5
print(myWallet)

# Same Effect
x = 0 
x += 1
x = x + 1

# Logical Operators
print(3 > 5 and 4 < 3) # AND reqires ALL expressions to be True.
print(3 > 2 and 4 < 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and favColor == "Blue" and temp == -5)
# When writing and expressions, put the value most likely to be False first!

# Logical or -- Requries One expression to be true.
print(5 > 2 or 2 <-2)
print(3 != 3 or 5 == 5)

# AND OR COMBINED 
print("Line 81")
print( 3 > 2 and 4 < 3 or 5 != 7)
# print(True and False or True)

# NOT Logical Operatior
print(not(3 >2))
print(not (not (not (5 != 3) )))