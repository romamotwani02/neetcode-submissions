class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countmap={}
        countmapt={}
        for idx,val in enumerate(s):
            if val in countmap:
                countmap[val] = countmap.get(val,0)+1
            else:
                countmap[val]=1
        for idx,val in enumerate(t):
            if val in countmapt:
                countmapt[val] = countmapt.get(val,0)+1 
            else:
                countmapt[val]=1
        print(countmap)
        print(countmapt)
        return (countmap == countmapt)  
        