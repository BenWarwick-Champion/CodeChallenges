# Write a function that takes in a string of one or more words, 
# and returns the same string, but with all five or more letter words reversed.
# Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.

# My Solution
def spin_words(sentence):
    words = sentence.split(" ")
    rSentence = sentence
    for word in words:
        if len(word) > 4:
            reverse = word[::-1]
            rSentence = rSentence.replace(word, reverse)
    return rSentence


# Best Solution
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])