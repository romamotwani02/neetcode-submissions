class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map1=dict()
        freq_map2=dict()
        for ch in s:
            freq_map1[ch]=freq_map1.get(ch,0)+1
        for ch in t:
            freq_map2[ch]=freq_map2.get(ch,0)+1
        return freq_map1==freq_map2
        