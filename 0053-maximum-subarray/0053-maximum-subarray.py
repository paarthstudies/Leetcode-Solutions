class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        temp = nums[0]
        max_arr = nums[0]
        for i in range(1, len(nums)):
            temp = max(temp + nums[i], nums[i])
            max_arr = max(temp, max_arr)
        return max_arr