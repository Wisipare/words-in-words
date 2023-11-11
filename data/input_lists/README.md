
## Input Lists

Input lists are CSV files that contain pairs of words that will be processed for some dictionary. Essentially, they come from asking the artificial intelligence. This way, we can generate pairs of words massively that will later be analyzed by our logic and thus decide if they are suitable to be used in the words-in-words game.

The CSV files must always have the same structure, the first word is the gray word, the second word is the golden word.

# Example of an Input List CSV file fragment:
# gray_word,golden_word
cat,act
listen,silent
astronomer,moonstarer
school,chaos
happy,pharmacy
# Note: Do not include the header in the actual CSV file.

These files will be called by the functions in the manipulate_input_list.py library, in src.
