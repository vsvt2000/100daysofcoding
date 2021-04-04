class Solution:
    def isValid(self, s: str) -> bool:
        s1=[]
        s2=[]
        count=0
        for i in s:
            if i in '({[':
                s1.append(i)
                count+=1
                continue
            else:
                if len(s1)>0:
                    if (s1[len(s1)-1]=='(' and i==')') or (s1[len(s1)-1]=='{' and i=='}') or (s1[len(s1)-1]=='[' and i==']'):
                        s1.pop()
                        count+=1
                        
        if count==len(s) and len(s1)==0:
            return True
        else:
            return False
