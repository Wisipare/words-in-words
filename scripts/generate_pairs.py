import json
import os
import random
from datetime import datetime
import json
import os
import random
from datetime import datetime


def generate_pairs(num_pairs=100):
    """
    Generates pairs of random words from a selected dictionary file and saves them in a CSV file.
    The CSV file will have the name "pairs_{dictionary_name}_{current_date}.csv".
    """
    dictionary_files = os.listdir('/Users/pablorsc/words-in-words/data/dictionaries')
    print('Select a dictionary file:')
    for i, file in enumerate(dictionary_files):
        print(f'{i+1}. {file}')

    selected_file = input('Enter the number of the file you want to use: ')
    selected_file = dictionary_files[int(selected_file)-1]
    
    num_pairs = int(input('Enter the number of pairs you want to generate: '))

    with open(f'/Users/pablorsc/words-in-words/data/dictionaries/{selected_file}') as f:
        dictionary = json.load(f)

    def choose_gold_word():
        """
        Chooses a random word from the dictionary with 3-5 letters and no repeated letters.
        """
        while True:
            word = random.choice(list(dictionary.keys()))
            if len(word) >= 3 and len(word) <= 5 and len(set(word)) == len(word):
                return word

    pairs = ''
    for i in range(num_pairs):
        while True:
            word1 = random.choice(list(dictionary.keys()))
            if len(word1) >= 5 and len(word1) <= 10:
                break
        word2 = choose_gold_word()
        pairs += f"{word1},{word2}\n"

    current_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"pairs_{selected_file}_{current_date}.csv"
    with open(f'/Users/pablorsc/words-in-words/{file_name}', 'w') as f:
        f.write(pairs)



if __name__ == '__main__':
    generate_pairs()
