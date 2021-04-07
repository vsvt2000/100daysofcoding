class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        x=set(allowed)
        count=0
        for i in words:
            if x.issuperset(i):
                count+=1
        return count
        
