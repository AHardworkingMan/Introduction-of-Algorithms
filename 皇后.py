# @Frame : 
# @Time : 2023-06-03 15:21
# @Author : Gu zhihao
# @platform : Pycharm
# @description :


n = 8  # 定义n皇后问题中的n
maxN = n + 5
a = [0 for i in range(1, maxN + 1, 1)]
c = [False for i in range(1, maxN + 1, 1)]
d = [False for i in range(1, 2 * maxN + 1, 1)]
e = [False for i in range(1, 2 * maxN + 1 + 1, 1)]
ans = 0


def Queen(x):
    global n, a, c, d, e, ans
    if x > n:  # 是否得到新结果
        ans += 1
        print(f"第{ans}种解法:")
        for i in range(1, n + 1, 1):
            print(f"第{i}行的皇后放在第{a[i]}列")  # 输出
        print("")
        return
    for j in range(1, n + 1, 1):  # 枚举列数
        if ((not c[j]) and (not d[x - j + n]) and (not e[x + j])):  # 判断与之前的皇后是否冲突
            c[j] = d[x - j + n] = e[x + j] = True
            a[x] = j
            Queen(x + 1)  # 递归,计算下1行
            c[j] = d[x - j + n] = e[x + j] = False
            a[x] = 0


Queen(1)  # 从第1行开始计算
print(f"\n{n}皇后问题共有{ans}种解")  # 输出解法总和
