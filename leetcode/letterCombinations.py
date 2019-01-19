# coding:utf-8 
'''
created on 2019/1/19

@author:sunyihuan
'''


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    index = {"2": ["a", "b", "c"], "3": ["e", "f", "d"], "4": ["h", "i", "g"], "5": ["k", "l", "j"],
             "6": ["n", "m", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

    def dfs(num, string, res):
        if num == length:
            res.append(string)
            return res
        for letter in index[digits[num]]:
            dfs(num + 1, string + letter, res)

    res = []
    length = len(digits)
    if length == 0:
        return res
    else:
        dfs(0, '', res)

    return res


print(letterCombinations(""))
