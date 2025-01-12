def caesar_decrypt_custom(ciphertext, shift, alphabet):
    """Decrypt a Caesar cipher using a custom alphabet."""
    decrypted = []
    for char in ciphertext:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - shift) % len(alphabet)
            decrypted.append(alphabet[new_index])
        else:
            decrypted.append(char)  # Leave characters not in the alphabet unchanged
    return ''.join(decrypted)

# Custom alphabet
custom_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890"

# Ciphertext
ciphertext = """
D_AZ_5H7S006_9WHF6BHD_33HX_5VHSAH3WS0AHIJHX3SY0H064WH6XHAZW4HS9WHX_3WH5S4WVHX3SYH5HTBAH064WA_4W0HAZWHX3SYH_0HZ_VVW5H_5HS56AZW9HX_3WHAZ_0H4W00SYWH_0HAZWHS50DW9HA6HUZS33W5YWHIHV6AHI
""".replace("\n", "")

# Test all shifts
for shift in range(len(custom_alphabet)):
    print(f"Shift {shift}:")
    decrypted_text = caesar_decrypt_custom(ciphertext, shift, custom_alphabet)
    print(decrypted_text)
    print("-" * 50)
