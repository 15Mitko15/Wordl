from colors import Color
class ColorsForWord:
    def __init__(self, target: str, guess: str) -> None:
        # Create a list of colors for a guess given a target
        self.color_list = self.colors_of_an_asked_word(target, guess)
        #self._list_of_six_letter_words = self._get_words()

    @staticmethod
    def replace_at_index(i, char_list):
        """Replaces a character at a given index in a list of characters."""
        if i == 0:
            return ['\0'] + char_list[1:]
        else:
            return char_list[:i] + ['\0'] + char_list[i + 1:]

    @staticmethod
    def replace_letter(letter, char_list):
        """Replaces a specific letter in a list of characters."""
        return ['\0' if char == letter else char for char in char_list]

    @staticmethod
    def check_green_letters(target, guess, pos_green):
        """Checks if green letters are correctly placed."""
        for pos in pos_green:
            target = ColorsForWord.replace_at_index(pos, target)
        return target, True

    @staticmethod
    def check_green_letters_positions(target, guess, pos):
        """Checks the positions of green letters in the guessed word."""
        green_positions = []
        for i, (trg, gss) in enumerate(zip(target, guess)):
            if trg == gss:
                green_positions.append(pos + i)
        return green_positions

    @staticmethod
    def colors_of_an_asked_word(target, guess):
        """Returns the colors of an asked word."""
        temp_target = list(target)
        green_positions = ColorsForWord.check_green_letters_positions(target, guess, 0)

        for pos in green_positions:
            temp_target = ColorsForWord.replace_at_index(pos, temp_target)

        colors = []
        for trg, gss in zip(target, guess):
            if trg == gss:
                colors.append(Color.GREEN)
            elif gss in temp_target:
                colors.append(Color.YELLOW)
                temp_target.remove(gss)
            else:
                colors.append(Color.GREY)

        return colors

