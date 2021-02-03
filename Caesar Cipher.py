print("Welcome to the Caesar Cipher Encryptor/Decryptor")
print("Please type only letters, numbers, spaces and commas/periods.")
print("The Caesar Cipher shifts alphabetically forward 15 units. For example, a becomes P.")

Encrypt = {"a": "P", "b": "Q", "c": "R", "d": "S", "e": "T", "f": "U", "g": "V", "h": "W", "i": "X", "j": "Y",
           "k": "Z", "l": "A", "m": "B", "n": "C", "o": "D", "p": "E", "q": "F", "r": "G", "s": "H", "t": "I",
           "u": "J", "v": "K", "w": "L", "x": "M", "y": "N", "z": "O", "A": "p", "B": "q", "C": "r", "D": "s",
           "E": "t", "F": "u", "G": "v", "H": "w", "I": "x", "J": "y", "K": "z", "L": "a", "M": "b", "N": "c",
           "O": "d", "P": "e", "Q": "f", "R": "g", "S": "h", "T": "i", "U": "j", "V": "k", "W": "l", "X": "m",
           "Y": "n", "Z": "o", " ": " ", "1": "4", "2": "5", "3": "6", "4": "7", "5": "8", "6": "9", "7": "0",
           "8": "1", "9": "2", "0": "3", ".": ",", ",": "."}

Decrypt = {v: k for k, v in Encrypt.items()}

while True:

    while True:
        answer = input("Would you like to encrypt or decrypt a message? Please type encrypt or decrypt: ")
        if answer.strip() in ["encrypt", "decrypt"]:
            break
        print("Invalid input. Please try again.")

    while True:
        if answer.strip() in "encrypt":
            message = str(input("Please enter the code you'd like to encrypt: "))
            encrypt_check = all(c in Encrypt for c in message)

            if encrypt_check is False:
                print("invalid lol")
                continue
            else:
                break
        else:
            message = input("Please enter the code you'd like to decrypt: ")
            decrypt_check = all(c in Decrypt for c in message)

            if decrypt_check is False:
                print("Invalid input. Please try again.")
                continue
            else:
                break

    def cryptocode():
        result = ""
        if answer.lower() == "encrypt":
            for e in message:
                result += Encrypt[e]

        elif answer.lower() == "decrypt":
            for r in message:
                result += Decrypt[r]
        return result

    print("The message translates into:", cryptocode())

    while True:
        restart_confirm = input("Would you like to encrypt/decrypt another message? \n"
                                "Type yes or no: ")

        if restart_confirm.strip() in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please type yes or no.")
            continue

    if "yes" in restart_confirm.lower():
        print("The program has reset.")
        continue

    else:
        break
