# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

# Input will consist of a list of lists containing two items each. 
# Each list contains information for a single potential member. 
# Information consists of an integer for the person's age and an integer for the person's handicap.
# Example Input:
# [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
# Example Output:
# ["Open", "Open", "Senior", "Open", "Open", "Senior"]

# My Solution
def open_or_senior(data):
    
    member = []
    
    for person in data:
        if person[0] > 54 and person[1] > 7:
            member.append('Senior')
        else:
            member.append('Open')
    return member


# Best Solution
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]