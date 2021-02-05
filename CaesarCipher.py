from Shift15.Crypto_Code import FinalCode
from Shift15.Message_Function import check
from Shift15.Restart_Function import confirm_restart

print("Welcome to the Caesar Cipher Encryptor/Decryptor")
print("Please type only letters, numbers, spaces and commas/periods.")
print("The Caesar Cipher shifts alphabetically forward 15 units. For example, a becomes P.\n")

while True:

    def en_or_de():
        while True:
            answer = input("Would you like to encrypt or decrypt a message? Please type encrypt or decrypt: ")
            answer1 = answer.strip().lower()

            if answer1 in ["encrypt", "decrypt"]:
                break
            print("Invalid input. Please try again.")
        return answer1

    FC = FinalCode(en_or_de(), check(""))
    print("Your message translates into: ", FC.cryptocode())

    if "yes" in confirm_restart():
        print("The program has reset.")
        continue
    else:
        break
