import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
from time import time 

def draw_bar_chart(y, path):
    start_time = time()
    x = np.arange(len(y))
    plt.figure()
    plt.bar(x, y, width=1.0, color='blue')
    plt.xlim(0, len(y))
    plt.ylim(0, max(y) + 1)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Sort State")
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
    
def draw_step(step_list, figure_path):
    plt.figure()
    plt.plot(range(11), step_list)
    plt.xlabel("Repeated percentage") 
    plt.ylabel("Steps")
    plt.title("Performance Of Different Repeated Percentage")
    plt.savefig(figure_path)


def draw_time(time_list, figure_path):
    plt.figure()
    plt.plot(range(11), time_list)
    plt.xlabel("Repeated percentage")
    plt.ylabel("Time (s)")
    plt.title("Time Performance Of Different Repeated Percentage")
    plt.savefig(figure_path)