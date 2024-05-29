import string

# Read the file content
with open('input.txt', 'r') as file:
    text = file.read()

# 1. Count the number of words and sentences
words = text.split()
num_words = len(words)
num_sentences = text.count('.') + text.count('!') + text.count('?') + text.count(',')

# 2. Count the number of digits
num_digits = sum(c.isdigit() for c in text)

# 3. Transpose each word (reverse the characters in each word)
transposed_text = ' '.join(word[::-1] for word in words)

# 4. Transform small letters to capital letters and vice versa
transformed_text = text.swapcase()

# 5. Change each letter to its ASCII code
ascii_codes = ' '.join(str(ord(c)) for c in text)

# 6. Archive the text based on an effective rule (simple RLE encoding)
def rle_encode(data):
    encoding = ''
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        encoding += data[i] + str(count)
        i += 1
    return encoding

archived_text = rle_encode(text)

# Save results to an external file
with open('output.txt', 'w') as file:
    file.write("1. ")
    file.write(f"Number of words: {num_words}\n")
    file.write(f"Number of sentences: {num_sentences}\n\n")
    file.write("2. ")
    file.write(f"Number of digits: {num_digits}\n\n")
    file.write("3. ")
    file.write(f"Transposed text: {transposed_text}\n\n")
    file.write("4. ")
    file.write(f"Transformed text: {transformed_text}\n\n")
    file.write("5. ")
    file.write(f"ASCII codes: {ascii_codes}\n\n")
    file.write("6. ")
    file.write(f"Archived text: {archived_text}\n\n")

print('Results are saved in "output.txt".')
