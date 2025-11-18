class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        for i in range(len(nums)):
            new_k = k
            for j in range(i, len(nums)):
                new_k -= nums[j]
                if new_k == 0:
                    count +=1


        return count