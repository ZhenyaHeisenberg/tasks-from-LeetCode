class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = {}

        for i in range(len(nums1)):
            s1[nums1[i]] = 0
        for i in range(len(nums2)):
            s1[nums2[i]] = 0

        s2 = s1.copy()

            
        for i in range(len(nums1)):
            s1[nums1[i]] +=1

        for i in range(len(nums2)):
            s2[nums2[i]] +=1

        s = []

        for key, value in s1.items():
            count = min(s1[key], s2[key])
            if count != 0:

                for i in range(count):
                    s.append(key)

        return s