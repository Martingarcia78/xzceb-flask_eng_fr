import unittest

from ..translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    
    #Tests for english to french
    def test_e2fe(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")

    def test_e2fne(self):
        self.assertNotEqual(english_to_french("cat"),"chien")

    #Tests for french to english
    def test_f2e(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
    
    def test_f2en(self):
        self.assertNotEqual(french_to_english("chien"),"cat")


if __name__ == "__main__":
    unittest.main()