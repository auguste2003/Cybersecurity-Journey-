"""
Exercise 10: Unique Words in a Sentence

Write a program that takes a sentence as input and returns the set of unique words in that sentence.
"""
words = input("Enter a sentence: ")
unique_words = set(words)
print(unique_words)

# Take a sentence as input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words using the split() method
words = sentence.split()

# Convert the list of words into a set to get unique words
unique_words = set(words)

# Print the set of unique words
print("Unique words in the sentence:", unique_words)
