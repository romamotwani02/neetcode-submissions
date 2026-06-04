class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        final_list=defaultdict(list)

        for word in strs:
            key="".join(sorted(word))
            final_list[key].append(word)
        
        return(list(final_list.values()))