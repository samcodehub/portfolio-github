# pip install pyspellchecker

from spellchecker import SpellChecker

# create an instance of SpellChecker
spell = SpellChecker()

# misspelled words 
misspelled = spell.unknown(['pythn','wht', 'favorte','languge'])

for word in misspelled:
    # return most likely correct spelling
    print(spell.correction(word))