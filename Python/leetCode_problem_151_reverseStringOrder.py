from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        
        strs_straight = []
        strs_reverse = []
        curr_word = ""
        n = len(strs_straight)

        for curr_str in s:
            if curr_str == " " and curr_word != "":
                strs_straight.append(curr_word)
                curr_word = ""
            
            elif curr_str != " ":
                curr_word += curr_str

        if curr_word:
            strs_straight.append(curr_word)

        for strs in reversed(strs_straight):
            print(strs)
            strs_reverse.append(strs)

        return " ".join(strs_reverse)

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()
        res = []

        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
            if i != 0:
                res.append(" ")

        return "".join(res)
"""

s = "the sky is blue"
sol = Solution()
print(sol.reverseWords(s))

"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""