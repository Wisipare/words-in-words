import os
import sys
import locale
import json

import os
import json
import locale

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
