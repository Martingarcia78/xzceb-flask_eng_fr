import unittest

from translator.py import englishToFrench, frenchToEnglish

class TestMyModule(unittest.TestCase):
    
    #Tests for english to french
    def test_e2fe(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

    def test_e2fne(self):
        self.assertNotEqual(englishToFrench("cat"),"chien")

    #Tests for french to english
    def test_f2e(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    
    def test_f2en(self):
        self.assertNotEqual(frenchToEnglish("chien"),"cat")


if __name__ == "__main__":
    unittest.main()