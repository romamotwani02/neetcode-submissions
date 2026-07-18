class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=dict()
        res=list()
        freqcountlist=[[] for i in range(len(nums)+1)]
        for n in nums:
            freq_map[n]=freq_map.get(n,0)+1
        for key,value in freq_map.items():
            freqcountlist[value].append(key)
        
        for i in range(len(freqcountlist)-1,0,-1):
            for num in freqcountlist[i]:
                res.append(num)
            if len(res)==k:
                return res
                