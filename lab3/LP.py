import pulp
import numpy as np
import random
from collections import defaultdict

# def LP(F, x):
#     prob = pulp.LpProblem("SetCoverRandomRounding", pulp.LpMinimize)
    
#     # 定义决策变量
#     vars = pulp.LpVariable.dicts("Select", range(len(F)), 0, 1, cat=pulp.LpContinuous)
    
#     # 添加LP约束：确保每个元素至少被覆盖一次
#     for element in x:
#         prob += pulp.lpSum(vars[i] for i, subset in enumerate(F) if element in subset) >= 1
    
#     # 目标函数：最小化选择的子集总数
#     prob += pulp.lpSum(vars[i] for i in range(len(F)))
    
#     # 求解松弛的LP问题
#     prob.solve()

#     # 随机舍入：以变量的LP解为概率进行选择
#     best_cover = None
#     best_set_count = 0
#     best_count = float('inf')
    
#     value = [vars[i].varValue for i in range(len(F))]
#     max_value = np.max(value)
#     trials = 1000000  # 可以调整重复实验的次数
#     for _ in range(trials):
#         selected_subsets = []
#         for i, subset in enumerate(F):
#             if random.random() < value[i]:
#                 selected_subsets.append(i)
        
#         # 检查是否覆盖了所有元素
#         covered_elements = set()
#         for idx in selected_subsets:
#             covered_elements.update(F[idx])
#         set_count = len(covered_elements)

        
#         if set_count >= best_set_count and len(selected_subsets) < best_count:
#             best_set_count = set_count
#             best_cover = selected_subsets
#             best_count = len(selected_subsets)

#     return best_cover

# def LP(F, x):
#     # pulp.LpSolverDefault.msg = 0
#     prob = pulp.LpProblem("SetCover", pulp.LpMinimize)
    
#     # 定义决策变量
#     # 整数规划时的时间代价无法接受，1000个点一晚上也没跑完
#     vars = pulp.LpVariable.dicts("Select", range(len(F)), 0, 1, cat=pulp.LpBinary)
    
#     # 添加约束条件：宇宙集合中的每个元素至少被一个子集覆盖
#     for element in x:
#         prob += pulp.lpSum(vars[i] for i, subset in enumerate(F) if element in subset) >= 1
    
#     # 定义目标函数：最小化选择的子集的总数
#     prob += pulp.lpSum(vars[i] for i in range(len(F)))
    
#     # 求解问题
#     # solver = pulp.GLPK_CMD(path="D:\glpk-4.65\w64\glpsol.exe")
#     # prob.solve(solver)
#     prob.solve()
    
#     # 输出结果
#     selected_subsets = [i for i in range(len(F)) if vars[i].varValue == 1]
#     return selected_subsets

def LP(F, x):            
    # pulp.LpSolverDefault.msg = 0
    prob = pulp.LpProblem("SetCover", pulp.LpMinimize)
    
    # 定义决策变量
    # 整数规划时的时间代价无法接受，1000个点一晚上也没跑完
    vars = pulp.LpVariable.dicts("Select", range(len(F)), 0, 1)
    
    # 添加约束条件：宇宙集合中的每个元素至少被一个子集覆盖
    for element in x:
        prob += pulp.lpSum(vars[i] for i, subset in enumerate(F) if element in subset) >= 1
    
    # 定义目标函数：最小化选择的子集的总数
    prob += pulp.lpSum(vars[i] for i in range(len(F)))
    
    # 求解问题
    # solver = pulp.GLPK_CMD(path="D:\glpk-4.65\w64\glpsol.exe")
    # prob.solve(solver)
    prob.solve()
    # 初始未覆盖元素统计
    found_set = set()
    
    threshold = 0.5
    while len(found_set) != len(x):
        # 输出结果
        selected_subsets = [i for i in range(len(F)) if vars[i].varValue >= threshold]
        for subset_index in selected_subsets:
            for element in F[subset_index]:
                if element not in found_set:
                    found_set.add(element)
        threshold *= 0.99
    # 输出结果
    # selected_subsets = [i for i in range(len(F)) if vars[i].varValue >= threshold]
    return selected_subsets