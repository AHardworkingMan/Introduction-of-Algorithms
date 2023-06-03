# @Frame : 
# @Time : 2023-06-03 15:26
# @Author : Gu zhihao
# @platform : Pycharm
# @description :

# -*- coding: UTF-8 -*- #
'''
@filename: graph_colouring_problem.py
@author:JIN
@time:2022-11-27
'''
"""
[问题描述]给定无向连通图G和m种不同的颜色，用这些颜色为图G的各顶点着色，每个顶点着一种颜色。
如果有一种着色法使G中每条边的两个顶点着不同颜色，则称这个图是m可着色的。
图的m着色问题是对于给定图G和m种颜色，找出所有不同的着色法。
输入描述：第1行有3个正整数n、k和m，表示给定的图G有n个顶点、k条边、m种颜色，
顶点的编号为1、2、…、n。在接下来的k行中每行有两个正整数u 、v，表示图G的一条边（u 、v）。
输出描述：程序运行结束时将计算出的不同着色方案数输出。如果不能着色，则程序输出-1。
输入样例
5 8 4
1 2
1 3
1 4
2 3
2 4
2 5
3 4
4 5
"""
import numpy as np


def ok(i):  # 遍历和顶点i相连接的所有顶点
    for j in range(1, n + 1):
        # 存在相邻顶点着色相同
        if (G[i][j] == 1 and flag[i] == flag[j]):
            return False
    # 顶点i的所有相邻顶点着色都不同
    return True


def getcolor(i):
    global count
    # i>n说明找到了一个可行的涂色方案
    if (i > n):
        count += 1
        print(f'第{count}个着色方案：{flag[1:n + 1]}')
    else:  # //还没有到叶子节点，需要给当前节点可行的涂色
        for k in range(1, m + 1):  # 子树是一个m叉树
            flag[i] = k  # 给第i个顶点着第k种颜色
            if (ok(i)):  # 当顶点i着色为第k种颜色时候，所有相邻顶点着色都不同时候，可以进入下一个顶点着色
                getcolor(i + 1)
            flag[i] = -1  # 当顶点i当顶点i着色为第k种颜色时候，存在相邻顶点着色相同同时候，还原flag初始，并且尝试下一个k种颜色


if __name__ == '__main__':
    a = list(map(int, input("输入图G的顶点数、边数、颜色数").split()))
    n = a[0]  # 图G有n个顶点
    k = a[1]  # k条边
    m = a[2]  # m种颜色
    count = 0  # 记录总着色方案
    flag = [-1 for i in range(n + 1)]  # flag代表顶点i的着色
    flag[0] = 0  # 0为虚点,
    G = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(1, k + 1):
        print(f"第{i}条边是如下两个顶点构成", end=' ')
        b = list(map(int, input().split()))  # b[0]为行，b[1]为列
        G[b[0]][b[1]] = 1
        G[b[1]][b[0]] = 1
    print("输出G图为:", np.array(G))  # G图用矩阵表示 两顶点之间有连线的记作1，两顶点之间无连线记为0
    getcolor(1)
    if count > 0:
        print(f"共{count}种着色方案")
    else:
        print(-1)