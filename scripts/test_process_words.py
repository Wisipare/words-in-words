"""
This script prompts the user for a gray word, a gold word, and the maximum number of words to use from a dictionary. 
It then calls the process_words function with the user inputs and prints the statistics of the valid words found, 
their dimensions, and the most repeated letters. Finally, it prompts the user if they want to see the list of selected words, 
and if the user wants to see the list, it prints it.
"""

import sys
sys.path.append('/Users/pablorsc/words-in-words/src')

import os
import json
import datetime
import logging
import requests
import bubbleio_library
from process_words import process_words
from manipulate_dictionary_library import choose_dictionary, list_dictionaries
from manipulate_words_library import create_or_update_library


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Prompt the user for the gray word
print("="*50)
gray_word = input("Please enter the ** GRAY ** word: ")

# Prompt the user for the gold word
print("="*50)
gold_word = input("Please enter the ** GOLDEN ** word: ")

# Get a list of available dictionaries
dictionaries = list_dictionaries()

# Print the list of dictionaries
print("Available dictionaries:")
for i, dictionary in enumerate(dictionaries):
    print(f"{i+1}. {dictionary}")

# Prompt the user to choose a dictionary
print("="*50)
dictionary_choice = input("Enter the number of the dictionary you want to use, or press enter to use the default dictionary: ")

# If the user chose a dictionary, set the dictionary path to the chosen dictionary
if dictionary_choice:
    try:
        dictionary_choice = int(dictionary_choice)
        dictionary_name = dictionaries[dictionary_choice-1]
    except (ValueError, IndexError):
        print("Invalid choice. Using default dictionary.")
        dictionary_name = None
else:
    print("Using default dictionary.")
    dictionary_name = None

# Get the path to the selected dictionary
dictionary_path = choose_dictionary(dictionary_name)

# Prompt the user to choose a game
print("="*50)
print("Choose a game:")
print("1. SwapSwap")
print("2. Classic")
print("3. Unknown")
print("4. Unknown")
print("5. Unknown")
game_choice = int(input("Enter the number of the game you want to use: "))

# Call the process_words function with the user inputs
result = process_words(gray_word, gold_word, dictionary_path, None, game_choice)

# Print the statistics of the valid words found, their dimensions, and the most repeated letters
print("#" * 50)
print(f"Number of valid words found: {len(result['Valid_Words'])}")
print(f"Dimensions of words: {result['Statistics']['Words_According_to_Length']}")
print(f"Most repeated letters: {result['Statistics']['Most_Common_Letters']}")
print("#" * 50)

# Prompt the user if they want to see the list of selected words
see_list = input("Do you want to see the list of selected words? (yes/no): ")

# If the user wants to see the list, print it
if see_list.lower() == 'yes':
    print("\n")
    print("#" * 50)
    print("\n")
    print(result['Valid_Words'])
    print("\n")
    print("#" * 50)
    print("\n")

# Prompt the user if they want to add the gray and gold words to the library
print("=" * 50)
add_to_library = input("Do you want to add the gray and gold words to the library? (yes/no): ")

# If the user wants to add the gray and gold words to the library, call the add_word_to_library function
if add_to_library.lower() == 'yes':
    try:
        new_result = create_or_update_library(result)
        # Unpack the output tuple
        mensaje, json_data = new_result
        print(mensaje)
    except Exception as e:
        print(f"Error adding words to the library: {e}")
        sys.exit(1)
elif add_to_library.lower() == 'json':
    json_data = json.dumps(result)
    print(json_data)

    # Ask the user if they want to make the API call
    print("=" * 50)
    make_api_call_input = input("Do you want to make the API call with the JSON data? (yes/no): ")
    if make_api_call_input.lower() == 'yes':
        url = 'https://wordsinwords.bubbleapps.io/version-test/api/1.1/wf/create_daily_game/'
        bubbleio_library.send_processed_words(json_data, url)