# @Frame : 
# @Time : 2023-06-03 14:58
# @Author : Gu zhihao
# @platform : Pycharm
# @description :

statistic = {'100':0, '50':0, '20':0, '10':0, '5':0, '2':0, '1':0}
"""
    GZ\币值 100 50 20 10 5 2 1
    z 252   2   1         1
    w 2686  26  1  1  1 1   1
total 2938  28  2  1  1 1 1 1

"""
bal = [252, 2686]

for i in range(len(bal)):
    tbal = bal[i]
    for val in statistic.keys():
        val = int(val)
        num = int(tbal / val)
        statistic['{}'.format(val)] = statistic['{}'.format(val)] + num
        tbal = tbal - num * val
print(statistic)

