from Shift15.Dictionaries import Encrypt, Decrypt


def cryptocode(answer, message):
    result = ""
    if answer.lower() == "encrypt":
        for e in message:
            result += Encrypt[e]

    elif answer.lower() == "decrypt":
        for r in message:
            result += Decrypt[r]

    return result
