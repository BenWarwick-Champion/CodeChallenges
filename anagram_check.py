# Write a piece of code to determine if
# two words are anagrams

def anagram_check(word1, word2):
    if len(word1) != len(word2):
        return False
    for char in word1:
        if char not in word2:
            return False
        else:
            word2 = word2.replace(char, ' ', 1)
    return True

if __name__ == "__main__":
    input1 = "granmaa"
    input2 = "anagram"
    if anagram_check(input1, input2):
        print("The words are anagrams")
    else:
        print("The words are not anagrams")
    