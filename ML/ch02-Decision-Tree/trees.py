# coding=utf-8

import numpy as np

"""计算样本实例的熵"""


def cal_entropy(data):
    entris_num = len(data)
    label_count = {}  # 字典存储每个类别出现的次数
    for vec in data:
        cur_label = vec[-1]
        # 将样本标签提取出来，并计数
        label_count[cur_label] = label_count.get(cur_label, 0) + 1
    entropy = 0.0
    # 对每一个类别，计算样本中取到该类的概率
    # 最后将概率带入，求出熵
    for key in label_count:
        prob = float(label_count[key]) / entris_num
        entropy += prob * np.math.log(prob, 2)
    return -entropy


def created_data():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def split_data(data, axis, value):
    """
    使用传入的axis以及value划分数据集
    axis代表在每个列表中的第X位，value为用来划分的特征值
    """
    new_subset = []
    # 利用循环将不符合value的特征值划分入另一集合
    # 相当于将value单独提取出来（或作为叶节点）
    for vec in data:
        if vec[axis] == value:
            feature_split = vec[:axis]
            feature_split.extend(vec[axis + 1:])
            new_subset.append(feature_split)
    return new_subset


def split_by_entropy(dataset):
    """
    使用熵原则进行数据集划分
    @信息增益:info_gain = old - new
    @最优特征：best_feature
    @类别集合：uniVal
    """
    feature_num = len(dataset[0]) - 1
    ent_old = cal_entropy(dataset)
    best_gain = 0.0
    best_feature = -1
    # ENT_OLD代表划分前集合的熵，ENT_NEW代表划分后的熵
    # best_gain将在迭代每一次特征的时候更新，最终选出最优特征
    for i in range(feature_num):
        feature_list = [x[i] for x in dataset]
        uniVal = set(feature_list)
        ent_new = 0.0
        # 使用set剔除重复项，保留该特征对应的不同取值
        for value in uniVal:
            sub_set = split_data(dataset, i, value)
            prob = len(sub_set) / float(len(dataset))
            # 使用熵计算函数求出划分后的熵值
            ent_new += prob * (0 - cal_entropy(sub_set))

        # 由ent_old - ent_new选出划分对应的最优特征
        Info_gain = ent_old - ent_new
        if (Info_gain > best_gain):
            best_gain = Info_gain
            best_feature = i

    return best_feature


if __name__ == '__main__':
    my_data, labels = created_data()
    print my_data
    print cal_entropy(my_data)
