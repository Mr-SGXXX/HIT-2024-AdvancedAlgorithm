from map import Map, INT_MAX
import numpy as np
import heapq


class Node:
    def __init__(self, point, g=0, f=0):
        self.point = point
        self.g = g
        self.f = f
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        
    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return self.f == other.f

        

class MinHeap:
    def __init__(self):
        self.heap = []
        
        
    def push(self, node:Node):
        heapq.heappush(self.heap, (node.f, node))
        
    def pop(self) -> Node:
        return heapq.heappop(self.heap)[1]


class A_star_tree:
    def __init__(self, map:Map):
        root_point = map.start_point
        self.map = map
        self.point2node = {}
        self.passed_mat = np.zeros(map.shape, dtype=bool)
        self.root = Node(root_point, 0)
        self.point2node[root_point] = self.root
        self.passed_mat[root_point[1]][root_point[0]] = True
        self.heap = MinHeap()
        self.heap.push(self.root)
    
        
    def find_path(self):
        node = self.get_min_cost_node()
        while node.point != self.map.end_point:
            child_nodes = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    x, y = node.point
                    x += i
                    y += j
                    if x < 0 or x >= self.map.shape[1] or y < 0 or y >= self.map.shape[0]:
                        continue
                    if self.map.block_cost(x, y) >= INT_MAX:
                        continue
                    path_cost = np.sqrt(i**2 + j**2)
                    g = node.g + path_cost + self.map.block_cost(x, y)
                    if self.passed_mat[y][x] and g >= self.point2node[(x, y)].g:
                        continue
                    h = INT_MAX
                    for m in range(-1, 2):
                        for n in range(-1, 2):
                            if m == 0 and n == 0:
                                continue
                            x1, y1 = x, y
                            x1 += m
                            y1 += n
                            if x1 < 0 or x1 >= self.map.shape[1] or y1 < 0 or y1 >= self.map.shape[0]:
                                continue
                            if self.map.block_cost(x1, y1) >= INT_MAX:
                                continue
                            path_cost = np.sqrt(m**2 + n**2)
                            h = min(h, np.sqrt((self.map.end_point[0]- x1)**2 + (self.map.end_point[1]-y1)**2))
                    f = g + h
                    new_node = self.add_node((x, y), node, g, f)
                    self.point2node[(x, y)] = new_node
                    child_nodes.append(new_node)
                    self.passed_mat[y][x] = True
            for child in child_nodes:
                self.heap.push(child)
            print(f"current node: {node.point}, G: {node.g}, F: {node.f}")
            node = self.get_min_cost_node()
        self.get_path(node)
        return node.g
    
    def get_path(self, node):
        path = []
        while node:
            if node.point != self.map.start_point and node.point != self.map.end_point:
                path.insert(0, node.point)
            node = node.parent
        for point in path:
            self.map.path.append(point)
            self.map.draw_map()

    def get_min_cost_node(self) -> Node:
        return self.heap.pop()
    
    def add_node(self, point, parent, g, f):
        node = Node(point, g, f)
        parent.add_child(node)
        return node
