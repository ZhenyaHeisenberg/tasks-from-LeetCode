class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = {}

        for i in range(len(nums)):
            s[nums[i]] = 0



        answer = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if -1*(nums[i]+nums[j]) in s:
                    if i != j and i != nums.index(-1*(nums[i]+nums[j])) and nums.index(-1*(nums[i]+nums[j])) != j:

                        p = [nums[i], nums[j], -1*(nums[i]+nums[j])]
                        p.sort()
                        if p not in answer:
                            answer.append(p)

        return answer