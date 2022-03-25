from os import error, path
from translate import Translator
from translate import Translator
import pathlib


try:
    with open('translate.txt', mode='a') as my_file:
        translator = Translator(to_lang="es")
        translation = translator.translate(my_file.read())
        my_file.write('\n\n Translation: \n')
        my_file.write(translation)
except:
    raise Exception()
