class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map=dict()
        for i,n in enumerate(nums):
            if target-n in freq_map:
                return([freq_map[target-n],i])
            freq_map[n]=i
