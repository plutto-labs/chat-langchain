from spellchecker import SpellChecker

input_file = "input.txt"
output_file = "output.txt"

spell = SpellChecker(language="es", case_sensitive=False)

with open(input_file, "r") as file:
    text = file.read()

# Split the text into individual words
words = text.split()

no_long_words = [word for word in words if len(word) < 30]

# Identify non-real words
non_real_words = [word if not spell.unknown([word]) else spell.correction(word) for word in no_long_words]

# Reconstruct the text without non-real words
new_text = " ".join(non_real_words)

with open(output_file, "w") as file:
    file.write(new_text)

print("Non-real words removed. Output written to", output_file)
