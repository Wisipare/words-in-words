import json
import unicodedata
from collections import Counter
from manipulate_dictionary_library import load_dictionary, choose_dictionary    


def verify_word_condition_1(word, gray_word, golden_word):
    """
    Verify if a word meets the condition to be considered valid for game 1.

    A word is considered valid if its odd-indexed letters are contained in the gray word and its even-indexed letters
    are contained in the golden word.

    Args:
        word (str): The word to verify.
        gray_word (str): The gray word to compare with.
        golden_word (str): The golden word to compare with.

    Returns:
        bool: True if the word meets the condition, False otherwise.
    """
    odd_letters_word = [letter for i, letter in enumerate(word) if i % 2 == 0]
    even_letters_word = [letter for i, letter in enumerate(word) if i % 2 != 0]


    # Verify if the odd-indexed letters of the word are contained in the gray word
    odd_letters_valid = all(letter in gray_word and gray_word.count(letter) >= odd_letters_word.count(letter) for letter in odd_letters_word)

    # Verify if the even-indexed letters of the word are contained in the golden word
    even_letters_valid = all(letter in golden_word for letter in even_letters_word)

    return odd_letters_valid and even_letters_valid

def verify_word_condition_2(word, gray_word, golden_word):
    """
    Verify if a word meets the condition to be considered valid for game 2.

    A word is considered valid if its odd-indexed letters are contained in the golden word and its even-indexed letters
    are contained in the gray word.

    Args:
        word (str): The word to verify.
        gray_word (str): The gray word to compare with.
        golden_word (str): The golden word to compare with.

    Returns:
        bool: True if the word meets the condition, False otherwise.
    """
    # Remove all letters that are already in the golden word
    reduced_word = ''.join([letter for letter in word if letter not in golden_word])

    # Verify if all remaining letters are in the gray word and their count is less than or equal to the count in the gray word
    result = all(letter in gray_word and gray_word.count(letter) >= reduced_word.count(letter) for letter in reduced_word)
    return result

def verify_word_condition_3(word, gray_word, golden_word):
    """
    Verify if a word meets the condition to be considered valid for game 3.

    A word is considered valid if its letters are contained in the gray word and the golden word, but the letters
    in the even positions must be different from the letters in the odd positions.

    Args:
        word (str): The word to verify.
        gray_word (str): The gray word to compare with.
        golden_word (str): The golden word to compare with.

    Returns:
        bool: True if the word meets the condition, False otherwise.
    """
    pass

def verify_word_condition_4(word, gray_word, golden_word):
    """
    Verify if a word meets the condition to be considered valid for game 4.

    A word is considered valid if its letters are contained in the gray word and the golden word, but the letters
    in the odd positions must be different from the letters in the even positions.

    Args:
        word (str): The word to verify.
        gray_word (str): The gray word to compare with.
        golden_word (str): The golden word to compare with.

    Returns:
        bool: True if the word meets the condition, False otherwise.
    """
    pass

def process_words(gray_word, golden_word, dictionary_file_path, num_words_to_consider=None, game_id=1):
    """
    Process a dictionary to find valid words that meet the condition.

    A word is considered valid if its letters meet the condition for the selected game.

    Args:
        gray_word (str): The gray word to compare with.
        golden_word (str): The golden word to compare with.
        dictionary_file_path (str): The path to the JSON file containing the dictionary.
        num_words_to_consider (int, optional): The number of words to consider from the dictionary. Defaults to None.
        game_id (int, optional): The id of the game to play. Defaults to 1.

    Returns:
        dict: A dictionary containing the summary of the process and the list of valid words.
    """
    # Load the dictionary from the JSON file and normalize its words
    dictionary = load_dictionary(dictionary_file_path)

    # Verify if the dictionary was loaded correctly
    if not dictionary:
        return None

    if num_words_to_consider is None:
        num_words_to_consider = len(dictionary)  # Consider the whole dictionary

    # List to store valid words
    valid_words = []

    # Set of letters from the gray word to verify the beginning of the dictionary words
    initial_letters_gray_word = set(letter for i, letter in enumerate(gray_word) if i % 2 == 0)

    # Select the function to verify the words according to the game id
    if game_id == 1:
        verify_word_condition = verify_word_condition_1
    elif game_id == 2:
        verify_word_condition = verify_word_condition_2
    elif game_id == 3:
        verify_word_condition = verify_word_condition_3
    elif game_id == 4:
        verify_word_condition = verify_word_condition_4
    else:
        return {"Error": f"Invalid game id: {game_id}"}

    # Loop to verify and store the words that meet the condition
    for word in dictionary[:num_words_to_consider]:
        # Optimization: discard words that do not start with any letter from the gray word
        if not any(letter in initial_letters_gray_word for letter in word):
            continue

        # New condition: discard words whose length is greater than twice the length of the gray word
        if len(word) >= 4 and len(word) <= 2 * len(gray_word) and verify_word_condition(word, gray_word, golden_word):
            valid_words.append(word)

    # Summary
    summary = {
        "Gray_Word": gray_word,
        "Golden_Word": golden_word,
        "Dictionary_Name": dictionary_file_path,
        "Game_Id": game_id,
        "Statistics": {
            "Words_Meeting_Condition": len(valid_words),
            "Words_According_to_Length": dict(Counter(len(word) for word in valid_words)),
            "Most_Common_Letters": dict(Counter("".join(valid_words)).most_common())
        },
        "Valid_Words": valid_words
    }

    return summary

# Example of how to use the function
if __name__ == "__main__":
    result = process_words("atadura", "iblacked", "/Users/pablorsc/words-in-words/data/dictionaries/en_dictionary.json", 10000, 1)

    # Print the result in JSON format
    if result:
        print(json.dumps(result, indent=4))
