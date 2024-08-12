"""
Exercise 12: Vowel Counter

Write a program that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string. Store the vowels in a set to ensure each is counted only once, and print the count.

"""
word = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for letter in word:
    if letter in vowels:
        count += 1
print(f"The word {word} has "+str(count) +" vowels")

