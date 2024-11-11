from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = max(citations) 
        cite_dict = {i: 0 for i in range(n + 1)}

        h_index = 0
        cumm_paper = 0

        for cites in citations:
            if cites in cite_dict:
                cite_dict[cites] += 1

        print(cite_dict)

        for index, cites in reversed( list( cite_dict.items())):
            cumm_paper += cites
            print("cumm_paper", cumm_paper)
            print("index", index)

            if cumm_paper >= index:
                h_index = index
                return h_index
            
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = len(citations)
        citation_buckets = [0] * (papers + 1)

        for citation in citations:
            citation_buckets[min(citation, papers)] += 1

        cumulative_papers = 0
        for h_index in range(papers, -1, -1):
            cumulative_papers += citation_buckets[h_index]
            if cumulative_papers >= h_index:
                return h_index   
"""

citations = [3,0,6,1,5]
sol = Solution()
print("h_index", sol.hIndex(citations))


"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""