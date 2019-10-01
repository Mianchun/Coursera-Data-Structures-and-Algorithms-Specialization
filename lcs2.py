#Uses python3

import sys

def lcs2(a, b):
    m=len(a)
    n=len(b)
    matrix=[[0]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            matrix[i][j]=matrix[i-1][j-1]+1 if b[i-1]==a[j-1] else max(matrix[i][j-1],matrix[i-1][j])
    return matrix[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
