import os
import imageio

def gen_gif(dir, gif_name):
    images = []
    for filename in sorted(os.listdir(dir), key=lambda x: (0, int(x.split(".")[0])) if x.split(".")[0].isdigit() else (1, x)):
        if filename.endswith(".png"):
            images.append(imageio.imread(os.path.join(dir, filename)))
        if filename.split(".")[0].isdigit():
            os.remove(os.path.join(dir, filename))
    imageio.mimsave(os.path.join(dir, f'{gif_name}'), images, duration=10 / len(images) if len(images) > 50 else 0.2)