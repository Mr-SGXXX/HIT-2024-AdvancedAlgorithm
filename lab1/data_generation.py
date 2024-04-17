# 随机生成正方形(0,0)-(0,100)-(100,100)-(100,0)内的点集合Q

import numpy as np

def generate_data(data_num):
    points = np.random.uniform(low=0, high=100, size=(data_num, 2))

    # 检查并移除重复的点
    unique_points, indices = np.unique(points, axis=0, return_index=True)
    while len(unique_points) < data_num:
        additional_points = np.random.uniform(low=0, high=100, size=(data_num - len(unique_points), 2))
        points = np.vstack((unique_points, additional_points))
        unique_points, indices = np.unique(points, axis=0, return_index=True)
    return unique_points
