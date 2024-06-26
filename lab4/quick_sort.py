import random
import numpy as np
import os
from time import time

from draw_figures import draw_bar_chart


def quick_sort(array:np.ndarray, p, r, figure_dir, draw_flag=False, entry=True):
    global figure_time
    global df 
    global total_figure_cost
    if entry:
        if draw_flag:
            draw_bar_chart(array, os.path.join(figure_dir, f"original.png"))
        if len(array) == 1000000 and np.all(array == 1):
            return 1000000, np.inf # 一百万个相同数据点在运行这段代码时，会出现严重的性能问题，导致程序崩溃
        figure_time = 1
        df = draw_flag
        start_time = time()
        total_figure_cost = 0
    if p < r:
        q, figure_cost = rand_parition(array, p, r, figure_dir)
        total_figure_cost += figure_cost
        # if figure_time % 100000 == 0:
        #     print(f"{figure_time} steps are used to sort the array.")
        quick_sort(array, p, q - 1, figure_dir, entry=False)
        quick_sort(array, q + 1, r, figure_dir, entry=False)
        
    if entry:
        time_cost = time() - start_time - total_figure_cost
        if draw_flag:
            draw_bar_chart(array, os.path.join(figure_dir, f"final.png"))
        return figure_time - 1, time_cost
    else:
        return None, None
        
        
def rand_parition(array:np.ndarray, p, r, figure_dir):
    global figure_time
    global df
    i = random.randint(p, r)
    array[i], array[r] = array[r], array[i]
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    if df:
        time_cost = draw_bar_chart(array, os.path.join(figure_dir, f"{figure_time}.png"))
    else:
        time_cost = 0
    figure_time += 1
    return i + 1, time_cost