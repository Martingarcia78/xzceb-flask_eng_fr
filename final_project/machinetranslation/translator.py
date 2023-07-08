from deep_translator import MyMemoryTranslator

#English to french function
def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source="english", target="french").translate(englishText) #creating an instance of the class
    return frenchText

#French to english function
def frenchToEnglish(frenchText):
    englishText = MyMemoryTranslator(source="french", target="english").translate(frenchText)
    return englishText