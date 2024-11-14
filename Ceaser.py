def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    
    for char in plain_text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # If the character is not a letter, just add it as is
        else:
            encrypted_text += char
    
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    
    for char in encrypted_text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # If the character is not a letter, just add it as is
        else:
            decrypted_text += char
    
    return decrypted_text

def main():
    # Get user input for the message and the shift value
    plain_text = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value (integer): "))
    
    # Encrypt the message using Caesar Cipher
    encrypted_message = caesar_cipher_encrypt(plain_text, shift)
    
    # Output the encrypted message
    print(f"Original Message: {plain_text}")
    print(f"Shift: {shift}")
    print(f"Encrypted Message: {encrypted_message}")
    
    # Ask the user if they want to decrypt the message
    decrypt_choice = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
    
    if decrypt_choice == "yes":
        # Decrypt the message using the same shift value
        decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    elif decrypt_choice == "no":
        print("You chose not to decrypt the message.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
    
if __name__ == "__main__":
    main()
