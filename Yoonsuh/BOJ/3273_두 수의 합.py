import sys
input = sys.stdin.readline

n = int(input())

arr = sorted(list(map(int, input().split())))
x = int(input())

start = 0
end = n-1

cnt = 0
while start < end:
    if arr[start] + arr[end] <= x:
        cnt+=1
        start+=1
    elif arr[start] + arr[end] < x:
        start+=1
    elif arr[start] + arr[end] > x:
        end-=1

print(cnt)