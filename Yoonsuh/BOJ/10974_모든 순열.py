import sys
import itertools
input = sys.stdin.readline

N = int(input())

arr = [i for i in range(1, N+1)]

nPr = itertools.permutations(arr, N)
for item in nPr:
    print(*item)