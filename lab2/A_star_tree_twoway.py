from map import Map, INT_MAX
import numpy as np
import heapq


class Node:
    def __init__(self, point, g=0, f=0, start_tree=True):
        self.point = point
        self.g = g
        self.f = f
        self.children = []
        self.parent = None
        self.start_tree = start_tree
        
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
        
    def top(self):
        return self.heap[0]
    
    def push(self, node:Node):
        heapq.heappush(self.heap, node)
        
    def pop(self) -> Node:
        return heapq.heappop(self.heap)


class A_star_tree_twoway:
    def __init__(self, map:Map):
        root1_point = map.start_point
        root2_point = map.end_point
        self.point2node1 = {}
        self.point2node2 = {}
        self.passed_mat1 = np.zeros(map.shape, dtype=bool)
        self.passed_mat2 = np.zeros(map.shape, dtype=bool)
        self.map = map
        self.root1 = Node(root1_point, 0)
        self.root2 = Node(root2_point, 0, start_tree=False)
        self.point2node1[root1_point] = self.root1
        self.point2node2[root2_point] = self.root2
        self.passed_mat1[root1_point[1]][root1_point[0]] = True
        self.passed_mat2[root2_point[1]][root2_point[0]] = True
        self.heap1 = MinHeap()
        self.heap2 = MinHeap()
        self.heap1.push(self.root1)
        self.heap2.push(self.root2)
    
        
    def find_path(self):
        meet_flag = False
        node1 = self.heap1.top()
        node2 = self.heap2.top()
        node = self.get_min_cost_node()
        while not meet_flag:
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
                    g = node.g + path_cost + self.map.block_cost(x, y) if node.start_tree else node.g + path_cost + self.map.block_cost(node.point[0], node.point[1])
                    if node.start_tree:
                        if self.passed_mat1[y][x] and g >= self.point2node1[(x, y)].g:
                            continue
                        if (x, y) in self.point2node2:
                            meet_flag = True
                            node1 = self.add_node((x, y), node, g, f)
                            node2 = self.point2node2[(x, y)]
                            break
                    else:
                        if self.passed_mat2[y][x] and g >= self.point2node2[(x, y)].g:
                            continue
                        if (x, y) in self.point2node1:
                            meet_flag = True
                            node2 = self.add_node((x, y), node, g, f)
                            node1 = self.point2node1[(x, y)]
                            break
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
                            the_other_node = node2 if node.start_tree else node1
                            h = min(h, np.sqrt((node1.point[0]- the_other_node.point[0])**2 + (node1.point[1] - the_other_node.point[1])**2))
                            # h = min(h, path_cost + np.sqrt((node1.point[0]- node2.point[0])**2 + (node1.point[1] - node2.point[1])**2))
                    f = g + h
                    new_node = self.add_node((x, y), node, g, f)
                    if node.start_tree:
                        self.point2node1[(x, y)] = new_node
                        self.passed_mat1[y][x] = True
                    else:
                        self.point2node2[(x, y)] = new_node
                        self.passed_mat2[y][x] = True
                    child_nodes.append(new_node)
            for child in child_nodes:
                self.heap1.push(child) if node.start_tree else self.heap2.push(child)
            print(f"current node: {node.point}, G: {node.g}, F: {node.f}")
            if not meet_flag:
                node1 = self.heap1.top()
                node2 = self.heap2.top()
                node = self.get_min_cost_node()
                # if node.start_tree:
                #     node1 = node
                # else:
                #     node2 = node
        self.get_path(node1, node2)
        return node1.g + node2.g
    
    def get_path(self, node1, node2):
        path1 = []
        path2 = []
        while node1:
            if node1.point != self.map.start_point:
                path1.insert(0, node1.point)
            node1 = node1.parent
        while node2:
            if node2.point != self.map.end_point and node2.point != node1:
                path2.insert(0, node2.point)
            node2 = node2.parent
        for point in path1:
            self.map.path.append(point)
            self.map.draw_map()
        for point in path2:
            self.map.path2.append(point)
            self.map.draw_map()
            

    def get_min_cost_node(self) -> Node:
        if self.heap1.top() < self.heap2.top():
            return self.heap1.pop()
        else:
            return self.heap2.pop()
    
    def add_node(self, point, parent, g, f):
        node = Node(point, g, f, start_tree=parent.start_tree)
        parent.add_child(node)
        return node
