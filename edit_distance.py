# Uses python3
def edit_distance(s, t):
    if s==t:
        return 0
    elif len(s)==0 or len(t)==0:
        return len(s) if len(s)>=len(t) else len(t)
    elif len(s)==1 or len(t)==1:
        if len(s)<=len(t):
            return len(t)-1 if s in t else len(t)
        else:
            return len(s)-1 if t in s else len(s)
    else:
        slist=list(map(str,s))
        sn=len(slist)
        tlist=list(map(str,t))
        tn=len(tlist)
        matrix=[[0]*(sn+1) for i in range(tn+1)]
        for i in range(1,sn+1):
            if i==1:
                if tlist[-1]==slist[-i]:
                    matrix[-1][-i]=0
                    for j in range(2,sn+1):
                        matrix[-1][-j]=matrix[-1][-(j-1)]+1
                    break
                else:
                    matrix[-1][-1]=1
            else:
                if tlist[-1]==slist[-i]:
                    matrix[-1][-i]=0+matrix[-1][-(i-1)]
                    for j in range(i+1,sn+1):
                        matrix[-1][-j]=matrix[-1][-(j-1)]+1
                    break
                else:
                    matrix[-1][-i]=1+matrix[-1][-(i-1)]      
        if matrix[-1][-1]==0:
            for i in range(2,tn+1):
                matrix[-i][-1]=matrix[-(i-1)][-1]+1
        else:
            for i in range(2,tn+1):
                if slist[-1]==tlist[-i]:
                    matrix[-i][-1]=0+matrix[-(i-1)][-1]
                    for j in range(i+1,tn+1):
                        matrix[-j][-1]=matrix[-(j-1)][-1]+1
                    break
                else:
                    matrix[-i][-1]=1+matrix[-(i-1)][-1]
        for i in range(2,tn+1):
            for j in range(2,sn+1):
                if tlist[-i]==slist[-j]:
                        matrix[-i][-j]=matrix[-(i-1)][-(j-1)]
                else:
                    matrix[-i][-j]=min(matrix[-i][-(j-1)], matrix[-(i-1)][-j], matrix[-(i-1)][-(j-1)])+1
        return matrix[1][1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
