print("Welcome to the Caesar Cipher Encryptor/Decryptor")
print("Please type only letters, numbers, and spaces.")
print("The Caesar Cipher shifts alphabetically forward 15 units. For example, a becomes P.")

Encrypt = {"a": "P", "b": "Q", "c": "R", "d": "S", "e": "T", "f": "U", "g": "V", "h": "W", "i": "X", "j": "Y",
           "k": "Z", "l": "A", "m": "B", "n": "C", "o": "D", "p": "E", "q": "F", "r": "G", "s": "H", "t": "I",
           "u": "J", "v": "K", "w": "L", "x": "M", "y": "N", "z": "O", " ": " ", "1": "1", "2": "2", "3": "3",
           "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0"}

Decrypt = {v: k for k, v in Encrypt.items()}

while True:

    while True:
        answer = input("Would you like to encrypt or decrypt a message? Please type encrypt or decrypt.")
        if answer.lower() in ["encrypt", "decrypt"]:
            break
        print("Invalid input. Please try again.")

    while True:
        if answer.lower() == "encrypt":
            message = str(input("Please enter the code you'd like to encrypt"))
            encrypt_for = ""
            for i in message.lower():
                encrypt_for += message.lower()
                if i not in Encrypt:
                    print("Invalid input. Please try again.")
                else:
                    break
            if True:
                break
        else:
            message = input("Please enter the code you'd like to decrypt")
            decrypt_for = ""
            for t in message.upper():
                decrypt_for += message.upper()
                if t not in Decrypt:
                    print("Invalid input. Please try again.")
                else:
                    break
            if True:
                break

    def cryptocode():
        result = ""
        if answer.lower() == "encrypt":
            for e in message.lower():
                result += Encrypt[e]
        elif answer.lower() == "decrypt":
            for r in message.upper():
                result += Decrypt[r]
        return result

    print("The message translates into:", cryptocode())

    while True:
        restart_confirm = input("Would you like to encrypt/decrypt another message?"
                                "Type yes or no")

        if restart_confirm.lower() in ["yes", "no"]:
            break
        else:
            print("Invalid input. Type yes or no.")
            continue

    if restart_confirm.lower() == "yes":
        print("The program has reset.")
        continue
    else:
        break
