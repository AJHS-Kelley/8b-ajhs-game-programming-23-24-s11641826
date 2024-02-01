# DNA Replication Game, Albert Laguerre, v0.0

import random

class DNASequence:
    nucleotides = ['A', 'C', 'G', 'T']

    def __init__(self, length):
        self.sequence = ''.join(random.choice(self.nucleotides) for _ in range(length))

def display_sequence(self):
        return self.sequence

class DNAGame:
    def __init__(self, length):
        self.target_sequence = DNASequence(length)
        self.attempts = 0

    def play(self):
        print("Welcome to the DNA Guessing Game!")
        print("Try to guess the DNA sequence.")
        print("The sequence contains only 'A', 'C', 'G', and 'T'.")
        print(f"The DNA sequence has a length of {len(self.target_sequence.display_sequence())} bases.")

while True:
            try:
                guess = input("Enter your guess: ")

                if guess.upper() == self.target_sequence.display_sequence():
                    print(f"Congratulations! You guessed the correct DNA sequence: {self.target_sequence.display_sequence()}")
                    print(f"It took you {self.attempts} attempts.")
                    break
                else:
                    print("Incorrect guess. Try again.")
                    self.attempts += 1

            except KeyboardInterrupt:
                print("\nGame interrupted. Exiting.")
                break

if __name__ == "__main__":
    game_length = 10  # You can adjust the length of the DNA sequence
    dna_game = DNAGame(game_length)
    dna_game.play()