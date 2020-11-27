# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
# because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. 
# Return True if it is, False if not. 
# Ignore numbers and punctuation.

# My solution:
def is_pangram(s):
    seen = set()
    for char in s:
        if not char.isalpha():
            continue
        if char.lower() in seen:
            continue
        seen.add(char.lower())

    if len(seen) == 26:
        return True
    
    return False

# More Pythonic Solution:
import string

def is_pangram2(s):
    return set(string.lowercase) <= set(s.lower())


if __name__ == "__main__":
    pangram = "The quick, brown fox jumps over the lazy dog!"
    if is_pangram(pangram):
        print("That's a pangram")
    else:
        print("Not a pangram")