from string import ascii_uppercase


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(f"Літары алфавіта: {' '.join(self.letters)}")

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__("EN", ascii_uppercase)

    def is_en_letter(self, let):
        print(f"Літара {let} адносіцца да алфавіту.") if let.upper() in self.letters else print(f"Літара {let} не адносіцца да алфавіту.")

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "This is an example text in English."
