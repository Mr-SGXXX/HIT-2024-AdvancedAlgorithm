import numpy as np
import random

def generate_data(n, i):
    if i == 10:
        return np.array([1] * n)
    num_repeats = int(n * 10 * i / 100)
    num_unique = n - num_repeats
    unique_elements = list(range(num_unique))
    repeated_elements = random.choices(unique_elements, k=num_repeats)
    dataset = unique_elements + repeated_elements
    random.shuffle(dataset)
    return np.array(dataset)
