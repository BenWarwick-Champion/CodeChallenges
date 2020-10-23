import time
import numpy as np


# This solution works but it has O(n^2) time complexity
# this means it only passes 10/15 tests. 
def minimum_loss(prices):
    min_loss = max(prices)
    for ind, n in enumerate(prices):
        for i in range(ind+1, len(prices)):
            loss = n - prices[i]
            if 0 < loss < min_loss:
                min_loss = loss
    return min_loss

# Looking for O(log(n)) time complexity
def fast_minimum_loss(prices):
    price_dict = {index : price for index, price in enumerate(prices)}
    print(price_dict)

    prices.sort()

    pass

    

if __name__ == "__main__":
    #input = [20, 7, 8, 2, 5]
    input = np.random.randint(1, 101, 1000)
    start_std = time.perf_counter()
    minimum_loss(input)
    end_std = time.perf_counter()
    start_fast = time.perf_counter()
    fast_minimum_loss(input)
    end_fast = time.perf_counter()
    print('Standard = ' + str(end_std - start_std))
    print('Fast = ' + str(end_fast - start_fast))

