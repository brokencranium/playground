# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
# (similar to C/C++'s atoi function).
#
# The function first discards as many whitespace characters as necessary until the first
# non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed
# by as many numerical digits as possible,
# and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the
# 32-bit signed integer range: [−231,  231 − 1].
# If the numerical value is out of the range of representable values,
# INT_MAX (231 − 1) or INT_MIN (−231) is returned.

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        res = 0
        for i in range(len(s)):
            if s[i] not in '0123456789':
                break
            res = res * 10 + int(s[i])
        res = sign * res
        if res > 2**31 - 1:
            return 2**31 - 1
        if res < -2**31:
            return -2**31
        return res




