# graham scan方法求凸包
from time import time
import os
import numpy as np

from draw_figure import draw_current

def graham_scan(points:np.ndarray, data_path, draw_flag=False):
    start = time()
    figure_time = draw_current(points, [], os.path.join(data_path, "0.png"))
    # 1. 找到最下方的点
    min_point = points[points[:, 1].argmin()]

    # 2. 按照极角排序
    points = np.array(sorted(np.delete(points, points[:, 1].argmin(), axis=0), key=lambda p: np.arctan2(p[1]-min_point[1], p[0]-min_point[0])))
    points = np.insert(points, 0, min_point, axis=0)
    
    # 3. 扫描
    stack = [0, 1, 2]
    for i in range(3, len(points)):
        while len(stack) > 1 and (points[stack[-1]][0] - points[stack[-2]][0]) * \
            (points[i][1] - points[stack[-2]][1]) - (points[stack[-1]][1] - points[stack[-2]][1]) * (points[i][0] - points[stack[-2]][0]) < 0:
            stack.pop()
        stack.append(i)
        if draw_flag:
            figure_time += draw_current(points, [(stack[i], stack[i + 1]) for i in range(len(stack) - 1)], os.path.join(data_path, f"{i}.png"))
    figure_time += draw_current(points, [(stack[i], stack[i + 1]) for i in range(len(stack) - 1)] + [(stack[-1], 0)], os.path.join(data_path, f"final.png"))
    time_cost = time() - start - figure_time
    return time_cost
        