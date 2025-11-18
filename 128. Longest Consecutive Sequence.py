class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        s = []
        s.append(nums[0])

        max_len = 1

        for i in range(1, len(nums)):
            if s[-1] == nums[i]-1:
                s.append(nums[i])
                
            else:
                max_len = max(max_len, len(s))
                s = []
                s.append(nums[i])
            
        return max(max_len, len(s))