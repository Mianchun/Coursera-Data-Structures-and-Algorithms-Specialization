# Uses python3

def get_change(m):
    #write your code here
    if m<=0:
        return 0
    else:
        matrix=[[(m+1)]*4 for i in range(m+1)]
        matrix[0][0]=0
        for i in range(1,m+1):
            if i>=1:
                matrix[i][1]=min(min(matrix[i-1])+1,matrix[i][0])
            if i>=3:
                matrix[i][2]=min(min(matrix[i-3])+1,matrix[i][1])
            if i>=4:
                matrix[i][3]=min(min(matrix[i-4])+1,matrix[i][2])
        if min(matrix[m])==m+1:
            return None
        else:
            return min(matrix[m])


m = int(input())
print(get_change(m))
