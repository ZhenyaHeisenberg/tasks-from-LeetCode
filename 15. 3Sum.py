class Solution:
    def threeSum():
        
        nums = [1, -2, 1]
        
        
        nums.sort()
        result = set()
        
        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    result.add((nums[i], complement, nums[j]))
                seen.add(nums[j]) # добавляем элемент, который уже не попадет в i или j 
                """"""
        
        return [list(triplet) for triplet in result]

    print(threeSum())
