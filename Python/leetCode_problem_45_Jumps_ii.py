def jump(nums) -> int:
        
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):  # Only need to go up to n - 2
            farthest = max(farthest, i + nums[i])
            
            # When we reach the end of the range for the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early exit if we can reach the last index
                if current_end >= n - 1:
                    break
        
        return jumps
    
    
nums = [2,3,1,1,4]

print(jump(nums))

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""