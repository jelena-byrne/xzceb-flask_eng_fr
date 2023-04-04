import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        # test when input is "What time is it?" and the output is "Quelle heure est-il?"
        self.assertEqual(englishToFrench("What time is it?"), "Quelle heure est-il?")
        # test when input is "What is your favorite color?" and the output is "Quelle est votre couleur préférée?"
        self.assertEqual(englishToFrench("What is your favorite color?"), "Quelle est votre couleur préférée?")
        # test when input is null
        self.assertIsNull(englishToFrench(),)
        # test when input is "Hello" and the output is "Bonjour"
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        # test when input is "Quelle est votre couleur préférée?" and the output is "What is your favorite color?"
        self.assertEqual(frenchToEnglish("Quelle est votre couleur préférée?"), "What is your favorite color?")
        # test when input is "Bonne soirée!" and the output is "Good evening!"
        self.assertEqual(frenchToEnglish("Bonne soirée!"), "Good evening!")
        # test when input is null
        self.assertIsNull(frenchToEnglish(),)
        # test when input is "Bonjour" and the output is "Hello"
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")