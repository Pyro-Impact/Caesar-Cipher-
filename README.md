# Caesar-Cipher- The CaesarCipher.py file is the main file.

This program was later modified for experimental purposes in order to learn how to separate a program into many modules. I recently removed all but 1 module (that one was reusable) so this program is archived.

This Caesar Cipher alphabetically shifts 15 to the right and converts the letter to a different case (lower
case or upper case). The numbers shift to the right 3 units. The comma encrypts into a period, and a period 
is encrypted into a comma. 

I originally got the idea from a friend who also had an encryption program on their repl.it profile. I used 
this website to come up with a dictionary for my program, which included a shift 15 alphabetical: 
https://crypto.interactive-maths.com/caesar-shift-cipher.html

The encryptor/decryptor includes: 
1. encoding/decoding function based on what the user chooses
2. user can also restart the program or break the program after their message is encrypted/decrypted.
3. If user enters a wrong input for their message that will get converted, question that asks to encrypt/decrypt, 
or the question that asks to restart or quit, then the program prints "Invalid Input. Please try again." and loops
back.
4. 2 different dictionaries for encrypt and decrypt
5. useage of while True loops for many sections of the user's usage of the tool.
6. New modules to shorten the code in the main.
7. A class added to practice OOP.
