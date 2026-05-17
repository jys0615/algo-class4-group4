##### 파괴되지 않는 건물 선행학습 #####
### 1D 누적합 먼저 ###
arr = [1, 2, 3, 4, 5]
n = len(arr)
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]

print("원본:", arr)
print("누적합:", prefix)

# 구간 합 [l, r] (0-indexed)
l, r = 1, 3
range_sum = prefix[r+1] - prefix[l] # [1, 3] -> (1+2+3+4) - 1
print(f"구간 합 [{l}, {r}] = prefix[{r+1}] - prefix[{l}] = {prefix[r+1]} - {prefix[l]} = {range_sum}")

### 2D 누적합 ###
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
N, M = 4, 4
prefix = [[0] * (M+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, M+1):
        prefix[r][c] = arr[r-1][c-1] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]

print("2D prefix 배열:")
for row in prefix:
    print(row)

r1, c1, r2, c2 = 0,0,1,1
result = (prefix[r2+1][c2+1]
          - prefix[r1][c2+1]
          - prefix[r2+1][c1]
          + prefix[r1][c1])

print(f"\n구간 합 ({r1},{c1})~({r2},{c2}) = {result}")

######################################################

