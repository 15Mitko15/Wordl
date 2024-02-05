with open('6_letter_words.txt', 'r') as txt_file:
    # Read all lines from the file
    lines = txt_file.readlines()

# Open the file in write mode to overwrite its contents
with open('6_letter_words.txt', 'w') as txt_file:
    # Iterate through each line (word) in the file
    for line in lines:
        # Convert the word to lowercase and write it to the file
        txt_file.write(line.strip().lower() + '\n')