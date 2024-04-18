# 求解凸包问题：输入是平面上 n 个点的集合 Q，凸包问题是要输出一个 Q 的凸包。其中，Q 的凸包是一个凸多边形 P，Q 中的点或者在 P 上或者在 P 中。
import os
import shutil

from data_generation import generate_data
from draw_figure import draw_current, gen_gif, draw_time
from divide_conquer import divide_conquer
from enumeration import enumeration
from graham_scan import graham_scan

METHODS = {
    "DC": divide_conquer,
    "ENUM": enumeration,
    "GS": graham_scan
}
DATA_DIR = "./lab1/results"

def run(data_num):
    time_dict = {}
    # 生成数据
    data = generate_data(data_num)
    for method in METHODS:
        # 生成数据文件夹
        data_path = os.path.join(DATA_DIR, f"{data_num}", method)
        os.makedirs(data_path)
            
        # 运行算法
        time = METHODS[method](data, data_path,True if data_num == 1000 else False)
        time_dict[method] = time
        # 生成动图
        gen_gif(data_path, "convex_hull.gif")
    return time_dict

def main():
    shutil.rmtree(DATA_DIR, ignore_errors=True)
    time_recoder = {}
    for method in METHODS:
        time_recoder[method] = []
    ran = range(1000, 11000, 1000)
    for i in ran:
        time_dict = run(i)
        for method in time_dict:
            time_recoder[method].append(time_dict[method])
    
    draw_time(time_recoder, ran, DATA_DIR)
        
    


if __name__ == "__main__":
    main()   