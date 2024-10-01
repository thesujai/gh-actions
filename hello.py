print("Hello World")



#random py code
import numpy as np

def prepare_text(plaintext, n):
    padding = (n - len(plaintext) % n) % n
    plaintext += 'X' * padding
    return plaintext

def c2i(text):
    return [ord(char) - ord('A') for char in text]

def i2c(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])

def hillcipher(plaintext, key):
    n = len(key)
    plaintext = prepare_text(plaintext, n)
    plaintext = c2i(plaintext)

    key_matrix = np.array(key)
    plaintext_matrix = np.array(plaintext).reshape(-1, n)
    encrypted_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    encrypted_numbers = encrypted_matrix.flatten().tolist()
    cipher = i2c(encrypted_numbers)

    return cipher

def get_key_matrix(n):
    print("Enter elements of key matrix (row-newline,column-space):")
    key = []
    for i in range(n):
        row = list(map(int, input().strip().split()))
        if len(row) != n:
            print("Invalid input. Please enter exactly", n, "elements in each row.")
            return get_key_matrix(n)
        key.append(row)
    return key

if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ").upper()
    n = int(input("Enter the size of the key matrix: "))
    key = get_key_matrix(n)
    ciphertext = hillcipher(plaintext, key)
    print("Plain text:", plaintext)
    print("Cipher text:", ciphertext)
