from wordlist import WordList

class SixLetterWordsList(WordList):
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name
        self._list_of_six_letter_words =self._get_words()

    def _get_words(self) -> list[str]:
       # Read the words from the file with 6 letter words 
       with open(self._file_name, 'r') as file:
            six_letter_words = [word.strip() for word in file.readlines()]
            file.close
            return six_letter_words
