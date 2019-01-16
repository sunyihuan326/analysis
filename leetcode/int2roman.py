# coding:utf-8 
'''
created on 2019/1/16

@author:sunyihuan
'''


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    conversions = {0: "", 1: "I", 5: "V", 10: "X", 50: 'L',
                   100: "C", 500: 'D', 1000: "M"}
    place = 1
    roman = ""
    while not num == 0:
        digit = num % 10
        if (digit >= 5 and digit < 9):
            digit = digit - 5
            roman = conversions[5 * place] + digit * conversions[place] + roman
        elif (digit >= 1 and digit < 4):
            roman = digit * conversions[place] + roman
        elif (digit == 4 or digit == 9):
            roman = conversions[place] + conversions[(digit + 1) * place] + roman
        else:
            roman = conversions[(digit) * place] + roman
        num = num // 10
        place = place * 10
    return roman


print(intToRoman(1994))
