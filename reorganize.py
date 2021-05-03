class Solution(object):
    
    
    def reorganizeString(self, S):
        memo={}
        for i in set(S):
            memo[i]=list(S).count(i)
        x=sum(memo.values())
        target=''
        if len(memo)==1:
            return target
        while(x>0):
            dummy=sorted(memo.items(),key=lambda x:x[1],reverse=True)
            #print(dummy)
            for i in range(2):
                if x>0 and dummy[i][1]>0:
                    if len(target)==0:
                        target+=dummy[i][0]
                        #print(target,"len0")
                        memo[dummy[i][0]]-=1
                        continue

                        
                    if len(target)>0:
                        #print(target[len(target)-1],dummy[i][0])
                        if target[len(target)-1]!=dummy[i][0]:
                            target+=dummy[i][0]
                            #print(target)
                            memo[dummy[i][0]]-=1
                        else:
                            memo[dummy[i][0]]-=1
                        
            x=sum(memo.values())
        if len(target)==len(S):
            return target
        else:
            return ""
                    
                
            
            
            
        
