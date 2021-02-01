print("Welcome to the Caesar Cipher Encryptor/Decryptor")
print("Please type only lower case letters and spaces.")

Encrypt = {"a": "P", "b": "Q", "c": "R", "d": "S", "e": "T", "f": "U", "g": "V", "h": "W", "i": "X", "j": "Y", "k": "Z",
           "l": "A", "m": "B", "n": "C", "o": "D", "p": "E", "q": "F", "r": "G", "s": "H", "t": "I", "u": "J", "v": "K",
           "w": "L", "x": "M", "y": "N", "z": "O", " ": " "}

Decrypt = {v: k for k, v in Encrypt.items()}

while True:
    message = input("Please enter the message that you'd like to encrypt/decrypt.")
    pass
    #type the if message has number blah blah blah here tomorrow!

    while True:
        answer = input("Would you like to encrypt or decrypt a message? Please type encrypt or decrypt.")
        if answer.lower() in ["encrypt", "decrypt"]:
            break
        print("Invalid input")

    def cryptocode():
        if answer.lower() == "encrypt":
            for i in message.lower():
                # Encrypt[i]
        # return should be here

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
