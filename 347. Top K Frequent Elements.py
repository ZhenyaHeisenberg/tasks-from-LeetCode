class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}

        for i in range(len(nums)):

            if nums[i] in s:
                s[nums[i]] += 1
            else:
                s[nums[i]] = 0
                

        answer = []

        for j in range(k):
            values = s.values()

            max_count = max(values)

            for i in range(len(nums)):
                if s.get(nums[i]) == max_count:
                    key = nums[i]
                    print(key)
                    break
            del s[key]
            answer.append(key)
        return answer