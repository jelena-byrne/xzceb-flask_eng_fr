import unittest

from translator import englishToFrench, frenchToEnglish


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        # test when input is "What time is it?" and the output is "Quelle heure est-il?"
        self.assertEqual(englishToFrench("What time is it?"),
                         "Quelle heure est-il?")
        # test when input is "What is your favorite color?" and the output is "Quelle est votre couleur préférée?"
        self.assertEqual(englishToFrench(
            "What is your favorite color?"), "Quelle est votre couleur préférée?")
        # test when input is null
        self.assertIsNone(englishToFrench(None))
        # test when input is "Hello" and the output is "Bonjour"
        self.assertEqual(englishToFrench("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        # test when input is "Il fait beau aujourd'hui." and the output is "It's beautiful today."
        self.assertEqual(frenchToEnglish(
            "Il fait beau aujourd'hui."), "It's beautiful today.")
        # test when input is "Bonne soirée!" and the output is "Good evening!"
        self.assertEqual(frenchToEnglish("Bonne soirée!"), "Good evening!")
        # test when input is null
        self.assertIsNone(frenchToEnglish(None))
        # test when input is "Bonjour" and the output is "Hello"
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")


unittest.main()
