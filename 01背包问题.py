# @Frame : 
# @Time : 2023-06-02 18:18
# @Author : Gu zhihao
# @platform : Pycharm
# @description :
"""
伪代码：
void search(层数)
{
If(搜索到最底层)
打印出结果解;
else
   for(遍历当前层解)
       {
            If(合适解)继续搜索;
            撤消当前状态的影响; //回溯
       }
}
"""

def search(cur, cur_v, cur_w, bag_v, bag):
    """

    :param cur:
    :param cur_v: 当前节点的价值
    :param cur_w: 当前节点的质量
    :return:
    """
    bag_w = 8 #背包最大容量:8
    n = 5 #物品个数
    w = [4,5,2,1,6] # 物品的重量
    val = [4500,5700,2250,1100,6700]
    if cur>=n:
        if cur_v>bag_v:
            bag_v = cur_v
            for i in range(n):
                bag[i]=x[i] # x表示当前是否被选中，将选中的物品存入bag中
        return bag_v,bag
    else:
        for j in range(2):
            x[cur]=j
            if cur_w + x[cur] * w[cur] <= bag_w:
                cur_w+=w[cur]*x[cur]
                cur_v += val[cur] * x[cur]
                bag_v,bag = search(cur + 1, cur_v, cur_w, bag_v, bag) #递归，下一件物品
                #清楚痕迹，回溯上一层
                cur_w -= w[cur] * x[cur]
                cur_v -= val[cur] * x[cur]
                x[cur] = 0
        return bag_v,bag

if __name__ == "__main__":
    bag = [0, 0, 0, 0, 0]
    x = [0, 0, 0, 0, 0]
    w = [0, 0, 0, 0, 0]
    val = [0, 0, 0, 0, 0]
    bag_v = 0
    bag_v, bag = search(1,0,0,0,bag)
    print('最大价值:',bag_v)
    print('选中物品:',end=' ')
    for i in range(len(bag)):
        if bag[i]==1:
            print(i+1,end=' ')
