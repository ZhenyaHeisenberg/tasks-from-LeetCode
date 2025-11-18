class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()

        for i in nums1:
            if i in nums2:
                s.add(i)

        for i in nums2:
            if i in nums1:
                s.add(i)

        return list(s)