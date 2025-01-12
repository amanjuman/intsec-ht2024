import unittest
import tempfile
import os
from enhanced_xor_decrypt import enhanced_xor_decrypt

class TestEnhancedXORDecrypt(unittest.TestCase):

    def setUp(self):
        """Set up temporary test files."""
        # Initialization
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.write(b"J\x0e\x1c\x00\x14\x14")  # Example XOR-encoded data
        self.test_file.close()
        self.key = "dgfd464sdf54z"
        self.key_length = 15

    def tearDown(self):
        """Remove temporary files after test."""
        os.unlink(self.test_file.name)

    def test_valid_decryption(self):
        # Initialization
        encrypted_data = b"J\x0e\x1c\x00\x14\x14"  # Example XOR-encoded data
        key = "dgfd464sdf54z"
        key_bytes = key.encode("ascii")
        expected_decrypted = bytes([encrypted_data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(encrypted_data))])

        # Function under test
        raw_decrypted, cleaned_output = enhanced_xor_decrypt(self.test_file.name, self.key, self.key_length)

        # Oracle
        self.assertEqual(raw_decrypted[:len(expected_decrypted)], expected_decrypted, "Decryption mismatch")

    def test_ascii_cleaning(self):
        # Initialization
        test_file_content = b"Some\xffbinary\x00data"  # Unprintable and printable characters
        with open(self.test_file.name, "wb") as f:
            f.write(test_file_content)

        # Function under test
        _, cleaned_output = enhanced_xor_decrypt(self.test_file.name, self.key, self.key_length)

        # Oracle
        self.assertNotIn("\x00", cleaned_output, "Null byte found in cleaned output")
        self.assertNotIn("\xff", cleaned_output, "Non-ASCII byte found in cleaned output")

    def test_key_adjustment(self):
        # Initialization
        short_key = "short"
        expected_key = "shortshortshor"  # Expanded to match key_length of 15

        # Function under test
        with open(self.test_file.name, "rb") as f:
            encrypted_data = f.read()
        key_bytes = (short_key * ((self.key_length // len(short_key)) + 1))[:self.key_length]

        # Oracle
        self.assertEqual(len(key_bytes), self.key_length, "Key adjustment failed")

if __name__ == "__main__":
    unittest.main()
