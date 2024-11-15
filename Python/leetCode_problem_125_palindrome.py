from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s == " ": return True

        clean_text = ''.join(char for char in s if char.isalnum())
        clean_text = clean_text.lower()

        str_len = len(clean_text)
        n = len(clean_text) // 2

        for i in range(n):
            if clean_text[i] == clean_text[str_len - 1]:
                str_len -= 1
                continue
            else:
                return False

        return True
    
s = "A man, a plan, a canal: Panama"

sol = Solution()
print(sol.isPalindrome(s))

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""