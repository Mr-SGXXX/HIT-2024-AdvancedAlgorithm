# 对每个算法，绘制算法性能曲线，对比算法。
import matplotlib.pyplot as plt
import imageio
import os
from time import time

def draw_current(points, edges, path):
    start_time = time()
    plt.figure()
    plt.scatter(points[:, 0], points[:, 1], color='blue', label='Points', s=10)
    for edge in edges:
        plt.plot([points[edge[0], 0], points[edge[1], 0]], [points[edge[0], 1], points[edge[1], 1]], color='red', label='Edges')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(path)
    return time() - start_time

def gen_gif(dir, gif_name):
    images = []
    for filename in sorted(os.listdir(dir), key=lambda x: (0, int(x.split(".")[0])) if x.split(".")[0].isdigit() else (1, x)):
        if filename.endswith(".png"):
            images.append(imageio.imread(os.path.join(dir, filename)))
        if filename.split(".")[0].isdigit():
            os.remove(os.path.join(dir, filename))
    imageio.mimsave(os.path.join(dir, f'{gif_name}'), images, duration=10 / len(images) if len(images) > 50 else 0.2)


def draw_time(time_recoder, ran, dir):
    for method in time_recoder:
        plt.figure()
        plt.plot(ran, time_recoder[method], label=method)
        plt.xlabel("Data size")
        plt.ylabel("Time (s)")
        plt.title("Performance of different algorithms")
        plt.legend()
        plt.savefig(os.path.join(dir, f"{method}.png"))