" This file is for creating translation methods "

from deep_translator import MyMemoryTranslator

#English to french function
def english_to_french(english_text):
    french_text = MyMemoryTranslator(source="english",
    target="french").translate(english_text) #creating an instance of the class
    return french_text

#French to english function
def french_to_english(french_text):
    english_text = MyMemoryTranslator(source="french",
    target="english").translate(french_text)
    return english_text
