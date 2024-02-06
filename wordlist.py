from abc import ABC, abstractmethod
import numpy as np


class WordList(ABC):
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    @abstractmethod
    def _get_words(self):
        pass
    

class FiveLetterWordsList(WordList):
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name
        self._listOfWords =self._get_words()

    def _get_words(self) -> list[str]:
       with open(self._file_name, 'r') as file:
            five_letter_words = [word.strip() for word in file.readlines()]
            file.close
            return five_letter_words