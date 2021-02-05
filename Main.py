from Shift15.Result_Function import cryptocode
from Shift15.Message_Function import check

print("Welcome to the Caesar Cipher Encryptor/Decryptor")
print("Please type only letters, numbers, spaces and commas/periods.")
print("The Caesar Cipher shifts alphabetically forward 15 units. For example, a becomes P.")

while True:

    while True:
        answer = input("Would you like to encrypt or decrypt a message? Please type encrypt or decrypt: ")
        if answer.strip().lower() in ["encrypt", "decrypt"]:
            break
        print("Invalid input. Please try again.")

    print("The message translates into:", cryptocode(answer.strip().lower(), check(answer.strip().lower())))

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
