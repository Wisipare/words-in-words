import json
import unicodedata
import os
import sys
import locale
import os

def load_dictionary(file_name):
    """
    Load a dictionary from a JSON file and normalize its words.

    Args:
        file_name (str): The name of the JSON file containing the dictionary.

    Returns:
        list: A list of normalized words from the dictionary.
    """
    try:
        with open(file_name, 'r') as file:
            dictionary = json.load(file)
        return [unicodedata.normalize('NFD', word.lower()).encode('ascii', 'ignore').decode() for word in dictionary]
    except FileNotFoundError:
        print("The dictionary file was not found.")
        return []
    except json.JSONDecodeError:
        print("The dictionary file is not valid JSON.")
        return []

def choose_dictionary(dictionary_name=None):
    """
    Chooses the dictionary to be used by the process_words module.

    If dictionary_name is provided, returns the path to the file with that name
    in the dictionaries folder. If not, checks if a file with the name
    <default_language>_dictionary.json exists in the dictionaries folder, where
    <default_language> is the language of the user's system. If it does, returns
    the path to that file. If no file is found, returns the path to the file
    en_dictionary.json.

    Args:
    dictionary_name (str): The name of the dictionary file to be used.

    Returns:
    str: The path to the selected dictionary file.
    """
    # Get the path to the dictionaries folder
    dictionaries_folder = os.path.join(os.path.dirname(__file__), '..', 'data', 'dictionaries')
    # Get the default language of the user's system
    default_language = locale.getdefaultlocale()[0][:2]

    # If a dictionary name is provided, try to load that dictionary
    if dictionary_name is not None:
        if os.path.isfile(dictionary_name):
            return dictionary_name
        dictionary_path = os.path.join(dictionaries_folder, dictionary_name)
        if os.path.isfile(dictionary_path):
            return dictionary_path

    # If no dictionary name is provided, try to load the default dictionary for the user's system
    default_dictionary_name = f"{default_language}_dictionary.json"
    default_dictionary_path = os.path.join(dictionaries_folder, default_dictionary_name)
    if os.path.isfile(default_dictionary_path):
        return default_dictionary_path

    # If no default dictionary is found, load the English dictionary
    return os.path.join(dictionaries_folder, 'en_dictionary.json')

def search_word(word, dictionary_path):
    """
    Search for a word in the dictionary and return its definition.

    Args:
        word (str): The word to search for.
        dictionary_path (str): The path to the dictionary file.

    Returns:
        str: The definition of the word if it exists in the dictionary, or a message indicating that the word was not found.
    """

    try:
        with open(dictionary_path, 'r') as file:
            dictionary = json.load(file)
        if word in dictionary:
            return dictionary[word]
        else:
            return "The word was not found in the dictionary."
    except FileNotFoundError:
        return "The dictionary file was not found."
    except json.JSONDecodeError:
        return "The dictionary file is not valid JSON."

def list_dictionaries():
    """
    List all available dictionaries in the dictionaries folder.

    Returns:
        list: A list of the available dictionary file names.
    """
    # Get the path to the dictionaries folder
    dictionaries_folder = os.path.join(os.path.dirname(__file__), '..', 'data', 'dictionaries')
    # List all files in the dictionaries folder
    files = os.listdir(dictionaries_folder)
    # Filter the list to only include JSON files
    json_files = [file for file in files if file.endswith('.json')]
    # Return the list of file names
    return json_files
