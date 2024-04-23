
def greedy(F, x):
    x_found = set()
    C = []
    while len(x_found) < len(x):
        i, max_s = max(enumerate(F), key=lambda s: len(s[1]) - len(set(s[1]).intersection(x_found)))
        C.append(i)
        x_found = x_found.union(set(max_s))
    return C
    