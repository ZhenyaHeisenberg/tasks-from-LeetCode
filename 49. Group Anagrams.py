class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        s = {}
                
        for i in strs:
            string = sorted(i) # eat -> aet
            key = ''.join(string)

                    
            if key not in s:
                s[key] = []
            s[key].append(i)
                
        return list(s.values())