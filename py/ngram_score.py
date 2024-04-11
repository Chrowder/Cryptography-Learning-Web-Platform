from math import log10

class ngram_score(object):
    def __init__(self, ngramfile, sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        with open(ngramfile) as file:
            for line in file:
                key, count = line.split(sep)
                self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        # calculate log probabilities
        for key in self.ngrams:
            self.ngrams[key] = log10(float(self.ngrams[key]) / self.N)
        self.floor = log10(0.01 / self.N)

    def score(self, text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.get  # Use .get for a default return value on missing keys
        for i in range(len(text) - self.L + 1):
            score += ngrams(text[i:i+self.L], self.floor)  # Use floor value if n-gram is not found
        return score
