class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        myset = set()
        for i in nums:
            myset.add(i)
        max_streak = 0
        for num in myset:
            if num - 1 in myset:
                continue
            else:
                number = num
                streak = 1
                while (number + 1) in myset:
                    streak += 1
                    number += 1
                max_streak = max(max_streak, streak)
        return max_streak