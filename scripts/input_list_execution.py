import os
import sys
sys.path.append('/Users/pablorsc/words-in-words/src')
sys.path.append('/Users/pablorsc/words-in-words/data')

import json
from manipulate_input_list import manipulate_input_list, print_results
import os
import sys
import json
from manipulate_input_list import manipulate_input_list, print_results


# Step 1: Show list of .csv files and ask user to select one
input_dir = 'data/input_lists'
input_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
print('Select an input file:')
for i, f in enumerate(input_files):
    print(f'{i+1}. {f}')
selection = int(input()) - 1
input_file_path = os.path.join(input_dir, input_files[selection])

# Step 2: Show list of .json files and ask user to select one
dict_dir = 'data/dictionaries'
dict_files = [f for f in os.listdir(dict_dir) if f.endswith('.json')]
print('Select a dictionary file:')
for i, f in enumerate(dict_files):
    print(f'{i+1}. {f}')
selection = int(input()) - 1
dictionary_file_path = os.path.join(dict_dir, dict_files[selection])


# Step 3: Call manipulate_input_list function with input and dictionary urls as parameters
"""
Call manipulate_input_list function with input and dictionary urls as parameters.
"""

results = manipulate_input_list(input_file_path, dictionary_file_path)
print_results(results)

# Step 4: Ask user if they want to send any of the results to Bubble
send_to_bubble = input('Do you want to send any of the results to Bubble? (yes/no) ')
if send_to_bubble.lower() == 'yes':
    print('Select the pairs of words you want to send to Bubble (separated by commas):')
    for i, result_dict in enumerate(results):
        print(f'{i+1}. {result_dict["input_word"]}: {", ".join(result_dict["output_words"])}')
    selection = input()
    selection = [int(s.strip()) for s in selection.split(',') if s.strip().isdigit() and int(s.strip()) <= len(results)]
    selected_results = [results[i-1] for i in selection]
    # TODO: Implement actions to send selected results to Bubble
