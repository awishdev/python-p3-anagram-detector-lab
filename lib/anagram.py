# your code goes here!
class Anagram:
    
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [word for word in word_list if sorted(self.word) == sorted(word.lower()) and word != self.word]