    # Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    elif left + 1 == right:
        return a[left]
    #write your code here
    else:
        a.sort()
        mid=right//2
        ans=a[mid]
        count=0
        for item in a:
            if item==ans:
                count+=1
        if count>float(right)/2:
            return 1
        else:
            return -1
                
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
