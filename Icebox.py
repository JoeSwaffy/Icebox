"""
Icebox
PURPOSE: Encrypts every file in a given directory 'Icebox'
Essentially a file locker for security purposes.
"""
from cryptography.fernet import Fernet
import os
#Generates the secret key for the encrypt operation, and stores it in a "key file"
def generateKey():
    secretKey = Fernet.generate_key()
    with open('Icekey.key', 'wb') as savedKey:
        savedKey.write(secretKey)
#Encrypts the contents of the icebox
def encryptBox():
    path = 'Icebox'
    index = 0
    files = os.listdir(path)
    length = len(files)
    for i in range(index, length):
        with open('Icekey.key', 'rb') as keyFile:
            key = keyFile.read()
        fernet = Fernet(key)
        with open(path + '/' + files[i], 'rb') as original_file:
            original_data = original_file.read()
        encrypted_data = fernet.encrypt(original_data)
        with open(path + '/' + files[i], 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

#Decrypts the icebox
def decryptBox():
    path = 'Icebox'
    index = 0
    files = os.listdir(path)
    length = len(files)
    for i in range(index, length):
        with open('IceKey.key', 'rb') as keyFile:
            key = keyFile.read()
        fernet = Fernet(key)
        with open(path + '/' + files[i], 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(path + '/' + files[i], 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
#Main Method -- The front end of the program
def main():
    programRunning = True
    while programRunning:
        print('Icebox v0.0.1 PoC Build - Written by Joseph Swafford')
        print('Menu Options:')
        print('1. Encrypt the Icebox')
        print('2. Decrypt the Icebox')
        print('3. Exit the program')
        optionSelected = int(input('Enter your selection:'))
        if optionSelected == 1:
            print('Encrypting the icebox...')
            generateKey()
            print('Generating the encryption key file..')
            encryptBox()
            print('Encryption operation successful!')
        elif optionSelected == 2:
            print('Decrypting the icebox')
            decryptBox()
            print('Decryption Operation Successful!')
        elif optionSelected == 3:
            print('Exiting the program..')
            programRunning = False
            break
        break
#start the program
main()