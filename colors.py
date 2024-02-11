from enum import Enum

class Color(Enum):
    # Colors indicateing the state of a letter
    GREEN = 1 # Indicates that the letter is in it right possition
    YELLOW = 2 # Indicates that the letters is in the word but not in the right possition
    GREY = 3 # Indicates that the letter is not in the word