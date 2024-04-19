import random
import numpy as np
import os
from time import time

from draw_figures import draw_bar_chart


def quick_sort_3way(array:np.ndarray, p, r, figure_dir, draw_flag=False, entry=True):
    global figure_time
    global df 
    global total_figure_cost
    if entry:
        if draw_flag:
            draw_bar_chart(array, os.path.join(figure_dir, f"original.png"))
        figure_time = 1
        df = draw_flag
        start_time = time()
        total_figure_cost = 0
    if p < r:
        lt, gt, figure_cost = rand_parition_3way(array, p, r, figure_dir)
        total_figure_cost += figure_cost
        if lt != p or gt != r:
            # if figure_time % 100000 == 0:
            #     print(f"{figure_time} steps are used to sort the array.")
            quick_sort_3way(array, p, lt - 1, figure_dir, entry=False)
            quick_sort_3way(array, gt + 1, r, figure_dir, entry=False)
        
    if entry:
        time_cost = time() - start_time - total_figure_cost
        if draw_flag:
            draw_bar_chart(array, os.path.join(figure_dir, f"final.png"))
        return figure_time - 1, time_cost
    else:
        return None, None
        
        
def rand_parition_3way(array:np.ndarray, p, r, figure_dir):
    global figure_time
    global df
    pi = random.randint(p, r)
    pivot = array[pi]
    array[pi], array[r] = array[r], array[pi]
    lt = p
    gt = r
    i = p
    while i < gt:
        if array[i] < pivot:
            array[lt], array[i] = array[i], array[lt]
            i += 1
            lt += 1
        elif array[i] > pivot:
            array[gt], array[i] = array[i], array[gt]
            gt -= 1
        else:
            i += 1
    if df:
        time_cost = draw_bar_chart(array, os.path.join(figure_dir, f"{figure_time}.png"))
    else:
        time_cost = 0
    figure_time += 1
    return lt, gt, time_cost