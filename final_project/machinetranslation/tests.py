import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):

    def test_e2f(self):

        self.assertEqual(englishToFrench("Hello"), "Bonjour")

        self.assertIsNone(englishToFrench(None))

class TestFrenchToEnglish(unittest.TestCase):

    def test_f2e(self):

        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

        self.assertIsNone(frenchToEnglish(None))

if __name__ == '__main__':
    unittest.main()