import sys
sys.path.append('/Users/pablorsc/words-in-words/src')
import json
from manipulate_dictionary_library import search_word, choose_dictionary
import os




word = input("Enter a word to find its definition: ")
dictionaries_dir = "/Users/pablorsc/words-in-words/data/dictionaries"
dictionaries = os.listdir(dictionaries_dir)
print("Select a dictionary:")
for i, dictionary in enumerate(dictionaries):
    print(f"{i+1}. {dictionary}")
selected_dict_index = int(input()) - 1
selected_dict_path = os.path.join(dictionaries_dir, dictionaries[selected_dict_index])
definition = search_word(word, selected_dict_path))

print("\n" + "#" * 50 + "\n")
print(f"Word: {word}")
print("-" * 50 + "\n")
print("Definition:")
print(definition)
print("\n" + "#" * 50 + "\n")
