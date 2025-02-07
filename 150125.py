# import numpy as np 

x = [10, 15, 3, 8]

k = 17

def find_pair_with_sum(x, k):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] + x[j] == k:
                return True
    return False

print(find_pair_with_sum(x, k))
