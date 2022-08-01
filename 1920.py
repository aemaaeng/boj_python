import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

m = int(input())
B = list(map(int, sys.stdin.readline().split()))

def binary_search(A, k, start, end):
    if start > end:
        return False
    
    m = (start + end) // 2
    
    if A[m] == k:
        return True
    elif A[m] > k:
        return binary_search(A, k, start, m-1)
    else:
        return binary_search(A, k, m+1, end)

for i in B:
    if binary_search(A, i, 0, n-1):
        print(1)
    else:
        print(0)