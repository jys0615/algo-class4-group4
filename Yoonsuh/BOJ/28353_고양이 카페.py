import sys
input = sys.stdin.readline

N, K = map(int, input().split())

w = sorted(list(map(int, input().split())))

cnt = 0

start = 0
end = N - 1

while start < end:
    if w[start] + w[end] <= K:
        cnt+=1
        start+=1
        end-=1
    elif w[start] + w[end] > K:
        end-=1

print(cnt)