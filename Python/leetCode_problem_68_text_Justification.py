from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        lines = []
        current_line = []
        current_length = 0

        # Step 1: Create the lines
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                # If the current line exceeds the maxWidth, we justify the line
                lines.append(self.justify(current_line, maxWidth, False))
                # Reset for the next line
                current_line = [word]
                current_length = len(word)
            else:
                # Add the word to the current line
                current_line.append(word)
                current_length += len(word)

        # Last line, should be left-justified
        lines.append(self.justify(current_line, maxWidth, True))

        return lines

    def justify(self, line, maxWidth, is_last_line):
        if is_last_line:
            # For the last line, we just join the words with a single space
            return " ".join(line).ljust(maxWidth)
        else:
            # Calculate total spaces we need to distribute
            total_spaces = maxWidth - sum(len(word) for word in line)
            num_slots = len(line) - 1  # spaces between words

            if num_slots > 0:
                # Space between each word
                even_space = total_spaces // num_slots
                extra_space = total_spaces % num_slots

                # Create the justified line
                result = line[0]
                for i in range(1, len(line)):
                    # Add the even space and any extra space to the leftmost positions
                    space_to_add = even_space + (1 if i <= extra_space else 0)
                    result += " " * space_to_add + line[i]
                return result
            else:
                # If there is only one word in the line, just pad the rest with spaces
                return line[0] + " " * total_spaces

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
sol = Solution()

print(sol.fullJustify(words, maxWidth))

"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth

"""