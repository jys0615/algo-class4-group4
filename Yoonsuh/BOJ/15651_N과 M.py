import sys
import itertools
input =sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]

nPr = itertools.product(arr, repeat=M)

for item in nPr:
    print(*item)