#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/18 11:04
# @Author  : ywendeng
# @Description : 并查集路径压缩算法实现
# 算法描述参考:http://blog.csdn.net/dellaserss/article/details/7724401/

# 定义一个存在和自己关联的数组
import random


def find(pre, x):
    r = x
    while pre[r] != r:
        # r 变成和自己相连接的值,如果pre[r]==r 则表示自己已经是终点
        r = pre[r]
    # 如果每次都需要从叶子节点到根节点的遍历则需要花费大量的时间,则使用路径压缩来进行优化
    i = x
    while pre[i] != r:
        # 使用j 来记录器其上一个节点
        j = pre[i]
        # 将其上一个节点直接修改为根节点----压缩自己的路径
        pre[i] = r
        # 压缩其上级的路径
        i = j
    # 直接返回其上级
    return r


def union(pre, x, y):
    # 分别找到其所在树的根节点
    x1 = find(pre, x)
    y1 = find(pre, y)
    # 如果两个根节点不在同一棵树中,则将两棵树联结在一起
    if x1 != y1:
        pre[x1] = y1
        return True
    else:
        return False


# **********************实践应用——查找城镇之间最少还需要修建多少条路****************
def check_build_road(n, m):
    # 总共需要修建n-1条路
    total = n - 1
    pre = []
    # 假设n个城市中一开始相互独立的
    for i in range(n):
        pre.append(i)
    # 随机产生m条路
    road = [(random.randint(0, n - 1), random.randint(0, n - 1)) for j in range(m)]
    for k, r in road:
        # 查找两条路是否相连
        if union(pre, k, r):
            total -= 1
            # 如果两点已经连通了,那么这条路只是在图上增加了一个环,对连通性没有任何影响，无视掉
    return total


if __name__ == '__main__':
    # 查询出需要修建的道路数
    road_num = check_build_road(10, 3)
    print road_num
