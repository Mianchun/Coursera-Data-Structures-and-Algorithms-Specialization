# Uses python3
def optimal_sequence(n):
    if n<=0:
        step=0
        array=[]
    else:
        matrix=[[(n+1)]*4 for i in range(n+1)]
        matrix[0][0]=-1
        for i in range(1,n+1):
            if i%2==0:
                a=int(i/2)
                matrix[i][1]=min(min(matrix[a])+1,matrix[i][0])
            if i%3==0:
                b=int(i/3)
                matrix[i][2]=min(min(matrix[b])+1,matrix[i][1])
            if i>=1:
                matrix[i][3]=min(min(matrix[i-1])+1,matrix[i][2])
        if min(matrix[n])==n+1:
            step=0
            array=[]
        else:
            step=min(matrix[n])
            tmp=step
            array=[]
            for i in range(1,n+1):
                if min(matrix[-i])==tmp and tmp>=0:
                    if array==[]:
                        array.append(n+1-i)
                        tmp-=1
                    elif (float(array[0])/2==n+1-i or float(array[0])/3==n+1-i or array[0]-1==n+1-i):
                            array.insert(0,n+1-i)
                            tmp-=1
    return array

n=int(input())
sequence = optimal_sequence(n)
sequence = [str(i) for i in sequence]
print(len(sequence) - 1)
print(' '.join(sequence))

