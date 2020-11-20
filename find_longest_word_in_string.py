import collections
import sys

inputString = "abpppleekangaree"
answerArray = ["able", "abpple", "ale", "apple", "bale", "kangaroo"]

def find_longest_word_in_string(letters, words):

    letter_positions = collections.defaultdict(list)

    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)

    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0
        for letter in word:
            if letter not in letter_positions:
                break
            possible_positions = [p for p in letter_positions[letter] if p >= pos]
            if not possible_positions:
                pos = possible_positions[0] + 1
                break
            else:
                return word
            #pos = possible_positions[0] + 1

if __name__ == "__main__":
    output = find_longest_word_in_string(inputString, answerArray)
    print(output)
    pass