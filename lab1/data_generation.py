# 随机生成正方形(0,0)-(0,100)-(100,100)-(100,0)内的点集合Q

import numpy as np

def generate_data(data_num):
    return np.random.uniform(low=0, high=100, size=(data_num, 2))
