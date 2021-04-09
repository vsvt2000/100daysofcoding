class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        X=list(S)
        stack=[]
        i=0
        while(i<len(X)):
            if X[i]=='(':
                stack.append(X[i])
                if len(stack)==1:
                    X.pop(i)
                else:
                    i+=1
                continue
            if X[i]==')':
                stack.pop()
                if len(stack)==0:
                    X.pop(i)
                else:
                    i+=1
        ss=""
        for j in X:
            ss=ss+j
            
        return ss
