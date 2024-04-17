# 对每个算法，绘制算法性能曲线，对比算法。
import matplotlib.pyplot as plt
import imageio
import os
from time import time

def draw_current(points, edges, path):
    start_time = time()
    plt.figure()
    plt.scatter(points[:, 0], points[:, 1], color='blue', label='Points')
    for edge in edges:
        plt.plot([points[edge[0], 0], points[edge[1], 0]], [points[edge[0], 1], points[edge[1], 1]], color='red', label='Edges')
    plt.savefig(path)
    return time() - start_time

def gen_gif(dir, gif_name):
    images = []
    for filename in os.listdir(dir):
        if filename.endswith(".png"):
            images.append(imageio.imread(os.path.join(dir, filename)))
    imageio.mimsave(os.path.join(dir, f'{gif_name}.gif'), images, duration=0.2)


def draw_time(time_recoder, path):
    plt.figure()
    for method in time_recoder:
        plt.plot(range(1000, 10000, 1000), time_recoder[method], label=method)
    plt.legend()
    plt.savefig(path)