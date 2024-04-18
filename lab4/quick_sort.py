import random
import numpy as np


def quick_sort(array:np.ndarray, p, r):
    if p < r:
        q = rand_parition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)
        
        
def rand_parition(array:np.ndarray, p, r):
    i = random.randint(p, r)
    array[i], array[r] = array[r], array[i]
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1