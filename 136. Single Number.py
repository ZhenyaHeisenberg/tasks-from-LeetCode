class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = {}
        for i in range(len(nums)):
            if nums[i] in s:
                s[nums[i]] = 2
            else:
                s[nums[i]] = 1

        for key, value in s.items():
            if value == 1:
                return key