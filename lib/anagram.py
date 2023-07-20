class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        sol = []
        for ana in list:
            if sorted(self.word) == sorted(ana):
                sol.append(ana)
        return sol
