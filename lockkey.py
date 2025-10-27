import pyfiglet
import os
import sys
import caesar_cipher
import vigenere_cipher
import affine_cipher
import playfair

def main():
    os.system('clear')
    for font in ["big"]:
        print(pyfiglet.figlet_format("LockKey", font=font))

    print("\nWelcome to LockKey! This tool helps you encrypt and decrypt text using various cipher methods including Caesar, Vigenère, Playfair, Rail Fence, Affine, and Hill ciphers.")
    method = int(input("\nSelect the method to perform the chosen operation:\n1) Caeser Cipher\n2) Vigenere Cipher\n3) Playfair Cipher\n4) Rail Fence Cipher\n5) Affine Cipher\n6) Hill Cipher\n7) Exit\nChoose: "))
    if method == 1:
        caesar_cipher.main()
    elif method == 2:
        vigenere_cipher.main()
    elif method == 2:
        vigenere_cipher.main()
    elif method == 3:
        playfair.main()
    elif method == 5:
        affine_cipher.main()
    elif method == 7:
        print("\nThank you for using CipherBox !!\nGoodbye !!")       
    elif method == 3:
        print("\nThank you for using CipherBox !!\nGoodbye !!")
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nThank you for using LockKey !!\nGoodbye !!")
        sys.exit(0)

