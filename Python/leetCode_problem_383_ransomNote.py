from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not magazine or len(ransomNote) > len(magazine):
            return False

        # Build a frequency map for magazine
        mag_count = {}
        for char in magazine:
            mag_count[char] = mag_count.get(char, 0) + 1

        # Check if ransomNote can be constructed
        for char in ransomNote:
            if mag_count.get(char, 0) == 0:  # Not enough chars in magazine
                return False
            mag_count[char] -= 1  # Use one instance of the character

        return True


ransomNote = "fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"

sol = Solution()
print(sol.canConstruct(ransomNote, magazine))




"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""