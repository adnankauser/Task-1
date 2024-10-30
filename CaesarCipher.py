def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # Traverse the text
    for char in text:
        if char.isalpha():  # Check if character is a letter
            # Determine ASCII offset (uppercase or lowercase)
            offset = 65 if char.isupper() else 97
            # Shift character and wrap around alphabet
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += shifted_char
        else:
            # Non-alphabetical characters are added without change
            result += char
    
    return result

# User input
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
message = input("Enter your message: ")
shift = int(input("Enter shift value (0-25): "))

# Validate shift range
if 0 <= shift <= 25:
    # Encrypt or Decrypt based on user input
    output = caesar_cipher(message, shift, mode)
    print(f"The result is: {output}")
else:
    print("Invalid shift value. Please enter a value between 0 and 25.")
