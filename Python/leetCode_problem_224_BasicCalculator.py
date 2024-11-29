from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_res,curr_num = 0, 0
        sign = 1
        for i in range(len(s)):

            char = s[i]

            if char.isdigit():
                curr_num = curr_num*10+int(char)

            elif char == '+' or char == '-':
                curr_res += curr_num*sign
                sign = 1 if char == '+' else -1
                curr_num = 0

            elif char == '(':
                stack.append((curr_res, sign))
                curr_res = 0
                sign = 1

            elif char == ')':
                curr_res+=sign*curr_num
                prev, p_sign = stack.pop()
                curr_res = prev+curr_res*p_sign
                curr_num = 0

        curr_res += curr_num*sign
        return curr_res

s = "(1+(4+5+2)-3)+(6+8)"
sol = Solution()
print(sol.calculate(s))

"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""