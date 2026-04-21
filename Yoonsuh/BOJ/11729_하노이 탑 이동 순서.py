import sys

def hanoi(n, start, end, bypass):
    if n == 1:                          # Base Case: 더 쪼갤 게 없음
        print(f"{start} {end}")
        return

    hanoi(n - 1, start, bypass, end)   # ① n-1개를 경유지로
    print(f"{start} {end}")             # ② 가장 큰 원반 이동
    hanoi(n - 1, bypass, end, start)   # ③ n-1개를 도착지로

n = int(sys.stdin.readline())
print(2**n - 1)  # 총 이동 횟수: 2^n - 1
hanoi(n, 1, 3, 2)