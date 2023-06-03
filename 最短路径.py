# @Frame : 
# @Time : 2023-06-03 14:36
# @Author : Gu zhihao
# @platform : Pycharm
# @description :
import sys


def dijkstra(graph, start):
    # 获取图中节点的数量
    n = len(graph)
    # 初始化 dist 列表，表示从起始节点到每个节点的最短距离
    dist = [sys.maxsize] * n
    # 起始节点到自身的距离为 0
    dist[start] = 0
    # 初始化 visited 列表，表示每个节点是否已经访问过
    visited = [False] * n
    # 初始化 prev 列表，表示每个节点的前驱节点
    prev = [None] * n

    # 循环 n 次，每次找到一个未访问过的距离最小的节点
    for i in range(n):
        min_dist = sys.maxsize
        u = -1
        for j in range(n):
            if not visited[j] and dist[j] < min_dist:
                min_dist = dist[j]
                u = j
        # 标记找到的节点为已访问过
        visited[u] = True

        # 更新从 u 节点出发能够到达的其他节点的最短距离
        for v in range(n):
            if not visited[v] and graph[u][v] and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                prev[v] = u
                print(f'更新: {u} -> {v}, 距离: {dist[v]}')

    # 打印从起始节点到每个节点的最短路径
    for i in range(n):
        if i != start:
            path = []
            j = i
            while j != start:
                path.append(j)
                j = prev[j]
            path.append(start)
            path.reverse()
            print(f'从 {start} 到 {i} 的最短路径: {" -> ".join(map(str, path))}')

    return dist


if __name__ == "__main__":
    graph = [[0, 2, 4, 0, 0, 0],
             [0, 0, 2, 4, 2, 0],
             [0, 0, 0, 0, 3, 0],
             [0, 0, 0, 0, 0, 2],
             [0, 0, 0, 3, 0, 2],
             [0, 0, 0, 0, 0, 0]]
    dots = ["A", "B", "C", "D", "E", "F"]
    dist = dijkstra(graph, 0)
    for i in range(6):
        print("从A点到{}点的最短距离为{}".format(dots[i], dist[i]))

