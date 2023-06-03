# @Frame : 
# @Time : 2023-06-02 17:16
# @Author : Gu zhihao
# @platform : Pycharm
# @description :
"""
规律如下：
a[i]==b[j]----->c[i][j]=c[i-1][j-1]+1
a[i]!=b[j]----->c[i][j]=MAX(c[i-1][j],c[i][j-1])
"""

a = [1, 3, 4, 5, 6, 7, 7, 8]
b = [3, 5, 7, 4, 8, 6, 7, 8, 2]
# a = ['d','b','c','b','a','d','b']
# b = ['b','a','c','d','b','d']
c = []
tmp = []
for i in range(len(a) + 1):
    for j in range(len(b) + 1):
        if i == 0 or j == 0:
            tmp.append(0)
        else:
            if a[i-1] == b[j-1]:
                tmp.append(c[i - 1][j - 1] + 1)
            else:
                tmp.append(max(tmp[-1], c[i - 1][j]))
    c.append(tmp)
    tmp = []

print('\t\t表如下，最长公共子序列长度为：',max(max(c)))
for i in range(len(a)+3):
    print('\t\t\t',end='')
    for j in range(len(b)+3):
        if i==0:
            if j==0:
                print('\t',end='')
            elif j>=2:
                print(j-2,end=' ')
        elif i==1:
            if j==0:
                print('\t',end='')
            elif j==2:
                print('j',end=' ')
            elif j>2:
                print(b[j-3],end=' ')
        else:
            if j==0:
                print(i-2,end=' ')
            elif j==1:
                if i==2:
                    print('i',end=' ')
                else:
                    print(a[i-3],end=' ')
            else:
                print(c[i-2][j-2],end=' ')
    print('')

