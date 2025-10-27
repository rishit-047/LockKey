import os
from string import ascii_uppercase, ascii_lowercase, ascii_lowercase
import math
import lockkey

def encryption(plaintext, a, b, alpha):
    encrypted_text = ""
    if alpha == "":
        for ch in plaintext:
            if ch in ascii_uppercase:
                pos = ascii_uppercase.index(ch)
                encrypted_text += ascii_uppercase[(pos * a + b) % len(ascii_uppercase)]
            elif ch in ascii_lowercase:
                pos = ascii_lowercase.index(ch)
                encrypted_text += ascii_lowercase[(pos * a + b) % len(ascii_lowercase)]
            else:
                encrypted_text += ch
        return encrypted_text
    
    for ch in plaintext:
        if ch in alpha:
            pos = alpha.index(ch)
            encrypted_text += alpha[(pos * a + b) % len(alpha)]
        else:
            encrypted_text += ch
    
    return encrypted_text

def decryption(encrypted, a, b, alpha):
    plaintext = ""
    if alpha == "":
        for ch in encrypted:
            if ch in ascii_uppercase:
                pos = ascii_uppercase.index(ch)
                plaintext += ascii_uppercase[(pow(a, -1, len(ascii_uppercase)) * (pos - b)) % len(ascii_uppercase)]
            elif ch in ascii_lowercase:
                pos = ascii_lowercase.index(ch)
                plaintext += ascii_lowercase[(pow(a, -1, len(ascii_lowercase)) * (pos - b)) % len(ascii_lowercase)]
            else:
                plaintext += ch
        return plaintext

    for ch in encrypted:
        if ch in alpha:
            pos = alpha.index(ch)
            plaintext += alpha[(pow(a, -1, len(alpha)) *(pos - b)) % len(alpha)]
        else:
            plaintext += ch
    return plaintext

def check_coPrime(a, b):
    return math.gcd(a,b) == 1

def main():
    os.system('clear')
    line = '-' * 60
    print(line)
    print(" Welcome to the Method of Affine Cipher !!")
    print(line,'\n')
    
    while True:
        try:
            opt = int(input("\nWhat would you like to do?\n1) Encrypt a message\n2) Decrypt a message\n3) Exit to main menu\nEnter your choice (1 or 2): "))
        except ValueError:
            print("\nInvalid option. Choose again....")
            continue

        if opt == 1:
            # Taking input
            plaintext = input("Please enter the text you wish to encrypt: ")
            a = int(input("Enter the Slope(a): "))
            b = int(input("Enter the Intercept(b): "))
            alpha = input("Enter custom alphabets to use for encryption (leave blank to use default behavior): ")
            
            # If no input given in custom_alphabets, assisgning values acordinglt
            if alpha == "":
                alpha_len = len(ascii_uppercase)

            # checking if the key one and the length of custom_alphabet is co prime
            if(check_coPrime(a, alpha_len)):
                print("Encrypted text: ",encryption(plaintext, a, b, alpha))
                input("\nPress Enter to return to CipherBox main menu...")
            else:
                print("The slope and the alphabets is not co prime")
            break

        elif opt == 2:
            encrypted = input("Please enter the text you wish to decrypt: ")
            a = int(input("Enter the Slope(a): "))
            b = int(input("Enter the Intercept(b): "))
            alpha = input("Enter custom alphabets to use for encryption (leave blank to use default behavior): ")

            if alpha == "":
                alpha_len = len(ascii_uppercase)
            
            if(check_coPrime(a, alpha_len)):
                print("Decrypted text: ",decryption(encrypted, a, b, alpha))
                input("\nPress Enter to return to CipherBox main menu...")
            else:
                print("The slope and the alphabets is not co prime")
            break
    
    input("\nPress Enter to return to CipherBox main menu...")


    lockkey.main()

if __name__ == "__main__":
    main()