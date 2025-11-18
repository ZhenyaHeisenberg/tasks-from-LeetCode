class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            s[nums[i]] = i

        for j in range(len(nums)):
            search = target-nums[j]
            if search in s and s[search] != j:

                return [j, s[search]]