import numpy as np
import os
import shutil
import sys
from time import time
from copy import deepcopy

from quick_sort import quick_sort
from quick_sort_3way import quick_sort_3way
from draw_figures import gen_gif, draw_step, draw_time
from generate_data import generate_data

DATA_DIR = "./lab4/results"

def main():
    sys.setrecursionlimit(30000)
    data_num = 1000000
    # data_num = 200
    data_dir = os.path.join(DATA_DIR, f"{data_num}")
    draw_flag = True if data_num <= 1000 else False
    shutil.rmtree(data_dir, ignore_errors=True)
    step_list = []
    step_improve_list = []
    time_list = []
    time_improve_list = []
    default_time_list = []
    for i in range(0, 11):
        data = generate_data(data_num, i)
        figure_dir = os.path.join(data_dir, f"{i}")
        os.makedirs(figure_dir)
        figure_steps, time_cost = quick_sort(deepcopy(data), 0, len(data) - 1, figure_dir, draw_flag)
        time_list.append(time_cost)
        step_list.append(figure_steps)
        print(f"Data {i} is sorted by default method in {figure_steps} steps in {time_cost} seconds")
        if draw_flag:
            gen_gif(figure_dir, "quick_sort.gif")
        start_time = time()
        sorted(deepcopy(data))
        time_cost = time() - start_time
        print(f"Data {i} is sorted by Python method in {time_cost} seconds")
        default_time_list.append(time_cost)
        figure_steps, time_cost = quick_sort_3way(deepcopy(data), 0, len(data) - 1, figure_dir, False)
        print(f"Data {i} is sorted by 3-way quick sort in {figure_steps} steps in {time_cost} seconds")
        time_improve_list.append(time_cost)
        step_improve_list.append(figure_steps)
    draw_time(time_improve_list, os.path.join(data_dir, "time_improved.png"))
    draw_step(step_improve_list, os.path.join(data_dir, "step_improved.png"))
    draw_time(time_list, os.path.join(data_dir, "time.png"))
    draw_time(default_time_list, os.path.join(data_dir, "python_time.png"))
    draw_step(step_list, os.path.join(data_dir, "step.png"))
    
if __name__ == "__main__":
    main()