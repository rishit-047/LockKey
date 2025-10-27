import os
from string import ascii_uppercase

def generate_key_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in keyword:
        if ch.isalpha() and ch not in used:
            used.add(ch)
            matrix.append(ch)

    for ch in ascii_uppercase:
        if ch == "J":  # skip J
            continue
        if ch not in used:
            used.add(ch)
            matrix.append(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
    return None, None

def encryption(plaintext, keyword):
    matrix = generate_key_matrix(keyword)
    ch_info = [(ch, ch.isupper(), ch.isalpha()) for ch in plaintext]
    clean_text = ''.join(ch.upper().replace("J", "I") for ch in plaintext if ch.isalpha())

    
    pairs = []
    i = 0
    while i < len(clean_text):
        a = clean_text[i]
        b = clean_text[i + 1] if i + 1 < len(clean_text) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    encrypted_pairs = []
    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            encrypted_pairs.append(matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:
            encrypted_pairs.append(matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2])
        else:
            encrypted_pairs.append(matrix[r1][c2] + matrix[r2][c1])

    ciphertext = ''.join(encrypted_pairs)

    result = []
    idx = 0
    for ch, is_upper, is_alpha in ch_info:
        if is_alpha:
            enc_ch = ciphertext[idx]
            result.append(enc_ch if is_upper else enc_ch.lower())
            idx += 1
        else:
            result.append(ch)

    return ''.join(result)


def main():
    os.system('clear')
    line = '-' * 60
    print(line)
    print(" Welcome to the Method of Playfair Cipher !!")
    print(line,'\n')

    while True:
        try:
            opt = int(input("\nWhat would you like to do?\n1) Encrypt a message\n2) Decrypt a message\n3) Exit to main menu\nEnter your choice (1, 2 or 3): "))
        except ValueError:
            print("\nInvalid option,Choose again....")
            continue
        
        if opt == 1:
            # Taking plaintext as input
            plaintext = input("Please enter the text you wish to encrypt: ")
            keyword = input("Enter the keyword: ")
            
            # checking if the keyword is empty
            if keyword == "":
                print("Empty string entered, try again..")
                continue

            print("Encrypted text:",encryption(plaintext, keyword))            

if __name__ == "__main__":
    main()