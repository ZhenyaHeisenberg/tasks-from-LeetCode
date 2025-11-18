class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = [""]
        for i in range(k-1):
            s.append("")
            
        s.extend(nums)

        for i in range(k):
            s.append("")

        for i in range(len(nums)):
            for j in range(i-k, i+k):
                if (nums[i] == s[j]) and (i != j+k) and abs(i-j+k) <= k:
                    return True
        return False