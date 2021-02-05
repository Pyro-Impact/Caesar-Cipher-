from Shift15.Dictionaries import Encrypt, Decrypt


def check(answer):
    while True:
        if answer.strip() in "encrypt":
            message = str(input("Please enter the code you'd like to encrypt: "))
            encrypt_check = all(c in Encrypt for c in message)

            if encrypt_check is False:
                print("Invalid input. Please try again.")
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
    return message
