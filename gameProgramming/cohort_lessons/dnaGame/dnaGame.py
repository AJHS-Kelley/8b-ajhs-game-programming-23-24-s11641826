# DNA Replication Game, Albert Laguerre, v0.0

import random

class DNASequence:
    nucleotides = ['A', 'C', 'G', 'T']

    def __init__(self, length):
        self.sequence = ''.join(random.choice(self.nucleotides) for _ in range(length))