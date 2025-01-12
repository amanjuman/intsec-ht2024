import hashlib

# Keys
key_1 = "1234"
key_2 = "5678"

# Messages and expected HMACs
messages = {
    "Challenge 2.2 is easy.": "12d44a1c2448cc54ddffc75e69313a7964d5d775",
    "Challenge 2.2 is doable.": "1b25d0e281f73935f7a122c088c1bc34686b271b",
    "Challenge 2.2 is hard.": "aec64e480f251c6811686597305b04edcc25da35"
}

def compute_hmac_sha1(key1, key2, message):
    # Inner hash
    inner = hashlib.sha1((key1 + message).encode()).hexdigest()
    # Outer hash
    outer = hashlib.sha1((key2 + inner).encode()).hexdigest()
    return outer

# Verify each message
for msg, expected_hmac in messages.items():
    computed_hmac = compute_hmac_sha1(key_1, key_2, msg)
    print(f"Message: {msg}")
    print(f"Computed HMAC: {computed_hmac}")
    print(f"Expected HMAC: {expected_hmac}")
    print("Match: ", computed_hmac == expected_hmac)
    print("-" * 40)
