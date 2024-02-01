# DNA Replication Game, Ryan Kelly, v0.0

# Import Entired Modules -- Get the whole tool box.
import time, datetime

# Import Specific Methods -- Get the specific tool.
from random import choice

# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please neter a positive integer number of bases to generate.\n"))
    dnaSequence = ""
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

# dna = genDNA()
# print(dna)

dna = genDNA()

def doTranscription(dnaSequence: str) -> tuple:
    
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence. \n")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan. 01, 1970
    rnaSequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press enter.\n").enter 
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can reference elements with the index
    # Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating
    # Tuples CAN have duplicate values

def verifySequence(dnaSequence: str, rnaSeqeunce: str) -> bool:
    isMatch = False 
    if len(dnaSequence) != len(rnaSeqeunce):
        print("The seqeunce are different lengths and cannot match.\n")
        return isMatch 
    for dnaBase, rnaBase in zip(dnaSequence, rnaSeqeunce):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase == "C" and rnaBase == "G":
            isMatch = True
        elif dnaBase == "G" and rnaBase == "C":
            isMatch = True
        elif dnaBase == "T" and rnaBase == "A":
            isMatch = True
        else:
            print("Sorry these dnaBases dont match, please try again.\n")
    return isMatch



