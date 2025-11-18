class Solution:
    def isHappy(self, n: int) -> bool:
        t = n
        for i in range(100000):
            t = 0
            for i in str(n):
                t += int(i)**2
            n = t
            if n==1:
                return True

        else:
            return False