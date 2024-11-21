from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # edge case
        if not s or not t:
            return False

        char_map = {}

        # build map 
        for i, j in zip(s, t):
            if i not in char_map and j not in char_map.values():
                char_map[i] = j
                
        for i, j in zip(s, t):
            
            try:
                if char_map[i] == j:
                    continue
            except KeyError:
                return False
                
            else:
                return False

        return True

s = "egg"
t = "add"

sol = Solution()
print(sol.isIsomorphic(s, t))

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

s = "badc"
t = "baba"
False


 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""