class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans2=list()
        n=len(nums)
        for i in range(0,n):
            ans2.insert(i,nums[i])
            ans2.insert(i+n,nums[i])
        return ans2
        