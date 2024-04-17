# 基于分治思想的凸包求解算法
from time import time
import os

from draw_figure import draw_current

def divide_conquer(points, data_path):
    draw_current(points, [], os.path.join(data_path, "0.png"))
    start = time()
    figure_time = 0
    # 1. 找到最左侧和最右侧的点
    left_point = points[0]
    right_point = points[0]
    for point in points:
        if point[0] < left_point[0]:
            left_point = point
        if point[0] > right_point[0]:
            right_point = point
    # 2. 分治
    def divide(points, left, right):
        if right - left <= 1:
            return [points[left]]
        mid = (left + right) // 2
        left_hull = divide(points, left, mid)
        right_hull = divide(points, mid, right)
        return merge(left_hull, right_hull)
    def merge(left_hull, right_hull):
        left_hull = sorted(left_hull, key=lambda x: x[1], reverse=True)
        right_hull = sorted(right_hull, key=lambda x: x[1])
        left_top = left_hull[0]
        right_top = right_hull[0]
        left_bottom = left_hull[-1]
        right_bottom = right_hull[-1]
        while (left_top[0] - left_bottom[0]) * (right_top[1] - right_bottom[1]) - (left_top[1] - left_bottom[1]) * (right_top[0] - right_bottom[0]) < 0:
            left_top = left_hull.pop(0)
            right_top = right_hull.pop(0)
        while (left_top[0] - left_bottom[0]) * (right_top[1] - right_bottom[1]) - (left_top[1] - left_bottom[1]) * (right_top[0] - right_bottom[0]) > 0:
            left_bottom = left_hull.pop()
            right_bottom = right_hull.pop()
        return left_hull + right_hull
    hull = divide(points, 0, len(points))
    for i in range(len(hull)):
        figure_time += draw_current(points, [(hull[i], hull[(i + 1) % len(hull)])], os.path.join(data_path, f"{i}.png"))
    return time() - start - figure_time
