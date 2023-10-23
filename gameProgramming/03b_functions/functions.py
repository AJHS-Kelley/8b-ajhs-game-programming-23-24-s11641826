# FUNCTIONS -- a named piece of code that can be reused easily.
# FUNCTIONS SIGNATURE -- Syntax for creating a new function
def exampleFunction(): #NO PARAMETERS
    count = 0
    num = int(input("How many time do you want to wish a happy birthday?"))
    while count < num:
        print("Happy Birthday!\n")
        count += 1

def exampleFunction(num, count): # PARAMETERS
    while count < num:
        print("Happy Birthday!\n")
        count += 1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM!

# RUNNING A FUNCTION IS KNOWN AS CALLING THE FUNCTION
exampleFunctionA = 0
exampleFunctionB = 0
exampleFunctionA()
exampleFunctionB(5, 0)