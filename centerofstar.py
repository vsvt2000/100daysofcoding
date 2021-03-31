class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        result=0
        print(edges)
        j=0
        i=j+1
        while(i<len(edges)):
            if j==0:
                x=set(edges[i])
                y=set(edges[j])
                result=x.intersection(y)
                j+=1
                i=i+j
                continue
            else:
                x=set(edges[i])
                result=result.intersection(x)
                j+=1
                i=i+j
        return list(result)[0]
            
