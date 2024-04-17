# graham scan方法求凸包
from time import time
import os

from draw_figure import draw_current

def graham_scan(points, data_path):
    draw_current(points, [], os.path.join(data_path, "0.png"))
    start = time()
    figure_time = 0
    # 1. 找到最下方的点
    min_point = points[0]
    for point in points:
        if point[1] < min_point[1]:
            min_point = point
        elif point[1] == min_point[1] and point[0] < min_point[0]:
            min_point = point
    # 2. 按照极角排序
    points = sorted(points, key=lambda x: (x[1] - min_point[1]) / (x[0] - min_point[0]))
    # 3. 扫描
    stack = [min_point, points[0], points[1]]
    for i in range(2, len(points)):
        while len(stack) > 1 and (stack[-1][0] - stack[-2][0]) * (points[i][1] - stack[-2][1]) - (stack[-1][1] - stack[-2][1]) * (points[i][0] - stack[-2][0]) < 0:
            stack.pop()
        stack.append(points[i])
        figure_time += draw_current(points, [(stack[i], stack[i + 1]) for i in range(len(stack) - 1)], os.path.join(data_path, f"{i}.png"))
    return time() - start - figure_time
        