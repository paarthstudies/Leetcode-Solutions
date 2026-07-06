class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in freq and freq[num] < i:
                freq[num] += 1
                if freq[num] == 0:
                    count += 1
                else:
                    count += freq[num]
            else:
                freq[num] = 0
        return count