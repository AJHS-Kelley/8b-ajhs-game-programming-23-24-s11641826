# This is a method for testing ocde and preventing crashes.
# try -- except -- else -- finally

try: # The code in this lbock is ALWAYS executing 
    myVariable = 1
    print(myVariable)
    myString = "Five"
    print(float(myString))
except NameError: # this code will run IF there is an error
    print("There is an incorrect variable name in your code")
except:
    print("Something else went wrong")
else: # this code runs if there are NO errors
    print("Code executed correctly with no exceptions.\n")
finally: # this code always runs, its like the terminator
    print("Ill be back.\n")

#except NameError:
#    pass