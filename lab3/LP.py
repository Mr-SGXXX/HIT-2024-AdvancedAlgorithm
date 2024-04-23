import pulp
import logging

def LP(F, x):
    logging.basicConfig(level=logging.ERROR)
    # 创建一个线性规划问题实例，目标是最小化
    
    # 禁止PuLP输出除错误信息外的其他日志信息
    pulp.LpSolverDefault.msg = 0
    prob = pulp.LpProblem("SetCover", pulp.LpMinimize)
    
    # 定义决策变量
    vars = pulp.LpVariable.dicts("Select", range(len(F)), 0, 1, pulp.LpBinary)
    
    # 添加约束条件：宇宙集合中的每个元素至少被一个子集覆盖
    for element in x:
        prob += sum(vars[i] for i, subset in enumerate(F) if element in subset) >= 1
    
    # 定义目标函数：最小化选择的子集的总数
    prob += sum(vars[i] for i in range(len(F)))
    
    # 求解问题
    prob.solve()
    
    # 输出结果
    selected_subsets = [i for i in range(len(F)) if vars[i].varValue == 1]
    return selected_subsets