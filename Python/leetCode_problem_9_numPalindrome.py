from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x_str = str(x)

        x_rev = x_str [::-1]
        print(x_rev)

        if x_str == x_rev:
            return True
        
        else:
            return False

sol = Solution()

"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
