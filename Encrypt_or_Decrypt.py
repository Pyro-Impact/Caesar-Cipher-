def en_or_de():
    while True:
        answer = input("Would you like to encrypt or decrypt a message? Please type encrypt or decrypt: ")
        answer1 = answer.strip().lower()
        if answer1 in ["encrypt", "decrypt"]:
            break
        print("Invalid input. Please try again.")
    return answer1
