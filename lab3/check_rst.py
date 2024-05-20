def check_rst(x, F, C):
    found_x = set()
    for subset_index in C:
        for element in F[subset_index]:
            found_x.add(element)
    
    if found_x != set(x):
        return False
    else:
        return True