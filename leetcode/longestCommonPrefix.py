# coding:utf-8 
'''
created on 2019/1/16

@author:sunyihuan
'''


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    common = strs[0]
    for string in strs[1:]:
        while string.find(common) != 0:
            common = common[:-1]
            if common == '':
                return ''
    return common


print(longestCommonPrefix(["a"]))
