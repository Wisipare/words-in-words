import os
import datetime
import json
import requests
import urllib3
import json
import process_words
import choose_dictionary


def send_processed_words(json_data, api_url, date_from_str=None):
    # Convert the JSON string to a Python dictionary
    json_data = json.loads(json_data)

    # Add the date_from to the JSON
    if date_from_str is not None:
        date_from = datetime.datetime.strptime(date_from_str, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'
    else:
        date_from = datetime.datetime.utcnow().isoformat() + 'Z'
    json_data['date_from'] = date_from

    # Make the API call
    url = api_url
    headers = {'Content-Type': 'application/json'}

    json_data = format_json_for_api_call(json_data)
    print(json_data)
    response = requests.post(url, headers=headers, json=json_data)

    # Print the response
    print(response.text)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def format_json_for_api_call(result):
    # Modify the JSON data to include the words according to length and the most common letters as a list of strings
    json_data = {}
    json_data['Gray_Word'] = result['Gray_Word']
    json_data['Golden_Word'] = result['Golden_Word']
    json_data['Valid_Words'] = [word for word in result['Valid_Words']]
    json_data['Statistics'] = {}
    words_length = result['Statistics']['Words_According_to_Length']
    words_common_letters = result['Statistics']['Most_Common_Letters']
    words_length = [f'{k}:{words_length[k]}' for k in words_length.keys()]
    words_common_letters = [f'{k}:{words_common_letters[k]}' for k in words_common_letters.keys()]
    json_data['Statistics']['Words_According_to_Length'] = words_length
    json_data['Statistics']['Most_Common_Letters'] = words_common_letters
    json_data['Valid_Words_Count'] = len(result['Valid_Words'])
    json_data['Date_From'] =  result['date_from']
    json_data['Game_Id'] =  result['Game_Id']

    # Get the language code from the dictionary file name
    dictionary_path = result['Dictionary_Name']
    language_code = os.path.basename(dictionary_path)[:2]
    if language_code in ['en', 'es', 'fr', 'de', 'it']:
        json_data['Language_Code'] = language_code
    else:
        json_data['Language_Code'] = 'unknown'

    return json_data



def request_words_game_bubble(gray_word, gold_word, dictionary_name=None, game_choice=1, add_to_library=False, make_api_call=False):
    # Get the path to the selected dictionary
    dictionary_path = choose_dictionary.choose_dictionary(dictionary_name)

    # Call the process_words function with the user inputs
    result = process_words.process_words(gray_word, gold_word, dictionary_path, None, game_choice)

    # Print the statistics of the valid words found, their dimensions, and the most repeated letters
    print("#" * 50)
    print(f"Number of valid words found: {len(result['Valid_Words'])}")
    print(f"Dimensions of words: {result['Statistics']['Words_According_to_Length']}")
    print(f"Most repeated letters: {result['Statistics']['Most_Common_Letters']}")
    print("#" * 50)

    # If the user wants to add the gray and gold words to the library, call the add_word_to_library function
    if make_api_call:
        json_data = json.dumps(result)
        print(json_data)

        # Ask the user if they want to make the API call
        print("=" * 50)
        make_api_call_input = input("Do you want to make the API call with the JSON data? (yes/no): ")
        if make_api_call_input.lower() == 'yes':
            url = 'https://wordsinwords.bubbleapps.io/version-test/api/1.1/wf/create_daily_game/'
            send_processed_words(json_data, url)
    
    # Return a dictionary indicating success or failure
    return {"success": True}
