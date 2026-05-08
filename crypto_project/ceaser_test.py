import unittest
from app.classical import caesar


class TestCaesar(unittest.TestCase):
    def test_encrypt_hello_word_shift3(self):
        self.assertEqual(caesar.encrypt("Hello Word", 3), "Khoor Zrug")

    def test_decrypt_hello_word_shift3(self):
        self.assertEqual(caesar.decrypt("Khoor Zrug", 3), "Hello Word")

    def test_encrypt_john_smith_shift5(self):
        self.assertEqual(caesar.encrypt("JohnSmith", 5), "OtmsXrnym")

    def test_decrypt_john_smith_shift5(self):
        self.assertEqual(caesar.decrypt("OtmsXrnym", 5), "JohnSmith")

    def test_encrypt_non_alpha(self):
        self.assertEqual(caesar.encrypt("Test 123!", 4), "Xiwx 123!")

    def test_decrypt_non_alpha(self):
        self.assertEqual(caesar.decrypt("Xiwx 123!", 4), "Test 123!")

    def test_roundtrip(self):
        for shift in [1, 3, 25]:
            original = "Hello World!@#"
            self.assertEqual(
                caesar.decrypt(caesar.encrypt(original, shift), shift),
                original
            )