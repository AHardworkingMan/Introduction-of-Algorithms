# @Frame : 
# @Time : 2023-06-03 15:05
# @Author : Gu zhihao
# @platform : Pycharm
# @description :

# 各活动的起始时间和结束时间存储于数组s和f中，且按结束时间的非减序排列
if __name__ == "__main__":
    n = 11
    s = [0,1,3,0,5,3,5,6,8,8,2,12]
    f = [0,4,5,6,7,9,9,10,11,12,14,16]
    A = [False,False,False,False,False,False,False,False,False,False,False,False,False]
    A[1] = True
    j=1
    for i in range(2,n+1):
        if s[i]>=f[j]:
            A[i] = True
            j=i
        else:
            A[i] = False
    print('安排的活动：',end=' ')
    for i in range(len(A)):
        if A[i]==True:
            print(i,end=' ')