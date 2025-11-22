class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        answer = set()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # если i совпадает с i-1 - не проверяем
                continue
                
            s = set()
            for j in range(i + 1, len(nums)):

            
                third = -nums[i] - nums[j]
                if third in s:
                    answer.add((nums[i], third, nums[j]))
                s.add(nums[j])
        
        return [list(x) for x in answer]