# 枚举方法求凸包
from time import time
import os

from draw_figure import draw_current

def enumeration(points, data_path):
    draw_current(points, [], os.path.join(data_path, "0.png"))
    start = time()
    figure_time = 0
    edges = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            flag = True
            for k in range(len(points)):
                if k == i or k == j:
                    continue
                if (points[j][0] - points[i][0]) * (points[k][1] - points[i][1]) - (points[j][1] - points[i][1]) * (points[k][0] - points[i][0]) > 0:
                    flag = False
                    break
            if flag:
                edges.append((i, j))
                figure_time += draw_current(points, edges, os.path.join(data_path, f"{i}.png"))
    return time() - start - figure_time


def intriangle(p1, p2, p3, p):
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    return cross_product(p1, p2, p) >= 0 and cross_product(p2, p3, p) >= 0 and cross_product(p3, p1, p) >= 0