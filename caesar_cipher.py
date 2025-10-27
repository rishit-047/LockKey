import os
import lockkey
from string import ascii_uppercase, ascii_lowercase

def decryption(encrypted_text, key, alpha):
    
    if alpha == "":
        plaintext = ""
        alpha_up = ascii_uppercase
        alpha_low = ascii_lowercase
        for ch in encrypted_text:
            if ch.isupper():
                new_ch = alpha_up[(alpha_up.index(ch) - key) % len(alpha_up)]
                plaintext += new_ch
            elif ch.islower():
                new_ch = alpha_low[(alpha_low.index(ch) - key) % len(alpha_low)]
                plaintext += new_ch
            else:
                plaintext += ch 
        return plaintext

    shifted = alpha[key % len(alpha):] + alpha[:key % len(alpha)]
    table = str.maketrans(shifted, alpha)
    return encrypted_text.translate(table)
    

def encryption(plaintext, key, alpha):
    if alpha == "":
        encrypted_text = ""
        for ch in plaintext:
            if ch.isupper():
                alpha = ascii_uppercase
                new_ch = alpha[(alpha.index(ch) + key) % len(alpha)]
                encrypted_text += new_ch
            elif ch.islower():
                alpha = ascii_lowercase
                new_ch = alpha[(alpha.index(ch) + key) % len(alpha)]
                encrypted_text += new_ch
            else:
                encrypted_text += ch 
        return encrypted_text
    
    shifted = alpha[key % len(alpha):] + alpha[:key % len(alpha)]
    table = str.maketrans(alpha, shifted)
    return plaintext.translate(table)


def main():
    os.system('clear')
    line = '-' * 60
    print(line)
    print(" Welcome to the Method of Caesar Cipher !!")
    print(line,'\n')

    while True:
        try:
            opt = int(input("\nWhat would you like to do?\n1) Encrypt a message\n2) Decrypt a message\n3) Exit to main menu\nEnter your choice (1 or 2): "))
        except ValueError:
            print("\nInvalid option. Choose again....")
            continue
    
        if opt == 1:
            # taking input
            plaintext = input("Please enter the text you wish to encrypt: ")
            key = int(input("Enter the shift key: "))
            alpha = input("Enter custom alphabets to use for encryption (leave blank to use default behavior): ")
        
            
            print("Encrypted text:",encryption(plaintext, key, alpha))
            break


        elif opt == 2:
            encrypted_text = input("Please enter the text you wish to decrypt: ")
            key = int(input("Enter the keyword: "))
            alpha = input("Enter custom alphabets to use for decryption (leave blank to use default behavior): ")
            
            print("Decrypted text:",decryption(encrypted_text, key, alpha))
            break
        
        elif opt == 3:
            lockkey.main()
            break

        else:
            print("\nInvalid option. Choose again....")
            continue
        
    
    input("\nPress Enter to return to LockKey main menu...")

    lockkey.main()

if __name__ == "__main__":
    main()
    