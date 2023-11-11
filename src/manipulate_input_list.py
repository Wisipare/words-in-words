import csv
from process_words import process_words
from manipulate_words_library import create_or_update_library, interpret_response

def manipulate_input_list(input_file_path, dictionary_file_path):
    """
    This function reads an input file containing pairs of words, processes them to find all valid words that can be formed
    using the letters of the first word and the second word, and adds those valid words to a library.
    
    Args:
    - input_file_path (str): The path to the input file containing pairs of words.
    - dictionary_file_path (str): The path to the dictionary file containing a list of valid words.
    
    Returns:
    - result (tuple): A tuple containing the number of successful updates, the number of failed updates, and a list of problems encountered.
    """
    success_count = 0
    failure_count = 0
    problems = []
    
    # Load the input file into memory
    with open(input_file_path, "r") as input_file:
        reader = csv.reader(input_file)
        total_rows = sum(1 for row in reader)  # Get the total number of rows
        input_file.seek(0)  # Reset the file pointer to the beginning of the file
        
        # Check if the first line contains "gris" or "gray" in the first column and "dorada" or "gold" in the second column
        first_row = next(reader)
        if len(first_row) >= 2 and ("gris" in first_row[0].lower() or "gray" in first_row[0].lower()) and ("dorada" in first_row[1].lower() or "gold" in first_row[1].lower()):
            pass  # Skip the first line
        else:
            gray_word, gold_word = first_row[0], first_row[1]
            valid_words = process_words(gray_word, gold_word, dictionary_file_path)
            library_update = create_or_update_library(valid_words)  # Add the valid words to the library
            result = interpret_response(library_update)
            if result[0]:
                success_count += 1
            else:
                failure_count += 1
                problems.append((result[1], result[2]))

            # Process the rest of the file
            current_row = 2
            for row in reader:
                gray_word, gold_word = row[0], row[1]
                valid_words = process_words(gray_word, gold_word, dictionary_file_path)
                library_update = create_or_update_library(valid_words)  # Add the valid words to the library
                result = interpret_response(library_update)
                if result[0]:
                    success_count += 1
                else:
                    failure_count += 1
                    problems.append((result[1], result[2]))
                
                # Print progress
                print(f"Processed row {current_row}/{total_rows} of the input file")
                current_row += 1

    return (success_count, failure_count, problems)

def print_results(results):
    print(f"Number of correctly added pairs: {results[0]}")
    print(f"Number of pairs with errors: {results[1]}")
    print("Errors:")
    for error in results[2]:
        print(f"\t{error[0]}: {error[1]}")
