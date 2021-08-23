from googletrans import Translator
translater=Translator()
input=""
output=translater.translate(input, dest="en")
print(output.text)
