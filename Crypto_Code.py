from Shift15.Dictionaries import Encrypt, Decrypt


class FinalCode:
    def __init__(self, answer, message):
        self.answer = answer
        self.message = message

    def cryptocode(self):
        result = ""
        if self.answer.lower() == "encrypt":
            for e in self.message:
                result += Encrypt[e]

        elif self.answer.lower() == "decrypt":
            for r in self.message:
                result += Decrypt[r]
        return result
