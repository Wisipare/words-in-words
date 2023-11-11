
import json

# Ask user for input file path
input_file_path = input("Enter the path of the input file: ")

# Open input file for reading
with open(input_file_path, 'r') as input_file:
    # Read all lines from input file
    lines = input_file.readlines()
    # Get total number of lines in input file
    total_lines = len(lines)
    # Initialize empty dictionary
    dictionary = {}
    # Loop through each line in input file
    for i, line in enumerate(lines):
        # Remove newline character from line
        line = line.strip()
        # Add line to dictionary with empty list as value
        dictionary[line] = []
        # Print progress message every 100 lines
        if (i+1) % 100 == 0:
            print(f"Processed {i+1} lines out of {total_lines}")
    
# Write dictionary to output file in JSON format
with open('output.json', 'w') as output_file:
    json.dump(dictionary, output_file)
