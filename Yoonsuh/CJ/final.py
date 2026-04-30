
# 백트래킹
rs = []
def recur(start):
    if len(rs) == M:
        result.append(rs[:])
    for i in range(start, N+1):
        rs.append(i)
        recur(i+1)
        rs.pop()

dp = [0] * (W+1)
for weight, value in items:
    for w in range(W, weight-1, -1):
        dp[w] = max(dp[w], dp[w-weight]+value)



def can_split(max_sum):
    groups, curr = 1, 0
    for x in arr:
        if curr+x > max_sum:
            groups+=1
            curr = x
        else:
            curr += x
    return groups


arr.sort()
def recur(start, remaining):
    if remaining == 0:
        result.append(rs[:])
        return
    
    for i in range(start, len(arr)):
        if arr[i] > remaining:
            break
        rs.append(arr[i])
        recur(i+1, remaining - arr[i])
        rs.pop()

## result랑 rs 다르게 하고, 전부 다 했으면 결과에 집어넣고 리턴