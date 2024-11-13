from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # output string
        commStr = ""

        sorted_strs = sorted(strs)
        
        first = sorted_strs[0]
        last = sorted_strs[-1]

        # Loop over the list of strings
        for i in range( min( len(first), len(last) ) ):
            if( first[i] != last[i] ):
                return commStr
            
            commStr += first[i]

        return commStr




        # return o/p string
        return commStr

strs = ["flower","flow","flight"]

sol = Solution()
print(sol.longestCommonPrefix(strs))

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""