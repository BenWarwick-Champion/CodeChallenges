# Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

# My Solution
def pig_it(text):
    workString = text.split(" ")
    resString = []
    for word in workString:
        if word.isalpha():
            newWord = word[1:] + word[0] + "ay"
            resString.append(newWord)
        else:
            resString.append(word)
    return " ".join(resString)


# Best Solution
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
