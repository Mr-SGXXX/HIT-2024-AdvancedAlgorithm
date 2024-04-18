# 枚举方法求凸包
from time import time
import os
import numpy as np

from draw_figure import draw_current

def enumeration(points:np.ndarray, data_path, draw_flag=False):
    start = time()
    figure_time = draw_current(points, [], os.path.join(data_path, "0.png"))
    original_points = points
    points_num = len(points)
    deleted_percent = 0
    i = 0
    while True:
        if i >= points_num:
            break
        j = 0
        while True:
            if j >= points_num:
                break
            if i == j:
                j += 1
                continue
            k = 0
            while True:
                if k >= points_num:
                    break
                if i == k or j == k:
                    k += 1
                    continue
                p = 0
                while True:
                    if p >= points_num:
                        break
                    if i == p or j == p or k == p:
                        p += 1
                        continue
                    if in_triangle(points[i], points[j], points[k], points[p]):
                        points = np.delete(points, p, axis=0)
                        if (len(original_points) - points_num) % (len(original_points) // 10) == 0 and len(original_points) != points_num:
                            deleted_percent += 1 
                            if draw_flag:
                                figure_time += draw_current(points, [], os.path.join(data_path, f"{deleted_percent}.png"))
                        points_num -= 1
                        if p < i:
                            i -= 1
                        if p < j:
                            j -= 1
                        if p < k:
                            k -= 1
                        p -= 1
                    p += 1
                k += 1
            j += 1
        i += 1
    
    # 以points[i-1]为参考点，按极角逆时针排序
    points = np.array(sorted(points, key=lambda p: (np.arctan2(p[1]-points[i-1][1], p[0]-points[i-1][0]), np.linalg.norm(p-points[i-1]))))
    
    final_edges = []
    edges = []
    for i in range(points_num):
        j = (i + 1) % points_num
        final_edges.append((int(np.where((original_points == points[i])[:, 0])[0]), int(np.where((original_points == points[j])[:, 0])[0])))
        edges.append((i, j))
    if draw_flag:
        figure_time += draw_current(points, edges, os.path.join(data_path, f"edges.png"))
    figure_time += draw_current(original_points, final_edges, os.path.join(data_path, f"final.png"))
    time_cost = time() - start - figure_time
    return time_cost


def in_triangle(p1, p2, p3, p):
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    return cross_product(p1, p2, p) >= 0 and cross_product(p2, p3, p) >= 0 and cross_product(p3, p1, p) >= 0