from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # edge case
        if not s or not pattern:
            return False

        words = s.split()

        if len(pattern) != len(words):
            return False
        
        word_map = {}

        # build the map
        for pat, word in zip(pattern, words):

            if (pat not in word_map and 
            word not in word_map.values()):
                word_map[pat] = word

        for pat, word in zip(pattern, words):

            try:
                if word_map[pat] == word:
                    continue
            except KeyError:
                return False

            else:
                return False

        return True

pattern = "abba"
s = "dog cat cat dog"

sol = Solution()
print(sol.wordPattern(pattern, s))

"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

pattern = "aaa"
s = "aa aa aa aa"

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""