import random
from copy import deepcopy

def generate_data(data_num):
    x = [i for i in range(data_num)]
    x_left = deepcopy(x)
    s_0 = random.sample(x_left, 20)
    s_union = set()
    for s in s_0:
        s_union.add(s)
        x_left.remove(s)
    F = [s_0]
    while len(x_left) > 0:
        if len(x_left) < 20:
            s = x_left
            F.append(s)
            break
        n = random.randint(1, 20)
        m = random.randint(1, n)
        s_i = random.sample(x_left, m)
        s_i += random.sample(s_union, n-m)
        F.append(s_i)
        for s in s_i:
            s_union.add(s)
            if s in x_left:
                x_left.remove(s)
    while len(F) < data_num:
        F.append(random.sample(s_union, random.randint(1, 20)))
    return x, F
        

