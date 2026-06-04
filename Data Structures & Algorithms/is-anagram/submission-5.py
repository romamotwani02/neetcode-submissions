class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        freq_map1=dict()
        freq_map2=dict()
        
        for i in range(len(s)):
            freq_map1[s[i]]=freq_map1.get(s[i],0)+1
            freq_map2[t[i]]=freq_map2.get(t[i],0)+1
        return freq_map1==freq_map2
        