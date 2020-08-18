# The Morse code encodes every character as a sequence of "dots" and "dashes". 
# For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. 
# The Morse code is case-insensitive, traditionally capital letters are used. 
# When the message is written in Morse code, a single space is used to separate the character codes 
# and 3 spaces are used to separate words. 
# For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

# NOTE: Extra spaces before or after the code have no meaning and should be ignored.

# In addition to letters, digits and some punctuation, there are some special service codes, 
# the most notorious of those is the international distress signal SOS (that was first issued by Titanic), 
# that is coded as ···−−−···. 
# These special codes are treated as single special characters, and usually are transmitted as separate words.

# Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.


# My Solution
def decodeMorse(morse_code):
    decoded = []
    output = morse_code.replace("   ", " # ").split()

    for code in output:
        if code != '#':
            code = MORSE_CODE[code]
        decoded.append(code)
        
    output = ("".join(decoded)).replace("#", " ")
    
    return output.strip()

# Best Solution
def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))

# ...There's always someone that can do it one line.