# John and Mary want to travel between a few towns A, B, C ... 
# Mary has on a sheet of paper a list of distances between these towns. 
# ls = [50, 55, 57, 58, 60]. 
# John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles 
# and he will visit only 3 towns.

# Which distances, hence which towns, will they choose to visit
# such that the sum of the distances is the largest possible?



# My Solution
import itertools
def choose_best_sum(t, k, ls):
    combos = list(itertools.combinations(ls, k))
    
    bestSum = 0
    for combo in combos:
        currSum = sum(combo)
        if currSum > bestSum and currSum <= t:
            bestSum = currSum
    
    if bestSum == 0:
        return None
    return bestSum

# Best Solution
import itertools
def choose_best_sum(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None
