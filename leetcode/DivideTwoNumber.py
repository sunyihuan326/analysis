# coding:utf-8 
'''
created on 2019/3/20

@author:sunyihuan
'''


class Solution:
    def divide(self, dividend, divisor):
        if dividend == 0 and dividend < divisor:
            return 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            quotient = "-"
        else:
            quotient = ""
        dividend, divisor = abs(dividend), abs(divisor)
        dividend = str(dividend)
        i = 0
        remainder = ""
        while i < len(dividend):
            remainder = int(str(remainder) + dividend[i])
            quot = 0
            while remainder >= divisor:
                remainder -= divisor
                quot += 1
            quotient += str(quot)
            i += 1
        if int(quotient) > 2147483647:
            return 2147483647
        elif int(quotient) < -2147483648:
            return 2147483648
        else:
            return int(quotient)


class Solution1:
    def divide(self, dividend, divisor):
        if dividend == 0 and dividend < divisor:
            return 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            quotient = "-"
        else:
            quotient = ""
        dividend, divisor = abs(dividend), abs(divisor)
        rem = dividend
        c = 0
        while rem >= divisor:
            print("c", c)
            rem -= divisor
            c = c + 1
        quotient += str(c)
        if int(quotient) > 2147483647:
            return 2147483647
        elif int(quotient) < -2147483648:
            return 2147483648
        else:
            return int(quotient)


s = Solution()
print(s.divide(1000, -3))
