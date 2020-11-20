# Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; 
# there are no other people in the queue. 
# The first one in the queue (Sheldon) buys a can, drinks it and doubles! 
# The resulting two Sheldons go to the end of the queue. 
# Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

# My Solution
def who_is_next(names, r):
    while r > len(names):
        r = (r - (len(names)-1)) // 2
    return names[r - 1]

# Best Solution
def whoIsNext(names, r):
    while r > 5:
        r = (r - 4) / 2
    return names[r-1]