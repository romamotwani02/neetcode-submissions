class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for str2 in strs:
            res.append(str(len(str2)))
            res.append('#')
            res.append(str2)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0

        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j
        return res