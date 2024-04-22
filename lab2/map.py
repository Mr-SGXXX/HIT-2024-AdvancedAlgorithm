import matplotlib.pyplot as plt
import numpy as np
import os

INT_MAX = 1000000

class Map():
    def __init__(self, shape, start_point, end_point, desert_points=[], river_points=[], obstacle_points=[], rst_dir=None):
        shape = (shape[1], shape[0])
        self.map_array = np.zeros(shape, dtype=int)
        self.shape = shape
        self.start_point = start_point
        self.end_point = end_point
        self.path = []
        self.path2 = []
        self.rst_dir = rst_dir
        self.figure_index = 0
        self.add_desert(desert_points)
        self.add_obstacle(obstacle_points)
        self.add_river(river_points)
        
    def add_desert(self, points):
        for point in points:
            x, y = point
            self.map_array[y][x] = 1
            
    def add_river(self, points):
        for point in points:
            x, y = point
            self.map_array[y][x] = 2
            
    def add_obstacle(self, points):
        for point in points:
            x, y = point
            self.map_array[y][x] = 3
        
    def block_cost(self, x, y):
        cost_map = {0: 0, 1: 4, 2: 2, 3: INT_MAX}
        return cost_map[self.map_array[y][x]]
    
    def draw_map(self):
        # 白色表示普通地形，代价为0，黄色表示沙漠，代价为4，蓝色表示河流，代价为2，灰色表示障碍，无法通行
        color_list = ['white', 'yellow', 'blue', 'grey']
        cmap = plt.cm.colors.ListedColormap(color_list)
        # 设置图形大小
        plt.figure(figsize=(10, 10))

        # 创建网格
        ax = plt.gca()
        ax.imshow(self.map_array, cmap=cmap, interpolation='nearest')
        # 设置每个方块的边框颜色和宽度
        for i in range(len(self.map_array)):
            for j in range(len(self.map_array[0])):
                color = color_list[self.map_array[i, j]]  # 方块边框颜色
                rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, edgecolor=color, facecolor='none')
                ax.add_patch(rect)
        plt.xticks(np.arange(-0.5, len(self.map_array[0])-0.5, 1))
        plt.yticks(np.arange(-0.5, len(self.map_array)-0.5, 1))
        plt.grid(True)

        # 绘制S和T的路径
        for x, y in self.path:
            plt.scatter([x], [y], color='black', s=100, zorder=5)
            # plt.fill_between([x-0.5, x+0.5], y-0.5, y+0.5, color='black')

        for x, y in self.path2:
            plt.scatter([x], [y], color='red', s=100, zorder=5)
        
        # # 绘制S和T点
        # plt.scatter([self.start_point[0]], [self.start_point[1]], color='black', s=100, label='S', zorder=5)
        # plt.scatter([self.end_point[0]], [self.end_point[1]], color='black', s=100, label='T', zorder=5)

        # 在S和T上添加文字标签
        plt.text(self.start_point[0], self.start_point[1], 'S', color='black', ha='center', va='center', fontsize=13)
        plt.text(self.end_point[0], self.end_point[1], 'T', color='black', ha='center', va='center', fontsize=13)
        plt.title("Map State")
        # 隐藏坐标轴的标记
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        rst_path = os.path.join(self.rst_dir, f"{self.figure_index}.png")
        self.figure_index += 1
        plt.savefig(rst_path)