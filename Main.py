from Shift15.Crypto_Currency import cryptocode
from Shift15.Message_Function import check
from Shift15.Restart_Function import confirm_restart
from Shift15.Encrypt_or_Decrypt import en_or_de

print("Welcome to the Caesar Cipher Encryptor/Decryptor")
print("Please type only letters, numbers, spaces and commas/periods.")
print("The Caesar Cipher shifts alphabetically forward 15 units. For example, a becomes P.\n")

while True:
    print("The message translates into:", cryptocode(en_or_de(), check("")))

    if "yes" in confirm_restart():
        print("The program has reset.")
        continue
    else:
        break
