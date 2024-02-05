import random

class WordGenerator:
    def __init__(self, word_list):
        self.word_list = word_list

    def choose_word(self):  # Choose a word for the player to guess.
        return random.choice(self.word_list)
