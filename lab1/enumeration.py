# 枚举方法求凸包
from time import time
import os
import numpy as np

from draw_figure import draw_current

def enumeration(points:np.ndarray, data_path):
    draw_current(points, [], os.path.join(data_path, "0.png"))
    original_points = points
    start = time()
    figure_time = 0
    points_num = len(points)
    i = 0
    while True:
        last_points_num = points_num
        if i == points_num:
            break
        j = i + 1
        while True:
            if j == points_num:
                break
            k = j + 1
            while True:
                if k >= points_num:
                    break
                p = k + 1
                while True:
                    if p >= points_num:
                        break
                    if in_triangle(points[i], points[j], points[k], points[p]):
                        points = np.delete(points, p, axis=0)
                        points_num -= 1
                    p += 1
                k += 1
            j += 1
        i += 1
        if last_points_num > points_num:
            last_points_num = points_num
            figure_time += draw_current(points, [], os.path.join(data_path, f"{i}.png"))
                  
        
    
    points = sorted(points, key=lambda p: (p[0], p[1]))
    edges = []
    for i in range(points_num):
        j = (i + 1) % points_num
        edges.append((int(np.where(original_points == points[i])), int(np.where(original_points, points[j]))))
    figure_time += draw_current(original_points, edges, os.path.join(data_path, f"final.png"))
    return time() - start - figure_time


def in_triangle(p1, p2, p3, p):
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    return cross_product(p1, p2, p) >= 0 and cross_product(p2, p3, p) >= 0 and cross_product(p3, p1, p) >= 0