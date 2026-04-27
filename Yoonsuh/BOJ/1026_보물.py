import sys
input = sys.stdin.readline

S = 0

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)


for i in range(N):
    S+=A[i]*B[i]

print(S)