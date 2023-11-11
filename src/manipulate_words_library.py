import csv
import os
import json
from datetime import datetime


def create_or_update_library(json_data):
    """
    This function receives a JSON object with data about a gray word, a golden word, and some statistics about the words
    that can be formed by using the letters of the gray word. It checks if the gray word and golden word meet certain
    conditions, and if the pair of words already exists in the library. If all checks pass, it appends the data to a CSV
    file that serves as a library of gray-golden word pairs. If the library file does not exist, it creates it with the
    appropriate headers.

    Args:
        json_data (dict): A JSON object with the following keys:
            - Gray_Word (str): The gray word.
            - Golden_Word (str): The golden word.
            - Statistics (dict): A dictionary with the following keys:
                - Words_Meeting_Condition (int): The number of words that can be formed by using the letters of the gray word.
                - Words_According_to_Length (dict): A dictionary where the keys are the lengths of the words that can be
                  formed by using the letters of the gray word, and the values are the number of words of that length.
                - Most_Common_Letters (list): A list of tuples where each tuple contains a letter and the number of times
                  it appears in the words that can be formed by using the letters of the gray word.
            - Valid_Words (list): A list of words that can be formed by using the letters of the gray word.

    Returns:
        tuple: A tuple containing a string with a message indicating if the input was valid or not, and the input JSON object.
    """
    
    # Check if gray word and golden word have at least 3 letters
    if len(json_data["Gray_Word"]) < 3 or len(json_data["Golden_Word"]) < 3:
        return "Error: Gray word and golden word must have at least 3 letters", json_data
    
    # Check if gray word and golden word contain only letters
    if not json_data["Gray_Word"].isalpha() or not json_data["Golden_Word"].isalpha():
        return "Error: Gray word and golden word must contain only letters", json_data
    
    # Check if the pair of words already exists in the library
    dictionary_name = json_data["Dictionary_Name"]
    library_file_name = dictionary_name.replace(".json", "_lib.csv")
    if os.path.isfile(library_file_name):
        with open(library_file_name, mode='r') as library_file:
            library_reader = csv.reader(library_file)
            for row in library_reader:
                if row[1] == json_data["Gray_Word"] and row[2] == json_data["Golden_Word"]:
                    return "Error: Pair of words already exists in the library", json_data
    else:
        with open(library_file_name, mode='w', newline='') as library_file:
            library_writer = csv.writer(library_file)
            library_writer.writerow([
                "Timestamp",
                "Gray_Word",
                "Golden_Word",
                "Words_Meeting_Condition",
                "Valid_Words",
                "Words_According_to_Length",
                "Most_Common_Letters"
            ])
    
    # If all checks pass, append the data to the library file
    with open(library_file_name, mode='a', newline='') as library_file:
        library_writer = csv.writer(library_file)
        library_writer.writerow([
            datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            json_data["Gray_Word"],
            json_data["Golden_Word"],
            json_data["Statistics"]["Words_Meeting_Condition"],
            json.dumps(json_data["Valid_Words"]),
            json.dumps(json_data["Statistics"]["Words_According_to_Length"]),
            json.dumps(json_data["Statistics"]["Most_Common_Letters"])
        ])
    
    # Return success message and input JSON
    return "Valid input", json_data

def interpret_response(response):

    if response[0] == "Valid input":
        return True, None, None
    else:
        error_message = response[0]
        gray_word = response[1]["Gray_Word"]
        golden_word = response[1]["Golden_Word"]
        return False, error_message, (gray_word, golden_word)
