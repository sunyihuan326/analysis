# coding:utf-8 
'''
created on 2019/1/4

@author:sunyihuan
'''


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s

    row = 0
    step = 1
    outp = [""] * numRows
    for c in s:
        if row == 0:
            step = 1
        if row == numRows - 1:
            step = -1
        outp[row] += c
        row += step
    outputStr = ""
    for j in range(numRows):
        outputStr += outp[j]
    return outputStr


s = "pahdwksjs"
numRows = 4
print(convert(s, numRows))
