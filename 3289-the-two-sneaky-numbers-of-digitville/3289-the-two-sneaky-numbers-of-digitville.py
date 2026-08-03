# from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq =  [0] * (len(nums))
        ans = []
        for x in nums:
            freq[x] += 1
            if freq[x] == 2:
                ans.append(x)
        return ans