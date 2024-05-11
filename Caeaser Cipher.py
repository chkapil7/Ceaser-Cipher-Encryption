def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Enter 'e' for encryption or 'd' for decryption: ").lower()
    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        encrypted_message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
