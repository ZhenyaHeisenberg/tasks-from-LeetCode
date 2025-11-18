class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        setnums = set()

        for i in nums:
            setnums.add(i)

        count = len(setnums)

        nums.clear()

        for i in setnums:
            nums.append(i)

        print(count)