class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            a = set()
            b = set()
            for i in s:
                a.add(ord(i))
            for i in t:
                b.add(ord(i))

            if a == b:
                return True
            else:
                return False