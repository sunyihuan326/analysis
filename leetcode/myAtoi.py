# coding:utf-8 
'''
created on 2019/1/7

@author:sunyihuan
'''


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    if str == "":
        return 0
    else:
        data_str = ""
        str_new = str.lstrip()
        if str_new[0] == "-":
            str_new = str_new[1:]
            a = -1
        else:
            a = 1
            str_new = str_new
        for i in range(len(str_new)):
            if str_new[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "9", "8"]:
                data_str += str_new[i]
            else:
                break
        if data_str == "":
            return 0
        else:
            data_str = int(data_str) * a
            if data_str > 2 ** 31 or data_str < -2 ** 31:
                return 0
            else:
                return data_str


def myAtoi0(str):
    """
    :type str: str
    :rtype: int
    """
    import re
    match = re.search(r"^ *[-+]?[0-9]+", str)
    if match:
        match = int(match.group())
        if match < -2 ** 31:
            return -2 ** 31
        elif match > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return match

    return 0


print(myAtoi0(" 987"))
