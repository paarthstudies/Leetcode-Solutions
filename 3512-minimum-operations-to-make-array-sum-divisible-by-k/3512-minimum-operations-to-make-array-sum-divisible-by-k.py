class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for i in nums:
            res += i
        if res % k == 0:
            return 0
        else:
            return res % k
        
        