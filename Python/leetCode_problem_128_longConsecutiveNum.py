from typing import List

# my Solution

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0

        if len(nums) == 1: return 1

        nums = list(set(nums))
        nums.sort()
        print(nums)

        L = 0
        cons = 1
        cons_max = [nums[0]]

        for R in range(len(nums)):

            if (R != len(nums) - 1) and nums[R + 1] - nums[R] == 1:
                
                cons_max.append(nums[R + 1])
                cons = max(len(cons_max), cons)

            else:
                L = R 
                cons_max = [nums[R]]


        return cons


sol = Solution()

nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109


nums =
[1,2,0,1]

nums =
[0]

"""
