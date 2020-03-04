import numpy as np


class  BatchGenerator:
    def __init__(self, list_of_sequences, batch_size, shuffle=False):
        self.list_of_sequences = list_of_sequences
        self.shuffle = shuffle
        self.batch_size = batch_size
        self.index = 0
        
    def __iter__(self):
        while self.index < len(self.list_of_sequences[0]):
            k = []
            for el in self.list_of_sequences:
                k.append(el[self.index: self.index + self.batch_size])
            self.index += self.batch_size
            yield k




