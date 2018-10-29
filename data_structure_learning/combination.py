# coding:utf-8 
'''
created on 2018/10/29

@author:sunyihuan
'''


def force():
    data = "abc"
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if data[i] != data[j] and data[j] != data[k] and data[k] != data[i]:
                    print(data[i], data[j], data[k])

def rank(data, step):
    '''
    递归算法，组合
    :param data: 要组合的字符串
    :param step: 开始的位置
    :return:
    '''
    if len(data) == step + 1:
        print(data)
        return
    else:
        for i in range(step, len(data)):
            print(i)
            data[step], data[i] = data[i], data[step]  # 让当前首位依次为后面的每一个数
            rank(data, step + 1)  # 递归后面的情况
            data[step], data[i] = data[i], data[step]   #确保data换回原来的顺序


def combine(data, step, select_data, target_num):
    if len(select_data) == target_num:  # 选择的元素已经够了，就输出并返回
        print(select_data)
        return
    if step >= len(data):  # 没有元素选了而且还没够，也是直接返回
        return
    select_data.append(data[step])  # 选择当前元素
    combine(data, step + 1, select_data, target_num)
    select_data.pop()  # 别忘了从已选择元素中先删除
    combine(data, step + 1, select_data, target_num)  # 不选择当前元素


if __name__ == '__main__':
    # force()
    data = list("abc")
    # rank(data, 0)
    data = [1, 2, 3, 4, 5, 6]
    combine(data, 0, [], 3)
