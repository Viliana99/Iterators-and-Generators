class  WordContextGenerator:
    def __init__(self, words, window_size):
        self.words = words
        self.window_size = window_size
        
    def __iter__(self):
        for i,j in enumerate(self.words):
            for z in self.words[max(i - self.window_size, 0) : min(i + self.window_size + 1, len(self.words))]:
                if z != j:
                    yield j, z  