import os
import lockkey
from string import ascii_uppercase

def decryption(encrypted_text, keyword, alpha):
    keyword = keyword.upper()
    key_index = 0
    plaintext = ""

    for ch in encrypted_text:
        if ch.upper() in alpha:
            k_char = keyword[key_index % len(keyword)]
            if k_char in alpha:
                k_index = alpha.index(k_char)
                e_index = alpha.index(ch.upper())
                p_char = alpha[(e_index-k_index+len(alpha)) % len(alpha)]
                if ch.islower():
                    p_char = p_char.lower()
                plaintext += p_char
                key_index += 1
            else:
                plaintext += ch
        else:
            plaintext += ch     

    return plaintext

def encryption(plaintext, keyword, alpha):
    keyword = keyword.upper()
    key_index = 0
    encrypted_text = ""
    
    for ch in plaintext:
        if ch.upper() in alpha:
            k_char = keyword[key_index % len(keyword)]
            if k_char in alpha:
                p_index = alpha.index(ch.upper())
                k_index = alpha.index(k_char)
                encrypted_char = alpha[(p_index + k_index) % len(alpha)]

                if ch.islower():
                    encrypted_char = encrypted_char.lower()

                encrypted_text += encrypted_char

                key_index += 1
            else:
                encrypted_text += ch
        else:
            encrypted_text += ch
    
    return encrypted_text

def main():
    os.system('clear')
    line = '-' * 60
    print(line)
    print(" Welcome to the Method of Vigenere Cipher !!")
    print(line,'\n')

    while True:
        try:
            opt = int(input("What would you like to do?\n1) Encrypt a message\n2) Decrypt a message\n3) Exit to main menu\nEnter your choice (1 or 2): "))
        except ValueError:
            print("\nInvalid option. Choose again....")
            continue
    
        if opt == 1:
            # taking input
            plaintext = input("Please enter the text you wish to encrypt: ")
            keyword = input("Enter the keyword: ")
            alpha = input("Enter custom alphabets to use for encryption (leave blank to use default behavior): ")
        
            if alpha == "":
                alpha = ascii_uppercase
            
            print("Encrypted text:",encryption(plaintext, keyword, alpha))


        elif opt == 2:
            encrypted_text = input("Please enter the text you wish to decrypt: ")
            keyword = input("Enter the keyword: ")
            alpha = input("Enter custom alphabets to use for decryption (leave blank to use default behavior): ")

            if alpha == "":
                alpha = ascii_uppercase
            
            print("Decrypted text:",decryption(encrypted_text, keyword, alpha))
        
        elif opt == 3:
            lockkey.main()
            break

        else:
            print("\nInvalid option. Choose again....")
            continue
        
    
    input("\nPress Enter to return to CipherBox main menu...")

    lockkey.main()

if __name__ == "__main__":
    main()
    