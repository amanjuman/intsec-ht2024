import re

def enhanced_xor_decrypt(file_path, key, key_length):
    # Ensure the key is exactly the correct length (15 bytes)
    if len(key) > key_length:
        key = key[:key_length]
    elif len(key) < key_length:
        key = (key * ((key_length // len(key)) + 1))[:key_length]

    # Read the encrypted file
    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    # Decrypt the file using the repeating XOR key
    key_bytes = key.encode("ascii")
    decrypted_data = bytes([encrypted_data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(encrypted_data))])

    # Clean and filter ASCII output
    cleaned_output = ""
    for b in decrypted_data:
        if 32 <= b < 127:  # Printable ASCII range
            cleaned_output += chr(b)
        elif b == 10:  # Preserve newlines
            cleaned_output += "\n"
        else:
            cleaned_output += " "  # Replace unprintable characters with space

    # Remove excessive spaces
    cleaned_output = re.sub(r'\s+', ' ', cleaned_output).strip()

    return decrypted_data, cleaned_output
