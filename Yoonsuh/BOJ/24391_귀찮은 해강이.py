import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(M+1)]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i].append(j)
A = list(map(int, input().split()))
print(*arr)