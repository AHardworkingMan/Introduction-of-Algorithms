# @Frame : 
# @Time : 2023-06-02 21:33
# @Author : Gu zhihao
# @platform : Pycharm
# @description :
cl = 0
bestl = 1000

n=5
g = [[0,0,0,0,0,0],
     [0,-1,10,-1,4,12],
     [0,10,-1,15,8,5],
     [0,-1,15,-1,7,30],
     [0,4,8,7,-1,6],
     [0,12,5,30,6,-1]]
x = [0,0,0,0,0,0]
bestx = [0,0,0,0,0,0]
for i in range(n+1):
    if i>0:
        x[i]=i
        bestx[i]=0;


def travel(t, cl, bestl, bestx,n):
    if t>n:
        if g[x[n]][1] != -1 and (cl + g[x[n]][1] < bestl):
            # 推销员到的最后一个城市与出发的城市之间有路径，且当前总距离比当前最优值小
            for j in range(n+1):
                if j>=1:
                    bestx[j] = x[j]
            bestl = cl + g[x[n]][1]
    else:
        for j in range(t,n+1):
            if g[x[t-1]][x[j]]!=-1 and (cl+g[x[t-1]][x[j]]<bestl):
                x[t], x[j] = x[j], x[t]
                cl += g[x[t - 1]][x[t]]
                bestx,bestl = travel(t + 1,cl,bestl,bestx,n)
                cl -= g[x[t - 1]][x[t]]
                x[t], x[j] = x[j], x[t]
    return bestx,bestl


bestx, bestl = travel(2,cl,bestl,bestx,n)
print("城市路线：")
for i in range(n+1):
    if i>0:
        print(bestx[i],end=' ')
print(bestx[1])
print("最短路线长度：")
print(bestl)

