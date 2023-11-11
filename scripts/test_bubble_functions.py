# mi_script.py
import sys
sys.path.append('/Users/pablorsc/words-in-words/src')
from bubbleio_library import request_words_game_bubble

# Definir valores para los argumentos
gray_word = "Alcantarilla"
gold_word = "golem"
dictionary_name = "en_dictionaty.json"
game_choice = 1
add_to_library = False
make_api_call = True

# Llamar a la función
request_words_game_bubble(gray_word, gold_word, dictionary_name, game_choice, add_to_library, make_api_call)
