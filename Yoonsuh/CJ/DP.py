### 0/1 배낭 ###
# 문제: 무게 W 이하로 담을 수 있는 최대 가치
items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (무게, 가치)
W = 8  # 최대 무게

dp = [0] * (W + 1)
print(f"초기 dp: {dp}")

for i, (weight, value) in enumerate(items):
    print(f"\n--- 아이템 {i+1}: 무게={weight}, 가치={value} ---")
    for w in range(W, weight - 1, -1):  # 역순 핵심!
        before = dp[w]
        dp[w] = max(dp[w], dp[w - weight] + value)
        if dp[w] != before:
            print(f"  dp[{w}]: {before} → {dp[w]}  (dp[{w-weight}]={dp[w-weight]} + {value})")

print(f"\n최종 dp: {dp}")
print(f"답: {dp[W]}")

