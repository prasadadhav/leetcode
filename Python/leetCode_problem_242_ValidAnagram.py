from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # edge case
        if not s or not t:
            return False

        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for s_i in s:
            s_map[s_i] = s_map.get(s_i, 0) + 1

        for t_i in t:
            t_map[t_i] = t_map.get(t_i, 0) + 1

        print(s_map, t_map)

        for s_i in s:
            
            try:
                if s_map[s_i] == t_map[s_i]:
                    continue
            except KeyError:
                return False

            else: return False

        return True

s = "anagram" 
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))

"""
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""