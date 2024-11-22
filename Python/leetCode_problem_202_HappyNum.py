from typing import List

class Solution:
    def isHappy(self, n: int) -> bool:

        num_list = str(n)
        
        curr_list = []
        lookup_map = {}
        sq_sum = 0

        while True:

            for n in num_list:
                sq_sum += int(n) * int(n)

            print(sq_sum)
            num_list = str(sq_sum)

            if sq_sum == 1:
                return True
            else:
                lookup_map[sq_sum] = lookup_map.get(sq_sum, 0) + 1
                if lookup_map[sq_sum] > 1:
                    return False
                else:
                    sq_sum = 0

        return False


n = 19
sol = Solution()
print(sol.isHappy(n))

"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""
