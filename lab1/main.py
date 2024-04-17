# 求解凸包问题：输入是平面上 n 个点的集合 Q，凸包问题是要输出一个 Q 的凸包。其中，Q 的凸包是一个凸多边形 P，Q 中的点或者在 P 上或者在 P 中。
import os

from data_generation import generate_data
from draw_figure import draw_current, gen_gif, draw_time
from divide_conquer import divide_conquer
from enumeration import enumeration
from graham_scan import graham_scan

METHODS = {
    # "DC": divide_conquer,
    "ENUM": enumeration,
    # "GS": graham_scan
}
DATA_DIR = "./lab1/results"

def run(data_num):
    time_dict = {}
    # 生成数据
    data = generate_data(data_num)

    for method in METHODS:
        # 生成数据文件夹
        data_path = os.path.join(DATA_DIR, method)
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        # 运行算法
        time = METHODS[method](data, data_path)
        time_dict[method] = time
    # 生成动图
    gen_gif(data_path, "convex_hull.gif")
    return time_dict

def main():
    time_recoder = {"DC": [], "ENUM": [], "GS": []}
    for i in range(1000, 10000, 1000):
        time_dict = run(i)
        for method in time_dict:
            time_recoder[method].append(time_dict[method])
    
    draw_time(time_recoder, os.path.join(DATA_DIR, "time.png"))
        
    


if __name__ == "__main__":
    main()   