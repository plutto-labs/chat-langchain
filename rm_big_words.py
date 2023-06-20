
# input_file = "input.txt"
# output_file = "output.txt"

# with open(input_file, "r") as file:
#     text = file.read()

# # Split the text into individual words
# words = text.split()

# no_long_words = [word for word in words if len(word) < 30]

# new_text = " ".join(no_long_words)

# with open(output_file, "w") as file:
#     file.write(new_text)

# print("Non-real words removed. Output written to", output_file)

import re

input_file = "input.txt"
output_file = "output.txt"
# words with repeating characters pattern
pattern = r"\b(\b(?!\d+\b)\w*(\w)\2{2,}\w*\b)"
replacement = ""

with open(input_file, "r") as file:
    text = file.read()

new_text = re.sub(pattern, replacement, text)

# words with more than 22 characters pattern
lines = new_text.split("\n")

# Split each line into words
words = [line.split() for line in lines]

no_long_words = []

for line in words:
    new_line = []
    for word in line:
        if len(word) < 22:
            new_line.append(word)
    if len(new_line) > 0:
        no_long_words.append(new_line)

words = no_long_words
# Join the words using the same spaces and newlines
output_text = "\n".join([" ".join(line) for line in words])

# new_text = " ".join(no_long_words)

with open(output_file, "w") as file:
    file.write(output_text)

print("Words with repeated non-numeric characters replaced. Output written to", output_file)

words = output_text.split()  # Split text into individual words

words_lengths = [(word, len(word)) for word in words]
words_lengths.sort(key=lambda x: x[1], reverse=True)  # Sort words by length in descending order

top_10_longest = words_lengths[:10]

for word, length in top_10_longest:
    print("Word:", word, "\tLength:", length)
