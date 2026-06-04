class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map=dict()
        for n in nums:
            freq_map[n]=freq_map.get(n,0)+1
        major_element_value=float("-inf")
        key1=0
        for key in freq_map:
            if freq_map[key]>major_element_value:
                major_element_value=freq_map[key]
                key1=key
        return key1