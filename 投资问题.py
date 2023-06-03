# @Frame : 
# @Time : 2023-06-03 14:29
# @Author : Gu zhihao
# @platform : Pycharm
# @description :

"""
暴力解决：
对所有项目进行循环，通过限定条件：总投资金额=y，得到所有符合的答案，从中选取最大值，即为所求
"""
def baoli():
    profitMatrix = [[0, 11, 12, 13, 14, 15],
                    [0, 0, 5, 10, 15, 20],
                    [0, 2, 10, 30, 32, 40],
                    [0, 20, 21, 22, 23, 24]]
    a = [0, 0, 0, 0]  # 存放最优投资方案
    maxProfit = 0
    sumMoney = 0
    for x1 in range(6):
        for x2 in range(6):
            for x3 in range(6):
                for x4 in range(6):
                    x = x1 + x2 + x3 + x4
                    if x == 5:
                        sumMoney = profitMatrix[0][x1] + profitMatrix[1][x2] + profitMatrix[2][x3] + profitMatrix[3][x4]
                    if sumMoney > maxProfit:
                        maxProfit = sumMoney
                        a[0] = x1
                        a[1] = x2
                        a[2] = x3
                        a[3] = x4
    print("最大利润为：" + str(maxProfit))
    print("最优投资方案为：" + str(a))


def getProfit(profitMatrix, outspace, maxProfit):
    """
    假设第x个项目投资m万元，则将x个项目的y万元投资问题分解为前x-1个项目投资y-m万元和第x个项目投资m万元。
    这样就可以将问题规模减小，直至仅有一个项目，此时的最佳投资方案就是其本身。
    令outspace[x][y]表示前x个项目投资y万元得到的最大利润，令
    profitMatrix[i][m]=fi(m)，则动态方程为：
    outspace[x][y]=profitMatrix[x][m]+outspace[x-1][y-m]
    限定边界为outspace[0][k]=profitMatrix[0][k]
    """
    for i in range(6):
        outspace[0][i] = profitMatrix[0][i]
    for i in range(1, 4):
        for j in range(6):
            for m in range(j + 1):
                if outspace[i][j] < profitMatrix[i][m] + outspace[i - 1][j - m]:
                    outspace[i][j] = profitMatrix[i][m] + outspace[i - 1][j - m]
                if maxProfit < outspace[i][j]:
                    maxProfit = outspace[i][j]
    return maxProfit


if __name__ == '__main__':
    baoli()

    profitMatrix = [[0, 11, 12, 13, 14, 15],
                    [0, 0, 5, 10, 15, 20],
                    [0, 2, 10, 30, 32, 40],
                    [0, 20, 21, 22, 23, 24]]
    outspace = []
    for i in range(4):
        outspace.append([])
        for j in range(6):
            outspace[i].append(0)
    maxProfit = 0
    a = getProfit(profitMatrix, outspace, maxProfit)
    print("最大利润为：" + str(a))
