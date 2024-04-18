# 基于分治思想的凸包求解算法
from time import time
import os
import numpy as np
from copy import deepcopy

from draw_figure import draw_current


def divide_conquer(points, data_path, draw_flag=False):
    global dp
    global figure
    global edges
    global draw
    start = time()
    draw = draw_flag
    figure = 1
    edges = []
    dp = data_path
    figure_time = draw_current(points, [], os.path.join(data_path, "0.png"))
    # 1. 根据x坐标排序
    points = np.array(sorted(points, key=lambda p: (p[0], p[1])))
    # 2. 分治
    _, div_figure_time = divide(points, 0, len(points))
    figure_time += div_figure_time
    figure_time += draw_current(points, edges, os.path.join(dp, f"final.png"))
    time_cost = time() - start - figure_time
    return time_cost

def divide(points, left, right):
    global figure
    global edges
    global draw
    figure_time = 0
    if right - left == 2:
        edges.append((left, left + 1))
        return [left, left + 1], figure_time 
    if right - left == 3:
        points_with_index = np.array(sorted(enumerate(points[left:right]), key=lambda p: (np.arctan2(p[1][1]-points[left][1], p[1][0]-points[left][0]), np.linalg.norm(p[1]-points[left]))))
        last_index = 0
        for index, _ in points_with_index:
            edges.append((last_index + left, index + left))
            last_index = index
        edges.append((last_index + left, left))
        if draw:
            figure_time = draw_current(points, edges, os.path.join(dp, f"{figure}.png"))
            figure += 1
        return [left, left+1, left+2], figure_time
    mid = (left + right) // 2
    left_points_index, left_time = divide(points, left, mid)
    right_points_index, right_time = divide(points, mid, right)
    # merged_points = left_points_index + right_points_index
    # merge_time = 0
    merged_points, merge_time = merge(points, left_points_index, right_points_index)
    return merged_points, left_time + right_time + merge_time

def merge(points, left_points_index, right_points_index):
    global figure
    global edges
    global draw
    figure_time = 0
    edges = remove_edges_with_points(edges, left_points_index)
    edges = remove_edges_with_points(edges, right_points_index)
    edges_points_index = left_points_index + right_points_index
    merged_points_index = graham_scan(deepcopy(points[edges_points_index]))
    merged_points_index = [edges_points_index[i] for i in merged_points_index]
    edges += [(merged_points_index[i], merged_points_index[i + 1]) for i in range(len(merged_points_index) - 1)] + [(merged_points_index[-1], merged_points_index[0])]
    if draw:
        figure_time = draw_current(points, edges, os.path.join(dp, f"{figure}.png"))
        figure += 1
    return merged_points_index, figure_time

def remove_edges_with_points(edges, points):
    for point in points:
        edges = [edge for edge in edges if point not in edge]
    return edges

def graham_scan(points:np.ndarray):
    global figure
    global dp
    # 1. 找到最下方的点
    min_point = points[points[:, 1].argmin()]
    min_point_index = points[:, 1].argmin()
    point_index = [i for i in range(len(points))]
    point_index.remove(min_point_index)

    # 2. 按照极角排序
    points_with_index = np.array(sorted(zip(point_index, np.delete(points, min_point_index, axis=0)), key=lambda p: np.arctan2(p[1][1]-min_point[1], p[1][0]-min_point[0])))
    point_index = [min_point_index] + [index for index, _ in points_with_index]
    points = np.array([point for _, point in points_with_index])
    points = np.insert(points, 0, min_point, axis=0)
    
    # 3. 扫描
    stack = [0, 1, 2]
    for i in range(3, len(points)):
        while len(stack) > 1 and (points[stack[-1]][0] - points[stack[-2]][0]) * \
            (points[i][1] - points[stack[-2]][1]) - (points[stack[-1]][1] - points[stack[-2]][1]) * (points[i][0] - points[stack[-2]][0]) < 0:
            stack.pop()
        stack.append(i)
    #     draw_current(points, [(stack[i], stack[i + 1]) for i in range(len(stack) - 1)], os.path.join(dp, f"gc_{i}.png"))
    # draw_current(points, [(stack[i], stack[i + 1]) for i in range(len(stack) - 1)] + [(stack[-1], 0)], os.path.join(dp, f"gc_final.png"))
    
    stack = [point_index[i] for i in stack]
    return stack